# pandas, requests, and beautifulsoup4 are not standard libraries
# if you don't have them installed, install them using:
# pip3 install pandas requests beautifulsoup4

# imports libraries (Pandas, requests, BeautifulSoup) for web scraping and data manipulation
import pandas as pd
import requests
from bs4 import BeautifulSoup

# send a request to Goodreads
url = 'https://www.goodreads.com/shelf/show/self-help'
response = requests.get(url)
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

# iterate through the pages to scrape

# structure data into a dataset for analysis

# display the first few rows to gut check dataset before saving

# save data to a CSV
