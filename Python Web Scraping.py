import requests
import pandas as pd
from bs4 import BeautifulSoup

# Function to get and parse HTML content from a Wiki page
def get_and_parse(url):
    print("Getting Wiki Page")
    try:
        webpage = requests.get(url)
        print("Parsing Wiki Content with Beautiful soup...")
        parsed_webpage = BeautifulSoup(webpage.content, "html.parser")
        print("Done Parsing Webpage...")
        return parsed_webpage
    except:
        print("Could Not parse link ensure you put in the right light")
        return None

# Function to extract the title of the article
def extract_article_title(parsed_webpage):
    print("Extracting Article from Wiki Page")
    article_title = parsed_webpage.find("span", {"class": "mw-page-title-main"}).text
    return article_title

# Function to extract headings and their corresponding paragraphs
def extract_heading_and_text(parsed_webpage):
    content = {}
    current_header = None
    corresponding_paragraphs = []

    # Use find_all instead of findall
    headers_and_paragraphs = parsed_webpage.find_all(["h2", "p"])

    for element in headers_and_paragraphs:
        if element.name == "h2":
            # Save the previous header and its paragraphs
            if current_header is not None and len(corresponding_paragraphs) != 0:
                content[current_header] = corresponding_paragraphs
            
            # Extract the new header text
            current_header = element.text.strip()
            corresponding_paragraphs = []
        elif element.name == "p":
            # Append paragraphs to the current header
            corresponding_paragraphs.append(element.text.strip())
    
    # Add the last header and paragraphs
    if current_header is not None and len(corresponding_paragraphs) != 0:
        content[current_header] = corresponding_paragraphs

    return content

# Main function to execute the web scraping process
def main_function(wiki_link):
    print("Executing Scrapping...")
    parsed_webpage = get_and_parse(wiki_link)
    if parsed_webpage is None:
        return
    title = extract_article_title(parsed_webpage)
    print(f"The Webpage title is {title}")
    content = extract_heading_and_text(parsed_webpage)
    print(content)

# Run the main function with a specific Wikipedia page link
main_function("https://en.wikipedia.org/wiki/Java_(programming_language)")
