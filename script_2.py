# Let's extract the specific sections we need to update
# and create the updated version with Bhavan's details

# Extract the body content
body_content = content[content.find('<body'):content.find('</body>') + 7]

# Now let's create the updated HTML with Bhavan's information
updated_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bhavan Shankar M - Creative Technologist & Digital Developer</title>
    <meta name="description" content="Immersive portfolio of Bhavan Shankar M - Where creativity meets technology in stunning digital experiences">
    <meta property="og:title" content="Bhavan Shankar M - Creative Technologist Portfolio">
    <meta property="og:description" content="Step into a world where art and code collide">
    <meta property="og:type" content="website">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        neon: '#00ff88',
                        cyber: '#ff0080',
                        electric: '#00d4ff',
                        plasma: '#ff6b00',
                        void: '#0a0a0f',
                        'void-light': '#1a1a2e'
                    },
                    fontFamily: {
                        'cyber': ['Orbitron', 'monospace'],
                        'display': ['Poppins', 'sans-serif']
                    }
                }
            }
        }
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">'''

# Continue with the original styles and scripts
style_start = content.find('<style>')
style_end = content.find('</head>') + 7
styles_and_head_end = content[style_start:style_end]

updated_html += styles_and_head_end

print("Created HTML head section successfully")
print("Length of updated HTML so far:", len(updated_html))