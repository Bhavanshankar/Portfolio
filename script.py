# Read the index.html file to see the complete content
with open('index.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Display the first 3000 characters to understand the structure
print("First 3000 characters of index.html:")
print(content[:3000])
print("\n" + "="*50 + "\n")

# Display the length of the file
print(f"Total file length: {len(content)} characters")