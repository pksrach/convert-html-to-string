def convert_html_to_single_line(html_content):
    # Remove newlines and extra spaces
    single_line_html = ' '.join(html_content.split())
    return single_line_html

if __name__ == "__main__":
    # Read HTML content from input.html file
    with open("input.html", "r") as file:
        html_content = file.read()

    # Convert HTML content to a single line
    single_line_html = convert_html_to_single_line(html_content)

    # Write the single-line HTML content to output.txt file
    with open("output.txt", "w") as output_file:
        output_file.write(single_line_html)

    print("Single-line HTML content has been written to output.txt")