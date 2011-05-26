#
# Decorator class that replaces the script elements with src attributes with script inline elements
#

import re

"""
Decorator class JsReplaceDecorator
"""
class JsReplaceDecorator():

  def __init__(self, domain, other_decorator = ""):
    self.other_decorator = other_decorator
    self.domain = domain

  def decorate_text(self, text):
    decorated_text = text

    if (self.other_decorator != ""):
      decorated_text = self.other_decorator.decorate(text)

    return self.decorate(decorated_text)

  def decorate(self, text):

    if (text == ""):
      return ""

    #re.search("src\s*=\s*('|\")((\w|\.|/)+)('|\")", b) for recovering src="javsacript.js"
    search_string = text
    result = ""
    while True:
      try:
        match = re.search("src\s*=\s*('|\")((\w|\.|/|\-)+)('|\")", search_string)
        js_file = match.group(2)
        if (js_file[0:4] != "http"):
          new_js_file = js_file
          if (js_file[0] == "/"):
            new_js_file = js_file[1:]
          search_string = search_string.replace(js_file, ("http://" + self.domain + "/" + new_js_file))
        result += search_string[:match.end()]
        search_string = search_string[match.end():]
      except AttributeError:
        return result + search_string

    return ""
