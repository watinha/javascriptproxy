import unittest

from css_replace_decorator import CSSReplaceDecorator 

class CSSReplaceDecoratorTest(unittest.TestCase):
  
  def test_single_decorate(self):
    html_mock_1 = "<html><head><link href='/teste_html.js'></head></html>"
    html_mock_2 = "<html><head><link rel=\"stylesheet\" href='teste_2html.js'></link><link rel=\"stylesheet\" href=\"css/teste.css\" type=\"text/css\" /></head><body><a href='teste.html'></body></html>"

    domain_mock = "www.watinha.com"

    html_result_mock_1 = "<html><head><link href='/teste_html.js'><style type=\"text/css\">/* teste_html.js */a{font-size:32px}</style></head></html>"
    html_result_mock_2 = "<html><head><link rel=\"stylesheet\" href='teste_2html.js'></link><link rel=\"stylesheet\" href=\"css/teste.css\" type=\"text/css\" /><style type=\"text/css\">/* teste_2html.js */a{font-size:32px}</style><style type=\"text/css\">/* css/teste.css */a{font-size:32px}</style></head><body><a href='teste.html'></body></html>"
    
    decorator = CSSReplaceDecorator(domain_mock)

    def html_extract_mock(text):
      return "a{font-size:32px}"

    decorator.get_css = html_extract_mock

    self.assertEquals(decorator.decorate(""), "")
    self.assertEquals(decorator.decorate(html_mock_1), html_result_mock_1)
    self.assertEquals(decorator.decorate(html_mock_2), html_result_mock_2)

    self.assertEquals(decorator.decorate_text(""), "")
    self.assertEquals(decorator.decorate_text(html_mock_1), html_result_mock_1)
    self.assertEquals(decorator.decorate_text(html_mock_2), html_result_mock_2)

  def test_import_statements(self):
    html_mock_1 = "<html><head><link href='/teste_html.js'></head></html>"
    html_result_mock_1 = "<html><head><link href='/teste_html.js'><style type=\"text/css\">/* teste_html.js */@import url(http://www.watinha.com/teste_html.js);a{font-size:32px}</style></head></html>"

    domain_mock = "www.watinha.com"

    decorator = CSSReplaceDecorator(domain_mock)
    
    def html_extract_mock(text):
      return "@import url(teste_html.js);a{font-size:32px}"

    decorator.get_css = html_extract_mock

    self.assertEquals(decorator.decorate(html_mock_1), html_result_mock_1)
    self.assertEquals(decorator.decorate_text(html_mock_1), html_result_mock_1)

    def html_extract_mock(text):
      return "@import 'teste_html.js';a{font-size:32px}"

    html_result_mock_1 = "<html><head><link href='/teste_html.js'><style type=\"text/css\">/* teste_html.js */@import 'http://www.watinha.com/teste_html.js';a{font-size:32px}</style></head></html>"

    decorator.get_css = html_extract_mock

    self.assertEquals(decorator.decorate(html_mock_1), html_result_mock_1)
    self.assertEquals(decorator.decorate_text(html_mock_1), html_result_mock_1)

  def test_url_statements_inside_css(self):
    html_mock_1 = "<html><head><link href='/teste_html.js'></head></html>"
    html_result_mock_1 = "<html><head><link href='/teste_html.js'><style type=\"text/css\">/* teste_html.js */@import url(http://www.watinha.com/teste_html.js);a{font-size:32px;background:url(http://www.watinha.com/../images/teste.png)};</style></head></html>"

    domain_mock = "www.watinha.com"

    decorator = CSSReplaceDecorator(domain_mock)
    
    def html_extract_mock(text):
      return "@import url(http://www.watinha.com/teste_html.js);a{font-size:32px;background:url(../images/teste.png)};"

    decorator.get_css = html_extract_mock

    self.assertEquals(decorator.decorate(html_mock_1), html_result_mock_1)
    self.assertEquals(decorator.decorate_text(html_mock_1), html_result_mock_1)

  def test_url_statements_inside_html(self):
    html_mock_1 = "<html><head><link href='/teste_html.js'></head><body style='background:url(/intl/en_com/images/srpr/logo1w.png)'> </body></html>"
    html_result_mock_1 = "<html><head><link href='/teste_html.js'><style type=\"text/css\">/* teste_html.js */@import url(http://www.watinha.com/teste_html.js);a{font-size:32px;background:url(http://www.watinha.com/../images/teste.png)};</style></head><body style='background:url(http://www.watinha.com/intl/en_com/images/srpr/logo1w.png)'> </body></html>"

    domain_mock = "www.watinha.com"

    decorator = CSSReplaceDecorator(domain_mock)
    
    def html_extract_mock(text):
      return "@import url(http://www.watinha.com/teste_html.js);a{font-size:32px;background:url(../images/teste.png)};"

    decorator.get_css = html_extract_mock

    self.assertEquals(decorator.decorate(html_mock_1), html_result_mock_1)
    self.assertEquals(decorator.decorate_text(html_mock_1), html_result_mock_1)

  def test_url_statement_variances_inside_html(self):
    html_mock_1 = "<html><head><link href='/teste_html.js'></head><body style='background:url(\"/intl/en_com/images/srpr/logo1w.png\")'> </body></html>"
    html_result_mock_1 = "<html><head><link href='/teste_html.js'><style type=\"text/css\">/* teste_html.js */@import url(http://www.watinha.com/teste_html.js);a{font-size:32px;background:url(http://www.watinha.com/../images/teste.png)};</style></head><body style='background:url(\"http://www.watinha.com/intl/en_com/images/srpr/logo1w.png\")'> </body></html>"

    domain_mock = "www.watinha.com"

    decorator = CSSReplaceDecorator(domain_mock)
    
    def html_extract_mock(text):
      return "@import url(http://www.watinha.com/teste_html.js);a{font-size:32px;background:url(../images/teste.png)};"

    decorator.get_css = html_extract_mock

    self.assertEquals(decorator.decorate(html_mock_1), html_result_mock_1)
    self.assertEquals(decorator.decorate_text(html_mock_1), html_result_mock_1)
    
