#
# RequestHandler that acts as a cross domain proxy for web applications
#   - gets the html code for the web applications
#   - replaces the relative URI paths with absolute URI paths
#   - include the Javascript and CSS code in the web application
#

"""
RequestHandler that implements the cross-domain proxy design pattern
"""

from google.appengine.ext import webapp

from html_utilities import html_extractor, parse_url
from js_replace_decorator import JsReplaceDecorator
from css_replace_decorator import CSSReplaceDecorator


class CrossProxy(webapp.RequestHandler):
  def get(self):
    """
    Receives the GET request with a URI parameter
    """
    parameter = self.request.get('url')
    domain = parse_url(parameter)[0]

    # Including the base javascript for replacing the relative URLs
    response = html_extractor (parameter)

    # Adding the decorators functions
    text_decorator = JsReplaceDecorator(domain, CSSReplaceDecorator(domain))

    #script_text = "<script type='text/javascript' src='/javascripts/replacing_urls.js'></script>"
    #response = response[0:response.find("</head>")] + script_text + response[response.find("</head>"):]

    self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
    self.response.out.write(text_decorator.decorate_text(response))
