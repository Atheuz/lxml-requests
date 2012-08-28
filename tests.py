# -*- coding: utf-8 -*-

# Filename      tests.py
# Author        Lasse Vang Gravesen <gravesenlasse@gmail.com>
# First edited  28-08-2012 01:57
# Last edited   28-08-2012 02:59

import unittest
from lxml_requests import *

class TestLxmlRequests(unittest.TestCase):

    def setUp(self):
        """Setup the objects."""
        self.html_site      = requests.html("https://www.google.dk/")
        self.xml_site       = requests.xml("http://apps.welpyourcall.com/files/example.xml")
        self.html_string    = requests.html_tostring(self.html_site)
        self.xml_string     = requests.xml_tostring(self.xml_site)

    def test_checkType(self):
        """Check that the objects are the correct type."""
        self.assertIsInstance(self.html_site, requests.lxml.html.HtmlElement)
        self.assertIsInstance(self.xml_site, requests.lxml.etree._Element)
        self.assertIsInstance(self.html_string, str)
        self.assertIsInstance(self.xml_string, str)

    def test_checkContent(self):
        """Check that the objects are not None or of length 0."""
        self.assertIsNotNone(self.html_site.xpath('//button/@aria-label'))
        self.assertIsNotNone(self.xml_site.xpath('//thread/@id'))
        self.assertTrue(len(self.html_string) > 0)
        self.assertTrue(len(self.xml_string) > 0)

    def test_convertFromString(self):
        """Convert from string to lxml object, and check it's of the correct type."""
        self.assertIsInstance(requests.html_fromstring(self.html_string), requests.lxml.html.HtmlElement)
        self.assertIsInstance(requests.xml_fromstring(self.xml_string), requests.lxml.etree._Element)

    def test_convertToString(self):
        self.assertIsInstance(requests.html_tostring(self.html_site), str)
        self.assertIsInstance(requests.xml_tostring(self.xml_site), str)

    def test_lxmlNamespace(self):
        """Check that the requests.lxml.* namespacing works."""
        self.assertIsNotNone(requests.lxml.html.fromstring(requests.get("https://www.google.dk/").text))
        self.assertIsNotNone(requests.lxml.etree.fromstring(requests.get("http://apps.welpyourcall.com/files/example.xml").text))

suite = unittest.TestLoader().loadTestsFromTestCase(TestLxmlRequests)
unittest.TextTestRunner(verbosity=3).run(suite)


#if __name__ == '__main__':
#    unittest.main()

