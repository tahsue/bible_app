# KGB Review Scraper

## KGB Review Scraper is a tool that:
    1.  Scrapes the first five pages of reviews
    2.  Identifies the top three most “overly positive” endorsements
    3.  Outputs these three reviews to the console, in order of severity

In order to find the top three "overly positive" endorsements, the KGB Review Scraper 
scrapes the first five pages of reviews from DealerRater.com and gives each review
a score of how positive it was. 

The level of positivity is determined by picking out common positive words and phrases in each review. 
For each positive word found in the review, its level of positivity increased. If the program found a positive word in
all capital letters, it would have a greater effect on its level of positivity. Along with the positive words, 
the review scraper also determines the customer's review out of 5 stars. The number of stars is added
to the level of positivity.

After the level of positivity is determined, the function sorts the list of reviews in order of the level of positivity to
find the three most "overly positive" statements.

## Libraries Used:
- Beautiful Soup and Requests to scrape the reviews 

## Running the Code

Before running the code, verify that bs4 and requests are installed since they are the libraries used to scrpe the web pages
To run the code, find the folder in the file directory in the terminal and run the following command:
### Mac: 
python3 ./KGB_review_scraper.py
### Windows:
KGB_review_scraper.py

To run the test cases, run the following commands:
### Mac:
python3 ./test_KBG_review_scraper.py
python3 ./test_review.py
### Windows:
test_KBG_review_scraper.py
test_review.py
