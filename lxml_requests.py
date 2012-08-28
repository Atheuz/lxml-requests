# -*- coding: utf-8 -*-

# Filename      lxml_requests.py
# Author        Lasse Vang Gravesen <gravesenlasse@gmail.com>
# First edited  28-08-2012 01:30
# Last edited   28-08-2012 03:38

import lxml.html, lxml.etree
import requests

# HTML
def html(url):
    return lxml.html.fromstring(requests.get(url).text)

def html_tostring(html):
    return lxml.html.tostring(html, pretty_print=True)

def html_fromstring(s):
    return lxml.html.fromstring(s)

# XML
def xml(url):
    return lxml.etree.fromstring(requests.get(url).text)

def xml_tostring(xml):
    return lxml.etree.tostring(xml, pretty_print=True)

def xml_fromstring(s):
    return lxml.etree.fromstring(s)

requests.html = html
requests.html_tostring = html_tostring
requests.html_fromstring = html_fromstring
requests.xml = xml
requests.xml_tostring = xml_tostring
requests.xml_fromstring = xml_fromstring
requests.lxml = lxml
requests.lxml.html = lxml.html
requests.lxml.etree = lxml.etree
