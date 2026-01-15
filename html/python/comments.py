#!/usr/bin/python
# -*- coding: cp1252 -*-

# 17 Mar 08 plus and tilde REMmed out with hashes
# 25 Feb 2008 converts MINn to <figure place="n"> and increments line count Charlie Mansfield
# 25 Jan 2008 Pilcrow converted to &#xb6; and notes tag made singular <note>
# hi rend substituted for rubric ink and dropcap
# 01 Jun 2007 comments,py - converts (notes) into XML tagged lines
# Modified by Charlie Mansfield 01-Jun-07 to make real xml tags from <>
# Script to generate XML file from text marked with Laidlaw Rules of Encoding Middle French
# <...> maintained as genuine xml tags
# BLn ==> n blank lines
# MINn ==> miniature spanning n lines
# PM ==> pilcrow or paragraph mark &#xb6;
# xn ==> Capital x spanning n lines now uses <hi rend="capn">
# & ==> contraction
#  ==> rhyme word (divide sign)
# |...| ==> abbreviation pipes
# $...£ dollar opens pound closes ==> rubric ink
# %...# ==> proper names
# [...] ==> folio number
# (...) ==> comments
# + ... ~ ==> supplied punctuation for scholarly edition. un ajout
# @...@ ==> acronyms eg AUBA
# {...} curly braces around intentional medieval superscripts eg ij{o}. ordinal
# « ... » les guillemets ouvrants et les guillemets fermants converted to <add place="supralinear">bien</add> where added above the line;

import sys, os, re

print "Generates XML file from a text file marked-up according to Laidlaw Rules"
print "t.txt gives t.txt.xml"
print "The Python script is running..."

filename = "t.txt"

if not os.path.exists(filename):
    print "Error:  File '%s' does not exist" % filename
    print "Usage:  %s <filename>" % sys.argv[0]
    sys.exit()

inh = file(filename)
outh = file("%s.xml" % filename, 'w')

preLine = ''
preFolio = ''
acro = '@'
min = 'MIN'
acronym='xxxx'
letter = ''
currFolio = 0
currColumn = 0
currLine = 0
hashcount = 0
percentcount = 0
dollarcount = 0
poundcount = 0
previouspercentline = ''
lasttime = ''
onebefore = ''
previousdollarline = ''

minRe = re.compile("^\s*MIN(\d+)\s*$")
acroLineRe = re.compile("\@(.*?)\@")
commentLineRe = re.compile("^\s*\(([^)]+)\)\s*$") 
folioLineRe = re.compile("^\s*\[(\d+)(.)\]\s*$")
blankRe = re.compile("^\s*BL(\d+)\s*$")
initialRe = re.compile("^\s*([A-Z])(\d+)")
abbrRe = re.compile("\|(.*?)\|")
def abbrFn(m):
    return '<abbr expan="%s"/>' % m.group(1)


