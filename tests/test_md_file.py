import os
import pytest

def read_md_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content

def check_file_extension(file_name):
    return file_name.endswith(".md")

def parse_md_file(content):
    lines = content.split("\n")
    title = lines[0].strip("# ")
    text = "\n".join(lines[1:]).strip()
    return {"title": title, "text": text}

def generate_html_from_md(content):
    lines = content.split("\n")
    html_lines = []
    for line in lines:
        if line.startswith("# "):
            html_lines.append(f"<h1>{line.strip('# ')}</h1>")
        else:
            html_lines.append(f"<p>{line}</p>")
    return "\n".join(html_lines)

def write_html_file(html, file_name):
    with open(file_name, "w") as file:
        file.write(html)

def test_read_md_file():
    content = read_md_file("example.md")
    assert isinstance(content, str)
    assert len(content) > 0

def test_check_file_extension():
    assert check_file_extension("example.md") == True
    assert check_file_extension("example.txt") == False

def test_parse_md_file():
    content = "# Heading\n\nText"
    parsed_data = parse_md_file(content)
    assert parsed_data["title"] == "Heading"
    assert parsed_data["text"] == "Text"

def test_generate_html_from_md():
    content = "# Heading\n\nText"
    html = generate_html_from_md(content)
    assert "<h1>Heading</h1>" in html
    assert "<p>Text</p>" in html

def test_write_html_file(tmpdir):
    html = "<h1>Heading</h1>"
    file_name = os.path.join(tmpdir, "output.html")
    write_html_file(html, file_name)
    
    assert os.path.exists(file_name)
    
    with open(file_name, "r") as file:
        file_content = file.read()
        assert html in file_content
