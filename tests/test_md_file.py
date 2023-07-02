import os
import pytest

def read_md_file(file_path):
    # Implement the logic to read the content of an MD file
    pass

def check_file_extension(file_name):
    # Implement the logic to check the file extension
    pass

def parse_md_file(content):
    # Implement the logic to parse the content of an MD file
    pass

def generate_html_from_md(content):
    # Implement the logic to generate HTML from an MD file
    pass

def write_html_file(html, file_name):
    # Implement the logic to write HTML content to a file
    pass

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

def test_write_html_file():
    html = "<h1>Heading</h1>"
    file_name = "output.html"
    write_html_file(html, file_name)
    
    assert os.path.exists(file_name)
    
    with open(file_name, "r") as file:
        file_content = file.read()
        assert html in file_content
