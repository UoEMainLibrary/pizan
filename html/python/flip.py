#!/usr/bin/python
# -*- coding: cp1252 -*-

# 12 Jun 08 flip.py to flip a string into reverse order so Baker becomes rekaB
# Accented characters must be saved as UTF-8 in Notepad before pasting-in
# Author Charlie Mansfield 12 June 2008


import sys, os, re

print "The Python script flip.py is running..."
print "The generosity of summer - string to flip: largeçe d'été"

flipped = ''

flipped = "largeçe d'été"[::-1]

print ""
print flipped
print ""
print "Run complete.  Thank you for using flip.py"
