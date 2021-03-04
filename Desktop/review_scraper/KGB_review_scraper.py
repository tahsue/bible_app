
import requests
from bs4 import BeautifulSoup
from review import Review
import re


# Gets the review data from the first five webpages, creating review objects for each review
# then each review object is stored in a list of review objects called listOfReviews. Used with
# the GetReviews(posts) function to get this data.
def GetReviewData(pages): 
	listOfReviews = []	
	for page in pages:		
		response = requests.get(page)
		if response.ok:
			soup = BeautifulSoup(response.text, 'html.parser')
			posts = soup.find_all(class_ = 'review-entry col-xs-12 text-left pad-none pad-top-lg border-bottom-teal-lt')
			listOfReviews += GetReviews(posts)
		else:
			return 'Bad response'
	listOfReviews.sort(key = lambda x: x.positiveScore, reverse = True)
	return listOfReviews

def GetReviews(posts):
	listOfReviews = []
	for post in posts:
		title = post.find(class_ = 'margin-bottom-sm line-height-150').get_text().replace('\n', '')
		review = post.find(class_ = 'font-16 review-content margin-bottom-none line-height-25').get_text().replace('\n','')
		numberOfStars = NumOfStars(post)
		listOfReviews.append(Review(title, review, numberOfStars))
		listOfReviews[-1].levelOfPositivity()
	return listOfReviews

# Gets the number of stars for each review. uses the library re to search for any class that 
# has the digits in the '\d\d' spot (this is where the rating will be). The returned value is
# between 00 and 50
def NumOfStars(post):
	pattern = re.compile(r'rating-static hidden-xs rating-\d\d margin-center')
	quality = post.find(class_ = pattern)
	return int(re.search(r'\d+', str(quality)).group())

# Prints out each positive review in the order of severity
def PrintPositiveReviews():
	print('TOP THREE POSITIVE ENDORSEMENTS:', '\n')
	for i in range(0, 3):
		print('REVIEW #', i + 1, ':')
		print(reviewList[i].review, '\n')

pages = [ # Stores the first five pages of reviews
'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page1/?filter=ALL_REVIEWS#link',
'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page2/?filter=ALL_REVIEWS#link',
'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page3/?filter=ALL_REVIEWS#link',
'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page4/?filter=ALL_REVIEWS#link',
'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page5/?filter=ALL_REVIEWS#link']

reviewList = GetReviewData(pages)

PrintPositiveReviews()

