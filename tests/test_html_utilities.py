import unittest
import html_utilities

class HtmlUtilitiesTest(unittest.TestCase):
  def test_html_extractor(self):
    """Testing the HTMLExtractor function wether it gets the URL HTML page"""
    test_url = "http://www.google.com"
    self.assertEquals(html_utilities.html_extractor(""), "")
    response = html_utilities.html_extractor(test_url)
    self.assertTrue(len(response) > 3)
    self.assertEquals(response[0:4], "<!do")

  def test_attribute_exception(self):
    test_url = "http://www.watinha.com"
    self.assertEquals(html_utilities.html_extractor(""), "")
    response = html_utilities.html_extractor(test_url)
    self.assertTrue(len(response) > 3)

  def test_url_parse(self):
    """Testing the url_parse function"""
    test_url = "http://www.google.com"
    test_url2 = "http://www.google.com/teste"
    self.assertEquals(html_utilities.parse_url(""), ["", ""])
    self.assertEquals(html_utilities.parse_url(test_url), ["www.google.com", ""])
    self.assertEquals(html_utilities.parse_url(test_url2), ["www.google.com", "/teste"])

  def test_encoding_issues(self):
    test_url = "http://www.uol.com"

    self.assertTrue(len(html_utilities.html_extractor(test_url)) > 15)

