
import re

# List of the common positive words/phrases used in reviews
positiveWords = [ 'happy', 'satisfied', 'nice', 'best', 'great', 'recommend', 'pleased', 'well',  
				  'thank you', 'wonderful', 'good', 'happier', 'helpful', 'thank', 'awesome',
				  'great deal', 'appreciate', 'enjoy', 'friendly', 'excellent', 'easy', 'outstanding', 
				  'fast', 'quick', '!', 'extremely', 'very friendly', 'knowledgeable', 'very helpful',
				  'reasonable', 'smile', 'pleasure', 'incredible', 'rocks', 'good service', 'gold star',
				  'five star', '5 star', 'genuine', 'personable', 'stellar', 'greatest', 'quality', 'amazing',
				  'quality service', 'top notch', 'extra mile', 'absolute best', 'fast and easy', 'love', 'perfect']

class Review():

	# Each review has a title, review, number of stars, and positive score
	# Positive score is calculated after running the levelOf Positivity function
	def __init__(self, title, review, numOfStars):
		self.title = title
		self.review = review
		self.numOfStars = numOfStars
		self.positiveScore = 0

	# Determines the level of positivity in the function based on:
	# - The number of positive words
	# - If they have any positive words in all caps
	# - Amount of stars 
	def levelOfPositivity(self):
		for word in positiveWords:
			if re.search(word, self.review, re.IGNORECASE):
				self.positiveScore += 1

			if re.search(word.upper(), self.review) and word != '!':
				self.positiveScore += 3

		# Adds the amount of stars to the positive score
		# If the customer left a five star review (numOfStars = 50),
		# the amount is multiplied by two to have a higher impact
		if self.numOfStars == 50:
			self.positiveScore += (self.numOfStars * 2)
			return
		elif self.numOfStars > 40:
			self.positiveScore += (self.numOfStars * 1.5)
			return
		else:
			self.positiveScore += self.numOfStars
			return


