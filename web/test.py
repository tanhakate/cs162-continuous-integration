import os
import unittest

import sys
from app import app, db


class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()

    # executed after each test
    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_add_valid(self):
        response = self.app.post(
          '/add',
          data = dict(text="1+1", value="1+1=2")
          follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        
    def test_add_invalid(self):
         response = self.app.post(
          '/add',
          data = dict(text="1+1", value="100+")
          follow_redirects=True
        )
         self.assertEqual(response.status_code, 400)
        
        
  if __name__ == '__main__':
    unittest.main()
