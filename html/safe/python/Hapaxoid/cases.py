# -*- coding=utf-8

'''
This module provides two functions for use by the other parts of the
Hapaxoid application, allowing conversion between cases for both
ordinary and special characters.

Hapaxoid was written by Tommy Herbert for Charlie Mansfield and Jim
Laidlaw.  Please see readme.txt for an overview.

Version 1.0
15th August 2008
'''

# The text file Hapaxoid uses for the Queen's Manuscript is in
# UTF-16.  Here are the special characters.
casePairs = [('\xc1', '\xe1'), # Á á
             ('\xc0', '\xe0'), # À à
             ('\xc2', '\xe2'), # Â â
             ('\xc4', '\xe4'), # Ä ä
             ('\xc3', '\xe3'), # Ã ã
             ('\xc5', '\xe5'), # Å å
             ('\xc9', '\xe9'), # É é
             ('\xc8', '\xe8'), # È è
             ('\xca', '\xea'), # Ê ê
             ('\xcb', '\xeb'), # Ë ë
             ('\xcd', '\xed'), # Í í
             ('\xcc', '\xec'), # Ì ì
             ('\xce', '\xee'), # Î î
             ('\xcf', '\xef'), # Ï ï
             ('\xd3', '\xf3'), # Ó ó
             ('\xd2', '\xf2'), # Ò ò
             ('\xd4', '\xf4'), # Ô ô
             ('\xd6', '\xf6'), # Ö ö
             ('\xd5', '\xf5'), # Õ õ
             ('\xda', '\xfa'), # Ú ú
             ('\xd9', '\xf9'), # Ù ù
             ('\xdb', '\xfb'), # Û û
             ('\xdc', '\xfc'), # Ü ü
             ('\xdd', '\xfd'), # Ý ý
             ('\x178', '\xff'), # Ÿ ÿ
             ('\x9f', '\xff'), # Ÿ ÿ
             ('\xc7', '\xe7'), # Ç ç
             ('\xd1', '\xf1')] # Ñ ñ

# This code is run when the module is imported.  It builds two
# dictionaries which are used by the functions below.
upperToLower = {}
lowerToUpper = {}
for (u, l) in casePairs:
   upperToLower[u] = l
   lowerToUpper[l] = u

def myUpper(character):
   '''Converts a character to upper case.  The name distinguishes it
   from the String class's function upper().'''
   if lowerToUpper.has_key(character):
      return lowerToUpper[character]
   else:
      return character.upper()

def myLower(character):
   '''Converts a character to lower case.  The name distinguishes it
   from the String class's function lower().'''
   if upperToLower.has_key(character):
      return upperToLower[character]
   else:
      return character.lower()
