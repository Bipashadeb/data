import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.pathdirname(__file__),'../src')))

from src.outfit_recommender import recommender_outfit

class TestOutfitRecommender(unittest.TestCase):
    def test_recommend_outfit(self):

        self.assertEqual(recommender_outfit(30, 'sunny'),"T-shirt and shorts")
        self.assertEqual(recommender_outfit(20, 'cloudy'),"Light jacket and jeans")
        self.assertEqual(recommender_outfit(10, 'rainy'),"Sweater and pants")
        self.assertEqual(recommender_outfit(0, 'snowy'),"Heavy coat, gloves, and scarf")

if __name__ == '__main__':
    unittest.main()
        