line = inh.readline()
while line:

    m = acroLineRe.match(line)
    if m:
        acronym = line.replace("@", "")
        acronym = acronym.replace("\n", "")
        acronym = acronym + "."
        print acronym
        line = inh.readline()
        continue

    m = commentLineRe.match(line)
    if m:
        outh.write("<!-- %s -->\n" % m.groups(1))
        line = inh.readline()
        continue

    m = folioLineRe.match(line)
    if m:
        num = m.group(1)
        letter = m.group(2)
        extra = ""

        colidx = " abcd".find(letter)
        if colidx > 0:
            currColumn = colidx
            tagType = 'cb'
            num = letter
            outh.write("\n")
            if letter in ['a', 'b', 'c', 'd']:
                currLine = 0
        elif letter in ['r', 'v', 'a', 'b', 'c', 'd']:
            currLine = 0
            tagType = 'pb'
            extra = ' side="%s"' % letter
            if letter == 'r':
                currFolio = int(num)
            outh.write("\n\n")
        else:
            print "Unknown line type: %s" % letter
        outh.write('<%s n="%s"%s/>\n' % (tagType, num, extra))
        line = inh.readline()
        continue

    m = blankRe.match(line)
    if m:
        num = int(m.group(1))
        outh.write("<!-- %s blank line(s) here -->\n" % num)
        currLine += num
        line = inh.readline()
        continue

    m = minRe.match(line)
    if m:
        num = int(m.group(1))
        outh.write('<figure place="%s"></figure>' % num)
        outh.write("<!-- miniature extends %s lines here -->\n" % num)
        currLine += num
        line = inh.readline()
        continue

    # Now process actual lines
 
    # Initials can only appear at beginning of line
    m = initialRe.match(line)
    if m:
        outline= '<hi rend="cap%s">%s</hi>' % (m.group(2), m.group(1))
        line = line[m.end():]
    else:
        outline = ""

    # process out & so we can put in xml
    line = line.replace('«', '<add place="supralinear" type="" evidence="">')
    line = line.replace("»", "</add>")
    line = line.replace("&", '&amp;')
    line = line.replace("<div2>", '<div2 n="" type="" met="" rhyme="">')

    # Make bracketed comments into TAGs
    line = line.replace('(', '<note>')
    line = line.replace(')', '</note>')

    # singles
    line = line.replace("\xc3\xb7", "<rhyme/>")
    line = line.replace("PM ", "¶ ")

    # begin/end names and rubrics
    if line.find('%') > -1:
        percentcount += 1
        onebefore = lasttime + ''
        lasttime = previouspercentline + ''
        previouspercentline = line + ''

    if line.rfind('%') <> line.find('%') and line.find('#') < 0:
        print "Two percents BUT NO HASH found in same line here"
        print line
    
    if line.find('#') > -1:
        hashcount += 1

    if percentcount > hashcount + 2:
	print 'Name-opening percents outnumber closing hashes by 3.  Percents ='
	print percentcount, hashcount
	print line
	print 'Previous line containing percent was '
	print lasttime
	print ' ... and the one before was '
	print onebefore
	hashcount = 0
	percentcount = 0

    if line.find('$') > -1:
        dollarcount += 1

    if line.rfind('$') <> line.find('$'):
        print "Two rubric-opening DOLLARS found in same line here"
        print line

    if line.find('£') > -1:
        poundcount += 1

    if dollarcount > poundcount + 1:
        print 'Rubric-opening dollar count is greater than closing pound'
	print dollarcount, poundcount
	print line
	dollarcount = 0
	poundcount = 0

    line = line.replace("{", '<num type="ordinal">')
    line = line.replace("}", "</num>")    
    line = line.replace("%", '<name ref="">')
    line = line.replace("#", "</name>")
    line = line.replace("$", '<hi rend="red">')
    line = line.replace("£", "</hi>")
    line = line.replace("•", "&#x95;")
    line = line.replace("·", "&#xb7;")
    # Bullet "•", &#x95;
    # Middle Dot, Georgian Comma "·", &#xb7;

    line = line.replace("\x2192", "&#x2192;")
    # Rightwards Arrow (see above^) 
    line = line.replace("\x2190", "&#x2190;")
    # above Leftwards Arrow is converted to a hexadecimal entity

#   line = line.replace("+", '<supplied>')
#   line = line.replace("~", "</supplied>")

    # Abbreviations |...|
    # assume nothing else within abbrs
    if line.find('|') > -1:
        line = abbrRe.sub(abbrFn, line)

    currLine += 1
    if currLine < 10:
        preLine = preLine + '0'

    if currFolio < 10:
        preFolio = preFolio + '0'

    if currFolio < 100:
        preFolio = preFolio + '0'
    
    outh.write(('<lb n="%s%s%s%s:%s%s"/>' % (acronym, preFolio, currFolio, letter, preLine, currLine) + outline + line))
    outh.flush()
    preLine = ''
    preFolio = ''
    line = inh.readline()

                 
inh.close()
outh.close()

print "Done"
