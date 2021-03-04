
import unittest
from bs4 import BeautifulSoup
import KGB_review_scraper
import requests
import re
from review import Review

# Unit test for the functions used in KGB_review_scraper.py

testPages = [ # Testing each function with the first two pages of reviews 
'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page1/?filter=ALL_REVIEWS#link',
'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page2/?filter=ALL_REVIEWS#link' ]

class TestReviewScraper(unittest.TestCase):
	
	# GetReviewData test 
	def test_GetReviewData(self):
		KGB_review_scraper.GetReviewData(testPages)

	# GetReviews test
	def test_GetReviews(self):
		response = requests.get(testPages[0])
		soup = BeautifulSoup(response.text, 'html.parser')
		posts = soup.find_all(class_ = 'review-entry col-xs-12 text-left pad-none pad-top-lg border-bottom-teal-lt')
		KGB_review_scraper.GetReviews(posts)

	# NumOfStars tests
	def test_NumOfStars(self):
		response = requests.get(testPages[0])
		soup = BeautifulSoup(response.text, 'html.parser')
		post = soup.find(class_ = 'review-entry col-xs-12 text-left pad-none pad-top-lg border-bottom-teal-lt')

		KGB_review_scraper.NumOfStars(post)


if __name__ == '__main__':
	unittest.main()
