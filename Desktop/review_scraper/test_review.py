
import unittest
from review import Review


# This is the unit test for the review class.
# - Creates 2 test review obects with the following reviews
# - Tests the levelOfPositivity() function to verify it outputs the correct positiveScore

# testReviewOne has 3 words that are in the positiveWords list in the review class
testReviewOne = """ 
McKaig is the best car and truck dealer I have ever dealt with, 
because of their no-nonsense deals and trades and the most friendly 
service dept. I have seen. Service is always prompt and loaners are 
available when needed to run errands! We have switched from imports 
to Chevrolets primarily because of McKaig.
""" 

# testReviewTwo has 1 word from the positiveWords list
testReviewTwo = """
We have been patronizing McKaig Chevrolet for nearly 40 years. We 
bought a few vehicles from other dealerships, but ALWAYS come back 
to McKaig Chevrolet. Their overall service is above all others. 
They are outstanding in all departments. We rely on them for all 
our vehicle needs, and they go above and beyond to take care of us.
""" 

class TestReview(unittest.TestCase):

	def setUp(self):
		self.review_1 = Review('Review One', testReviewOne, 50)
		self.review_2 = Review('Review Two', testReviewTwo, 42)

	def test_levelOfPositivity(self):
		
		self.review_1.levelOfPositivity()
		self.review_2.levelOfPositivity()
		self.assertEqual(self.review_1.positiveScore, 103)
		self.assertEqual(self.review_2.positiveScore, 64)

# After running the levelOfPositivity() function, the positiveScore should be 
# 103 for the first review (3 + (50 * 2))
# 64 for the second review (1 + (42 * 1.5))

if __name__ == '__main__':
	unittest.main()