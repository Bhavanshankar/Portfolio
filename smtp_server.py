#!/usr/bin/env python3
"""Minimal SMTP API for contact form submissions.

Run:
    python smtp_server.py

Environment variables:
    SMTP_HOST        (required) e.g. smtp.gmail.com
    SMTP_PORT        (optional) default 587
    SMTP_USERNAME    (required)
    SMTP_PASSWORD    (required)
    SMTP_FROM        (optional) default SMTP_USERNAME
    SMTP_TO          (optional) default skillx192@gmail.com
    SMTP_USE_TLS     (optional) true/false, default true
    ALLOWED_ORIGINS  (optional) comma-separated origins or *
    PORT             (optional) default 5000
    HOST             (optional) default 0.0.0.0
"""

import json
import os
import smtplib
from email.message import EmailMessage
from http.server import BaseHTTPRequestHandler, HTTPServer


def _env_bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def send_smtp_email(name: str, email: str, subject: str, message: str) -> None:
    smtp_host = os.getenv("SMTP_HOST", "").strip()
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USERNAME", "").strip()
    smtp_pass = os.getenv("SMTP_PASSWORD", "").strip()
    smtp_from = os.getenv("SMTP_FROM", smtp_user).strip()
    smtp_to = os.getenv("SMTP_TO", "skillx192@gmail.com").strip()
    use_tls = _env_bool("SMTP_USE_TLS", True)

    missing = []
    if not smtp_host:
        missing.append("SMTP_HOST")
    if not smtp_user:
        missing.append("SMTP_USERNAME")
    if not smtp_pass:
        missing.append("SMTP_PASSWORD")
    if not smtp_from:
        missing.append("SMTP_FROM")

    if missing:
        raise RuntimeError("Missing SMTP settings: " + ", ".join(missing))

    email_message = EmailMessage()
    email_message["Subject"] = f"Portfolio Contact: {subject}"
    email_message["From"] = smtp_from
    email_message["To"] = smtp_to
    email_message["Reply-To"] = email
    email_message.set_content(
        "\n".join(
            [
                f"Name: {name}",
                f"Email: {email}",
                "",
                "Message:",
                message,
            ]
        )
    )

    with smtplib.SMTP(smtp_host, smtp_port, timeout=20) as server:
        if use_tls:
            server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(email_message)


class ContactHandler(BaseHTTPRequestHandler):
    def _resolve_cors_origin(self) -> str:
        origin = self.headers.get("Origin", "")
        allowed_raw = os.getenv("ALLOWED_ORIGINS", "*")
        allowed = [item.strip() for item in allowed_raw.split(",") if item.strip()]

        if not allowed or "*" in allowed:
            return "*"
        if origin in allowed:
            return origin
        return allowed[0]

    def _set_headers(self, status_code: int = 200) -> None:
        cors_origin = self._resolve_cors_origin()
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", cors_origin)
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self) -> None:
        if self.path == "/health":
            self._set_headers(200)
            self.wfile.write(json.dumps({"ok": True}).encode("utf-8"))
            return

        self._set_headers(404)
        self.wfile.write(json.dumps({"error": "Not found"}).encode("utf-8"))

    def do_OPTIONS(self) -> None:
        self._set_headers(200)
        self.wfile.write(json.dumps({"ok": True}).encode("utf-8"))

    def do_POST(self) -> None:
        if self.path != "/send-email":
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not found"}).encode("utf-8"))
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
            raw_body = self.rfile.read(content_length).decode("utf-8")
            payload = json.loads(raw_body)

            name = str(payload.get("name", "")).strip()
            email = str(payload.get("email", "")).strip()
            subject = str(payload.get("subject", "")).strip()
            message = str(payload.get("message", "")).strip()

            if not name or not email or not subject or not message:
                self._set_headers(400)
                self.wfile.write(
                    json.dumps({"error": "All fields are required."}).encode("utf-8")
                )
                return

            send_smtp_email(name, email, subject, message)
            self._set_headers(200)
            self.wfile.write(
                json.dumps({"message": "Message sent successfully via SMTP."}).encode("utf-8")
            )

        except json.JSONDecodeError:
            self._set_headers(400)
            self.wfile.write(json.dumps({"error": "Invalid JSON payload."}).encode("utf-8"))
        except Exception as exc:
            self._set_headers(500)
            self.wfile.write(json.dumps({"error": str(exc)}).encode("utf-8"))


def main() -> None:
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "5000"))
    server = HTTPServer((host, port), ContactHandler)
    print(f"SMTP API running at http://{host}:{port}")
    print("Endpoint: POST /send-email")
    server.serve_forever()


if __name__ == "__main__":
    main()
