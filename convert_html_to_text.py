import json
from bs4 import BeautifulSoup

with open("input.html") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# Find the HTML body content
body_content = soup.body if soup.body else soup

# Get the original HTML including tags for specified tags
html_tags = ["h1", "h2", "h3", "h4", "h5", "h6", "p", "b"]

original_html_tags = body_content.find_all(html_tags)
original_html = "".join(str(tag) for tag in original_html_tags)

output = []
for elem in body_content:
    if not elem.name:
        continue

    tag = elem.name
    attributes = ""

    if tag in html_tags and elem.parent.has_attr("style"):
        attributes = str(elem.parent.attrs)

    # Check if the string representation of the tag is already present in the "original_html" field
    if str(elem) not in original_html:
        output.append(f"<{tag}{attributes}>{elem}</{tag}>")

result_html = "".join(output)

# Create a dictionary to store relevant information
result_data = {
    "original_html": original_html,
    "single_line_html": result_html
}

# Writing the dictionary to a JSON file
with open("output.json", "w", encoding="utf-8") as json_file:
    json.dump(result_data, json_file, indent=2)

print("Output written to 'output.json'")
