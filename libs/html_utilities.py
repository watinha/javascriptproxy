#
# Functions group that deals with HTTP requests
#

"""
Function responsible for acquiring the HTML code for an specific webpage
"""

import urllib2
import re

def html_extractor(url):
  """ Uses urllib2 to follow redirects """
  if (len(url) == 0):
    return ""

  request = urllib2.Request(url)
  opener = urllib2.build_opener()
  response = opener.open(request)

  content = response.read()

  encoding = get_encoding(response.headers["content-type"], content)

  return content.decode(encoding)

def parse_url(url):
  if(url == ""):
    return ["", ""]
  url_array = filter(lambda x: x[0:4] != "http" and x != "", url.split("/"))
  domain = url_array[0]

  if(len(url_array) == 1):
    url_add = ""
  else:
    url_add = "/" + reduce(lambda x, y: x + "/" + y, url_array[1:])
  return [domain, url_add]

def get_encoding(content_type, content):
  """ Accepts only UTF-8 and ISO-8859-1 """
  try:
    re_match = re.search("charset=((.)+)", content_type)
    encoding = re_match.group(1)
  except AttributeError, IndexError:
    try:
      re_match = re.search("charset=((.)+)(\'|\")", content)
      encoding = re_match.group(1)
    except AttributeError, IndexError:
      # tries defalt encoding
      encoding = "ISO-8859-1"

  return encoding
