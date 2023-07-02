import os
import pytest

def test_read_md_file():
    # Assume you have a function called read_md_file that reads the content of an MD file
    content = read_md_file("example.md")
    assert isinstance(content, str)
    assert len(content) > 0

def test_check_file_extension():
    # Assume you have a function called check_file_extension that checks the file extension
    assert check_file_extension("example.md") == True
    assert check_file_extension("example.txt") == False

def test_parse_md_file():
    # Assume you have a function called parse_md_file that parses the content of an MD file
    content = "# Heading\n\nText"
    parsed_data = parse_md_file(content)
    assert parsed_data["title"] == "Heading"
    assert parsed_data["text"] == "Text"

def test_generate_html_from_md():
    # Assume you have a function called generate_html_from_md that generates HTML from an MD file
    content = "# Heading\n\nText"
    html = generate_html_from_md(content)
    assert "<h1>Heading</h1>" in html
    assert "<p>Text</p>" in html

def test_write_html_file():
    # Assume you have a function called write_html_file that writes HTML content to a file
    html = "<h1>Heading</h1>"
    file_name = "output.html"
    write_html_file(html, file_name)
    
    # Check that the file exists
    assert os.path.exists(file_name)
    
    # Check that the file contains the expected HTML
    with open(file_name, "r") as file:
        file_content = file.read()
        assert html in file_content
