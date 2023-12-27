# Running braindump

A reverse-chronological collection of notes, questions, references, plans, and pretty much everything else that comes up as I work on this project.

## 2023.12.27

### How to scrape

[Web Scraping Popular Books on Goodreads using Python](https://medium.com/@nikhil-1e9/web-scraping-popular-books-on-goodreads-using-python-4f03b6e1b5a0)

[Scraping Goodreads: A Beginner’s Guide](https://medium.com/@adesua/scraping-goodreads-a-beginners-guide-3ad3a5907c2a)

### Bookwyrm code

Repo: https://github.com/bookwyrm-social

The book data schema is in two places, one the Django model and one in the ActivityPub section. I'm not sure how they fit together but it's probably a good place to look when thinking about how to structure the scraped data:

- bookwyrm/activitypub/book.py
- bookwyrm/models/book.py