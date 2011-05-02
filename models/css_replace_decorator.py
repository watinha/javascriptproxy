#
# Decorator class that replaces the link CSS elements with href attributes with inline elements
#

import re
from js_replace_decorator import JsReplaceDecorator
from html_utilities import html_extractor

"""
Decorator class CSSReplaceDecorator
"""
class CSSReplaceDecorator(JsReplaceDecorator):
 
  def get_css(self, url):
    return html_extractor(url)

  def decorate(self, text):
    
    if (text == ""):
      return ""
    
    # re.search("link\s+((\w)+=('|\")(\w|\.|/)*('|\"))*\s*href\s*=\s*('|\")((\w|\.|/)+)('|\")", test)
    search_string = text
    result = ""
    inline_styles = ""
    while True:
      try:
        match = re.search("link\s+((\w)+=('|\")(\w|\.|/)*('|\"))*\s*href\s*=\s*('|\")((\w|\.|/|\-)+)('|\")", search_string)
        css_file = match.group(7) # teste.css

        if (css_file[0:4] != "http"):
          new_css_file = css_file

          if (css_file[0] == "/"):
            new_css_file = css_file[1:]
          
          css_get = self.get_css("http://" + self.domain + "/" + new_css_file)
          css_get = self.replace_url(css_get)
          inline_styles += "<style type=\"text/css\">/* " + new_css_file + " */" + css_get + "</style>"
        
        result += search_string[:match.end()]
        search_string = search_string[match.end():]
      except AttributeError:
        result += search_string
        result = self.replace_url(result)
        result = result.replace("</head>", (inline_styles + "</head>"))
        return result

    return ""
  
  def replace_url(self, css_code):
    
    if (css_code == ""):
      return ""
    
    search_string = css_code 
    result = ""
    while True:
      try:
        match = re.search("(url|import)\s*(\(|\'|\"|\(\'|\(\")((\w|\.|/|\-)+)(\'|\"|\)|\'\)|\"\))", search_string)
        css_file = match.group(3)
        if (css_file[0:4] != "http"):
          new_css_file = css_file
          if (css_file[0] == "/"):
            new_css_file = css_file[1:]
          search_string = search_string.replace(css_file, ("http://" + self.domain + "/" + new_css_file))
        result += search_string[:match.end()]
        search_string = search_string[match.end():]
      except AttributeError:
        return result + search_string

    return ""
