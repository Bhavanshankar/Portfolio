# Let's see more of the content to understand the structure better
# Look for the main sections and content areas

# Find key sections
sections = []
lines = content.split('\n')

current_section = ""
for i, line in enumerate(lines):
    if '<section' in line or '<div class=' in line:
        # Get some context around important sections
        if any(keyword in line.lower() for keyword in ['hero', 'about', 'skills', 'projects', 'contact', 'experience']):
            sections.append(f"Line {i}: {line.strip()}")

print("Key sections found:")
for section in sections[:20]:  # Show first 20 sections
    print(section)

print("\n" + "="*50 + "\n")

# Look for the actual content sections
import re

# Find the main content areas
hero_match = re.search(r'<section[^>]*class[^>]*hero[^>]*>(.*?)</section>', content, re.DOTALL | re.IGNORECASE)
about_match = re.search(r'<section[^>]*class[^>]*about[^>]*>(.*?)</section>', content, re.DOTALL | re.IGNORECASE)

print("Looking for main content structure...")
if hero_match:
    print("Hero section found")
if about_match:
    print("About section found")
    
# Let's find where the actual content starts and ends
content_start = content.find('<body')
content_end = content.find('</body>')

print(f"Body content from character {content_start} to {content_end}")