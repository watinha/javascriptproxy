#! /usr/bin/env python

#
# Main file that sets out the url patterns and its respective RequestHandler classes
# The main file also sets out the standard paths of the system
# - handlers folder: that contain all RequestHandlers classes
# - models folder: that contain all db.models classes
# - tests folder: that contain all tests classes
#

"""
 Setting all base paths for the application (handlers, models and tests folder) and configuring the base url patterns to its respective RequestHandler classes
"""

import sys
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

# setting the base paths
sys.path.append("handlers")
sys.path.append("models")
sys.path.append("libs")
sys.path.append("templates")

import cross_proxy

debug_state = True

def main():
  """Main function to be run as the application starts: sets the base path directories and the url patterns"""

  # setting the standard url configurations
  application = webapp.WSGIApplication([
                                         ('/', cross_proxy.CrossProxy),
                                       ], debug=debug_state)
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
