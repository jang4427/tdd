from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
    	self.browser = webdriver.Firefox()
    
    def tearDown(self):
    	self.browser.quit()
    
    def test1ddd(self):
    	assert 0
    	self.browser.get('http://localhost:8000')
    	self.assertIn('To-Do', self.browser.title)
    	self.fail('Finish the Test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
