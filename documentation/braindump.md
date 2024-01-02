# Running braindump

A reverse-chronological collection of notes, questions, references, plans, and pretty much everything else that comes up as I work on this project. 

## 2024.01.01

### Attempt to write a scraper that does what the Medium tutorial purported to do

I created a new file, keeping the comments to help me structure it along with the imports header which I know works: `medium_exercise/shelf_scraper.py`

#### Send a request to Goodreads

[Requests library documentation](https://docs.python-requests.org/en/latest/index.html)

[Make a Request](https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request)

I can adapt this to my code. This is how:

```
response = requests.get('https://www.goodreads.com/shelf/show/self-help')
print(response.text)
```

If I try to just print `response` I get a type error because that's the whole response object. response.text grabs all the text, in this case, the entire HTML page. It works!

Now I'll rework it so the URL is a variable for better reuseability, and also create a variable for the html_content, just following the exercise. It works!

#### Create a Beautiful Soup object to parse the HTML content

[Beautiful Soup Documentation](https://beautiful-soup-4.readthedocs.io/en/latest/)

Here's how to pass text into Beautiful Soup [Making the Soup](https://beautiful-soup-4.readthedocs.io/en/latest/#making-the-soup)

Now I am a little hungry.

`soup = BeautifulSoup(html_content)` works but I get a warning that no parser was explicitly specified and it defaults to HTML. ChatGPT suggests specifying the HTML parser. The documentation has a section about that:

[Specifying the parser to use](https://beautiful-soup-4.readthedocs.io/en/latest/#specifying-the-parser-to-use)

It looks like the parser should be the second argument, like so `soup = BeautifulSoup(html_content, 'html.parser')`

And that worked! (After an initial syntax error where I accidentally typed in "parser.html" instead).

I used `print(soup)` just to check what the output looks like and it looks like nicely formatted HTML. 

#### Calculate pages to scrape

After poring over the example from the article, I realized it's reading the little thingie at the top of the page that says "Showing 1-50 of 100,000" and then manipulating that string to figure out the number of items total, and turn that into an int. For some reason the example is just assigning the items per page even though it could detect that, too. All this made me realize that if I want to learn to scrape a couple of pages from a known list first, I could just assign the numbers of items per page and the number of pages directly and come back to write this later.

#### Create empty lists to store the data that script will scrape

This is a weird data structure but I'm going to keep it just so I can fit it with the example code, hopefully.

#### Iterate through the pages to scrape

Figured out how to go through the pages. I mostly based this on the article example, except that the article had "base_url" a variable that was previously not defined. But if you use just "url" it gets wacky.

### Attempt to use Medium article

**Summary:** The code given in the article doesn't run and I am giving up on it. Read this section for the saga.

I should probably follow one of the existing scraper scripts and try to make it work before I go further down the data structure rabbit hole. 

I've decided to use [Scraping Goodreads: A Beginner’s Guide](https://medium.com/@adesua/scraping-goodreads-a-beginners-guide-3ad3a5907c2a).

#### Install vs import

What's the difference between importing a library and installing a library? That is, what's the difference between

```
pip install requests
```

and 

```
import requests
```

Answer (after conversation with friend):

`install` is for installing the library into your development environment, for example, your computer. You only have to do it once (except for upgrades, of course).

`import` is for making the library available in your code, for a particular program. You have to import whenever you want to use the library.

Previously, I thought Python was kind of magic because it seemed like you could `import` whatever you wanted without having to install it. That was just because Python has a bunch of built-in libraries it comes with, called standard libraries. Why not always have all the standard libraries available? Because it keeps the code smaller to only import the libraries you're going to use. 

Useful note: It doesn't matter what directory you're in when running `pip install`.

#### Trying to install - friction log

`pip install beautifulsoup4 requests` threw an error

```
potentia-est:book-scraper akrajewska$ pip install beautifulsoup4 requests
-bash: /usr/local/bin/pip: /usr/bin/python: bad interpreter: No such file or directory
```

This is probably because `pip` assumes Python 2 and I am on Python 3. Weird that the instructions are written this way since the article was published Sept 12, 2023. 

Onward then with `pip3` instead.

It's a new and different error message:

```
potentia-est:book-scraper akrajewska$ pip3 install beautifulsoup4 requests
pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
Collecting beautifulsoup4
  Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/beautifulsoup4/
  Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/beautifulsoup4/
  Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/beautifulsoup4/
  Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/beautifulsoup4/
  Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/beautifulsoup4/
  Could not fetch URL https://pypi.org/simple/beautifulsoup4/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/beautifulsoup4/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.")) - skipping
  Could not find a version that satisfies the requirement beautifulsoup4 (from versions: )
No matching distribution found for beautifulsoup4
pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.")) - skipping
potentia-est:book-scraper akrajewska$ 
```

Checking where my python3 lives:

```
potentia-est:book-scraper akrajewska$ which python3
/usr/local/bin/python
```

Apparently this is weird and past me may have done something weird and/or bad. Also checking my Python version:

```
potentia-est:book-scraper akrajewska$ python3 --version
Python 3.7.1
```

Also it's out of date. Getting an update from https://www.python.org/.

Downloads > Download for macOS

Ran through the wizard, which has a lot of blah blah blah, but one rather important bit at the end

```
Congratulations!  Python 3.12.1 for macOS 10.9 or later was successfully installed.

One more thing: to verify the identity of secure network connections, this Python needs a set of SSL root certificates.  You can download and install a current curated set from the Certifi project by double-clicking on the Install Certificates icon in the Finder window.  See the ReadMe file for more information.
```

I probably skipped this (because blah blah blah) when I installed the old version of Python previously.

So in Finder, I click Install Certificates.command and it fires up a terminal window and runs some processes, with a confirmation message like this that it finished

```
Installing collected packages: certifi
Successfully installed certifi-2023.11.17
```

Now that I have updated and installed the certificate, I try again:

```
pip3 install beautifulsoup4 requests
```

And now it works! Success, victory, etc.

**Lesson learned**: Past me clicked through a bunch of boring text and it turned out some of it was important. Maybe more actionable lesson: Think about security certificates.

#### Set up the file

I'm going to keep this exercise in a file I hope will make sense to future me:

medium_exercise/beginners_guide_exercise.py

Also VScode suggested installing a Python extension so I'm doing that.

Now I put this at the start of my new file:

```
#imports necessary libraries (Pandas, requests, BeautifulSoup) for web scraping and data manipulation.

import pandas as pd
import requests
from bs4 import BeautifulSoup
```

Following the exercise is mostly copy-paste at this point.

```
import requests

url = "https://www.goodreads.com/"
response = requests.get(url)
html_content = response.text
```

Why is the code snippet telling me to import requests again? Seems weird. Is the exercise expecting I'll do this in a different file? I confess I haven't been reading that closely.

I read the article all the way through. Arguably maybe I should have done that to begin with, just like you're supposed to read the whole recipe before you start cooking. Luckily with code, you can always unscramble the eggs, as it were. Anyway, the author helpfully provides a link to their GitHub repo at the end so I can find an answer to my question about the seemingly doubled import.

https://github.com/Adesuaayo/goodreads_webscraper/tree/main

OK, no. The project described in the repo appears to be a different one than described in the Medium article. It imports additional dependencies and seems to output some kind of top rating analysis. Whatever I guess I'll have to use my own reasoning to figure the rest of this out. Onward. Also the audience for this sample code seems to be data analysts who want to analyze Goodreads, not book nerds who want to extract their own data. 

Copy-pasted all the code samples from the Medium article with the following changes:
- Omitted duplicative `requests` import
- Changed maxed number of pages to scrape to 2 from 200 (2 to make sure pagination works, but keeping it short)
- Added comments to each code block so future me knows WTF I meant

#### Debugging the sample code

1. No pandas

Ran code, got this error:

```
potentia-est:book-scraper akrajewska$ /usr/local/bin/python3 /Users/akrajewska/Documents/projects/book-scraper/medium_exercise/beginners_guide_exercise.py
Traceback (most recent call last):
  File "/Users/akrajewska/Documents/projects/book-scraper/medium_exercise/beginners_guide_exercise.py", line 3, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'
```

I wonder what's the difference between a module and a library. I guess the article author must have already had `pandas` installed into their environment and didn't think to include it in the setup instructions. 

To fix, I'm running

```
potentia-est:book-scraper akrajewska$ pip3 install pandas
```

That fixed the pandas error.

2. BeautifulSoup finds the Response object has no len()

```
potentia-est:book-scraper akrajewska$ /usr/local/bin/python3 /Users/akrajewska/Documents/projects/book-scraper/medium_exercise/beginners_guide_exercise.py
Traceback (most recent call last):
  File "/Users/akrajewska/Documents/projects/book-scraper/medium_exercise/beginners_guide_exercise.py", line 13, in <module>
    soup = BeautifulSoup(response, "html.parser")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/bs4/__init__.py", line 315, in __init__
    elif len(markup) <= 256 and (
         ^^^^^^^^^^^
TypeError: object of type 'Response' has no len()
```

I think that means that the Response object is not the type of object that has a len() method. This is a bit more thorny. I will ask my coding buddy, ChatGPT, for help.

Here's what ChatGPT says

```
The error indicates a TypeError in the BeautifulSoup constructor, specifically related to the length of the markup. The markup argument for BeautifulSoup is expected to be a string or an object that supports the Python len() function. In this case, it seems like you are passing a Response object, which does not have a length.

You should extract the content from the Response object before passing it to BeautifulSoup. Assuming you are using the requests library for making HTTP requests, you can modify your code like this:
```

Then it gives some sample code. So my guess and ChatGPTs suggestion match. I am using the requests library, so the fix will probably work.

Something feels deeply wrong here. Why are we going to the Goodreads front page for the request? Instead of, as the exercise says earlier, the self-help books list, that is `https://www.goodreads.com/shelf/show/self-help`? 

I'm starting to wonder if this is even real, workable code or just a content farm copypasta. I'm guilty of copy-pasting myself but now I wonder if I'd be better off just starting this from scratch and using ChatGPT to help me. 

I'm going to try replacing the vague URL with `https://www.goodreads.com/shelf/show/self-help`.

It doesn't make a difference I still get the same error. 

Time to "phone a friend" and get an expert opinion if this is even a reasonable bit of sample code to follow.

#### Abandon ship

After consulting with a Python expert, I am abandoning this exercise and will instead write something from scratch. There are indeed a lot of errors and the code doesn't all fit together. These are things that would be relatively easy for a Python expert to debug but the point of following a tutorial was to get something that just runs and then build on it. If the tutorial doesn't run, I might as well just bang my head against a wall with my own code.

## 2023.12.28

### How the book data is structured in Goodreads

All the existing scraping scripts and the official CSV script seem to (mostly) take the data from the first book list, the "My Books" list. In my case, https://www.goodreads.com/review/list/704067?shelf=%23ALL%23

Then they also pull the generic book info, I think, that you would get from clicking the link in the "Title" field. So for the first book in my list, that would be: https://www.goodreads.com/book/show/35380408-the-unique-and-its-property

Somehow, the official CSV _does_ pull "My Review" which I don't think is found on that generic book info page. As far as I can tell, the review is in what I'd call the user-specific book detail page. It's weirdly difficult to get to that page even through the Goodreads GUI. 

"My Books" has the following column headers: cover, title, author, avg rating, rating, shelves, date read, date added 

At the end, there are two unlabelled columns. The first one has an "edit / view" link for each book. The last one has an X that presumably lets you delete a book. I'm not going to try it in case there's no confirmation dialogue. "Edit" takes you into a mode where you can add reviews, edit date read and so on. 

"View" takes you to the user-specific book detail page. Based on the breadcrumb, it might be the case that Goodreads attaches it to the user rather than the book. For example mine is

"Agnieszka's Reviews > The Spy Who Came in from the Cold"
https://www.goodreads.com/review/show/4964829801

(I'm switching to _The Spy Who Came in from the Cold_ as my example book because it has quotes, and a review.)

Of the things that aren't included in other views, that page includes
- Started reading
- Review
- Highlights (which is a link to my quotes and notes, maybe "annotations" for short) 
- Comments other people left on the book
- Comments I might have left attached to reading progress

If I want to see the higlights, I have to go to another page, named "My Kindle Notes & Highlights." That title makes me think that Goodreads might have structured the annotations as belonging to the user and then the user's Kindle, and then the book. 

https://www.goodreads.com/notes/19847968-the-spy-who-came-in-from-the-cold/704067-agnieszka?ref=rsp

The annotations can be marked as public or private. They can be marked as spoilers. They can also have comments. 

I wish I could see the data schema that Goodreads used rather than having to reverse-engineer it. It feels that it it's something like this:

Book: Universal book object with properties that any of that book would have like:
- title
- author
- isbn

User: The individual person who has shelves, reviews, and devices
- Shelves
    - Books
    - Actions that occurred to books
        - Dates the actions occured
        - Comments associated with actions
- Reviews
    - User-created text associated with books
    - Ratings associated with books
- Devices
    - Highlights associated with books
        - Comments associated with highlights
    - Notes associated with books

I'm sure this isn't quite right, and it's not necessarily the way _I_ want the data. It might be close_ish_ to the way that Bookwyrm structures the data.

I would really love a schema diagram of the Bookwyrm data. Everybody loves an Entity Relationship Diagram. I might make one when I work my way through the code.

## 2023.12.27

### Headers in the official export CSV

Book Id,Title,Author,Author l-f,Additional Authors,ISBN,ISBN13,My Rating,Average Rating,Publisher,Binding,Number of Pages,Year Published,Original Publication Year,Date Read,Date Added,Bookshelves,Bookshelves with positions,Exclusive Shelf,My Review,Spoiler,Private Notes,Read Count,Owned Copies

### How to scrape

[Web Scraping Popular Books on Goodreads using Python](https://medium.com/@nikhil-1e9/web-scraping-popular-books-on-goodreads-using-python-4f03b6e1b5a0)

[Scraping Goodreads: A Beginner’s Guide](https://medium.com/@adesua/scraping-goodreads-a-beginners-guide-3ad3a5907c2a)

### Bookwyrm code

Repo: https://github.com/bookwyrm-social

The book data schema is in two places, one the Django model and one in the ActivityPub section. I'm not sure how they fit together but it's probably a good place to look when thinking about how to structure the scraped data:

- bookwyrm/activitypub/book.py
- bookwyrm/models/book.py