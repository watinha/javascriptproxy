import unittest

from js_replace_decorator import JsReplaceDecorator

class JsReplaceDecoratorTest(unittest.TestCase):
  
  def test_single_decorate(self):
    html_mock_1 = "<html><head><script src='/teste_html.js'></head></html>"
    html_mock_2 = "<html><head><script src='teste_2html.js'></script><script src=\"teste.js\"></head></html>"

    domain_mock = "www.watinha.com"

    html_result_mock_1 = "<html><head><script src='http://www.watinha.com/teste_html.js'></head></html>"
    html_result_mock_2 = "<html><head><script src='http://www.watinha.com/teste_2html.js'></script><script src=\"http://www.watinha.com/teste.js\"></head></html>"
    
    decorator = JsReplaceDecorator(domain_mock)

    self.assertEquals(decorator.decorate(""), "")
    self.assertEquals(decorator.decorate(html_mock_1), html_result_mock_1)
    self.assertEquals(decorator.decorate(html_mock_2), html_result_mock_2)

    self.assertEquals(decorator.decorate_text(""), "")
    self.assertEquals(decorator.decorate_text(html_mock_1), html_result_mock_1)
    self.assertEquals(decorator.decorate_text(html_mock_2), html_result_mock_2)

