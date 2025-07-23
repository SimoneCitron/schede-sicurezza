import os
import re

# Path to the directory containing PDF files
pdf_directory = "./schede"
output_file = "index.html"

# Regex pattern to extract product name and version number
pattern = re.compile(r"^(?P<name>.+)-v(?P<version>\d+)\.pdf$")

# Dictionary to store the latest version of each product
latest_versions = {}

# Scan the directory
for file in os.listdir(pdf_directory):
    if file.endswith(".pdf"):
        match = pattern.match(file)
        if match:
            name = match.group("name")
            version = int(match.group("version"))
            if name not in latest_versions or version > latest_versions[name][0]:
                latest_versions[name] = (version, file)

# Generate the HTML content
html_content = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Schede di Sicurezza – Ultime Versioni</title>
</head>
<body>
    <h1>Schede di Sicurezza – Ultime Versioni</h1>
    <ul>
"""

for name, (version, filename) in sorted(latest_versions.items()):
    html_content += f'        <li><a href="schede/{filename}" target="_blank">Scheda {name.upper()}</a></li>\n'

html_content += """    </ul>
</body>
</html>
"""

# Write the output HTML file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"File '{output_file}' generato con successo.")
