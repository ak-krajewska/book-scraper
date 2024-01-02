# pandas, requests, and beautifulsoup4 are not standard libraries
# if you don't have them installed, install them using:
# pip3 install pandas requests beautifulsoup4

# imports libraries (Pandas, requests, BeautifulSoup) for web scraping and data manipulation
import pandas as pd
import requests
from bs4 import BeautifulSoup

# send a request to Goodreads
base_url = 'https://www.goodreads.com/shelf/show/self-help'
response = requests.get(base_url)
# print(response.text) # check if the response worked
html_content = response.text
# print(html_content) # check if the response worked

# create a Beautiful Soup object to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# calculate pages to scrape

# for the purposes of the learning example
# just assign the number of pages
# and items per page

total_pages = 10 # magic number, assigning just for practice
max_pages_to_scrape = 2 # magic number, assigning just for practice

# create empty lists to store the data that script will scrape
# This is a weird data structure but I'm going to keep it
# just so I can fit it with the example code, hopefully

title = []
url_list = []
authors = []
avg_ratings = []
rating = []
year = []

# iterate through the pages to scrape
# TODO make quotatin marks consistent

for page in range(1, min(max_pages_to_scrape, total_pages) + 1):
    # Construct the URL for the current page
    url = f"{base_url}?page={page}"
    # print(url) #check that the url pagination is working
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    book_elements = soup.find_all("div", "elementList")
    # print(book_elements) #check that the books are getting slurped up correctly

# structure data into a dataset for analysis

# display the first few rows to gut check dataset before saving

# save data to a CSV
