#
# Functions group that deals with HTTP requests
#

"""
Function responsible for acquiring the HTML code for an specific webpage
"""

import httplib
import re

def html_extractor(url):
  """ Recursion function that follows HTTP moved out wepages """  

  [domain, url_add] = parse_url(url)
  if (domain == ""):
    return ""

  conn = httplib.HTTPConnection(domain)
  conn.request("GET", url_add)
  response = conn.getresponse()
  content = response.read()

  headers = response.getheaders()
  content_type = filter (lambda x: x[0] == 'content-type', headers)
  try: 
    re_match = re.search("charset=((.)+)", content_type[0][1])
    encoding = re_match.group(1)
  except AttributeError, IndexError:
    try:
      re_match = re.search("charset=((.)+)", content)
      encoding = re_match.group(1)
    except AttributeError:
      # tries defalt encoding
      encoding = "ISO-8859-1"

  if (response.status == 302 or response.status == 303 or response.status == 301):
    location = filter (lambda x: x[0] == 'location', headers)
    try:
      return html_extractor(location[0][1])
    except:
      try:
        re_match = re.search("<A HREF=(\"|')((.)+)('|\")>", content)
        new_url = re_match.group(2)
        return html_extractor(new_url)
      except AttributeError:
        return content

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
