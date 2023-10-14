import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = "https://example.com/blog"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find and extract specific elements from the page
    article_titles = soup.find_all("h2", class_="article-title")

    # Iterate through the extracted elements and print their text
    for title in article_titles:
        print(title.text)
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
