# Running braindump

A reverse-chronological collection of notes, questions, references, plans, and pretty much everything else that comes up as I work on this project. 

## 2024.01.01

I should probably follow one of the existing scraper scripts and try to make it work before I go further down the data structure rabbit hole. 

I've decided to use [Scraping Goodreads: A Beginner’s Guide](https://medium.com/@adesua/scraping-goodreads-a-beginners-guide-3ad3a5907c2a).

### Install vs import

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

### Trying to install - friction log

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