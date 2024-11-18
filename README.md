**Web Scraping with Python**

This project demonstrates how to scrape and parse web content using Python, specifically from a Wikipedia page. 
The script extracts the page title and organizes headings (h2 tags) with their corresponding paragraphs (p tags).

**Features**

# Retrieve Web Page Content: Fetch HTML content from a given URL using the requests library.
# Parse HTML with Beautiful Soup: Use the Beautiful Soup library to parse the content.
# Extract Specific Information:
# Page title (<span> tag with a specific class).
# Headings (h2 tags) and their corresponding paragraphs (p tags).
# Output Results: Display the extracted content in a structured dictionary format.

**Prerequisites**
Before running the script, ensure you have the following installed:

# Python 3.7+
# Required Libraries:
# requests
# pandas
# beautifulsoup4

**To install the required libraries, run:**

bash
Copy code
pip install requests pandas beautifulsoup4


**How It Works**

# Functions
# get_and_parse(url)

# Fetches the HTML content of a URL.
# Parses the content using Beautiful Soup.
# extract_article_title(parsed_webpage)

# Extracts and returns the main title of the webpage.
# extract_heading_and_text(parsed_webpage)

# Iterates through headings (h2 tags) and paragraphs (p tags).
Organizes the extracted data into a dictionary where each heading maps to its related paragraphs.
# main_function(wiki_link)
Combines the above functionalities to fetch, parse, and display content from a given Wikipedia link.
Usage

Clone or download this script.
Update the wiki_link parameter in the main_function call with the URL of a Wikipedia page you want to scrape.
Run the script:
bash
Copy code
python web_scraping.py
**The script will display:**

The page title.
A dictionary where each key is a heading, and its value is a list of associated paragraphs.

**Example Output**
For the input URL: https://en.wikipedia.org/wiki/Java_(programming_language), the script will output:
plaintext
Copy code
Executing Scrapping...
Getting Wiki Page
Parsing Wiki Content with Beautiful soup...
Done Parsing Webpage...
Extracting Article from Wiki Page
The Webpage title is Java (programming language)
{'Overview': ['Java is a high-level, class-based, ...', ...]}

**Notes**
Dynamic Content: This script is intended for static web pages. Dynamic content generated with JavaScript may require tools like Selenium.
Error Handling: Ensure the URL is correctly formatted and accessible.
Legal Compliance: Verify that the website permits web scraping in its terms of service.


