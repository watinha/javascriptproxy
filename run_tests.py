#! /usr/bin/env python

#
# The run_tests.py file aims at running all tests that are supposed to be executed within the application
#   at first we import the base library paths and then we run the tests
#

import sys
import unittest

sys.path.append("models")
sys.path.append("handlers")
sys.path.append("tests")

from test_html_utilities import HtmlUtilitiesTest
from test_js_replace_decorator import JsReplaceDecoratorTest
from test_css_replace_decorator import CSSReplaceDecoratorTest

if __name__ == "__main__":
  unittest.main()

