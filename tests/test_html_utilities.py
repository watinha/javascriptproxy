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
    response = html_utilities.html_extractor(test_url)
    self.assertTrue(len(response) > 15)

  def test_get_encoding_utf8(self):
    test_content_type_1 = "text/html; charset=ISO-8859-1"
    test_content_1 = "<html><body>Text in html content</body></html>"
    test_content_type_2 = "text/html"
    test_content_2 = "<html><meta content='text/html; charset=UTF-8'></html>"
    test_content_type_3 = "text/html; charset=UTF-8"
    test_content_3 = "<html><meta content='text/html; charset=UTF-8'></html>"

    test_content_type_4 = "text/html;"
    test_content_4 = "<html><meta content='text/html; charset=ISO-8859-1'></html>"

    test_content_type_5 = "text/html;"
    test_content_5 = "<html><meta content='text/html; charset=ISO-8859-1'></html>"

    self.assertEquals("ISO-8859-1", html_utilities.get_encoding(test_content_type_1, test_content_1))
    self.assertEquals("UTF-8", html_utilities.get_encoding(test_content_type_2, test_content_2))
    self.assertEquals("UTF-8", html_utilities.get_encoding(test_content_type_3, test_content_3))
    self.assertEquals("ISO-8859-1", html_utilities.get_encoding(test_content_type_4, test_content_4))
    self.assertEquals("ISO-8859-1", html_utilities.get_encoding(test_content_type_5, test_content_5))
