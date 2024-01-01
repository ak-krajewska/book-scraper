#imports necessary libraries (Pandas, requests, BeautifulSoup) for web scraping and data manipulation.

import pandas as pd
import requests
from bs4 import BeautifulSoup

# send a request to goodreads
url = "https://www.goodreads.com/shelf/show/self-help"
response = requests.get(url)
html_content = response.text

# create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response, "html.parser")

# calculate pages to scrape
total_items_info = soup.find("div", class_="mediumText").get_text().strip()
total_items = int(total_items_info.split()[-1].replace(',', ''))

items_per_page = 50  # Adjust this based on the actual number of items per page
total_pages = (total_items + items_per_page - 1) // items_per_page
max_pages_to_scrape = 2 # Changed from samples 200 to just 2

# create empty lists to store the data that script will scrape
title = []
url_list = []
authors = []
avg_ratings = []
rating = []
year = []

# iterate through the pages to scrape
for page in range(1, min(max_pages_to_scrape, total_pages) + 1):
    # Construct the URL for the current page
    url = f"{base_url}?page={page}"
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    book_elements = soup.find_all("div", "elementList")
    
    # Iterate through each book element on the current page
    for book_element in book_elements:
        # Use try-except blocks to handle potential errors if elements are missing
        try:
            # Extract book details
            book_title = book_element.find("a", "bookTitle").text
            book_url = "https://www.goodreads.com" + book_element.find("a", "bookTitle").get("href")
            author = book_element.find("a", "authorName").text
            rating_text = book_element.find("span", "greyText smallText").text.split()
            avg_rating = rating_text[2]
            ratings = rating_text[4]
            published_year = rating_text[-1] if len(rating_text) == 9 else ""
    
            # Append the extracted data to their respective lists
            title.append(book_title)
            url_list.append(book_url)
            authors.append(author)
            avg_ratings.append(avg_rating)
            rating.append(ratings)
            year.append(published_year)
        except AttributeError:
            # Handle the case where an element is not found
            print(f"Skipping a book on page {page} due to missing data.")

# structure data into a dataset for analysis
good_reads = pd.DataFrame({
    "Title": title,
    "URL": url_list,
    "Authors": authors,
    "Avg Ratings": avg_ratings,
    "Rating": rating,
    "Published_year": year
})

# display the first few rows to gut check dataset before saving
good_reads.head()

# save data to a CSV
good_reads.to_csv("goodreads.csv", index=False)