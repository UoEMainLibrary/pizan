#!/usr/bin/python
# -*- coding: cp1252 -*-

# 21-Aug-06 correctrice - to provide better pointers to unclosed name # and rubric Charlie Mansfield
# Script to generate XML file from text marked with Laidlaw Rules of Encoding Middle French
# BLn ==> n blank lines
# MINn ==> miniature spanning n lines
# PM ==> paragraph mark &#xb6;
# xn ==> Capital x spanning n lines
# & ==> contraction
#  ==> rhyme word (divide sign)
# |...| ==> abbreviation pipes
# <...> ==> superscript
# $...£ dollar opens pound closes ==> rubric ink
# %...# ==> proper names
# [...] ==> folio number
# (...) ==> comments
# + ... ~ ==> supplied punctuation for scholarly edition. un ajout 

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

commentLineRe = re.compile("^\s*\(([^)]+)\)\s*$") 
folioLineRe = re.compile("^\s*\[(\d+)(.)\]\s*$")
blankRe = re.compile("^\s*BL(\d+)\s*$")
initialRe = re.compile("^\s*([A-Z])(\d+)")
abbrRe = re.compile("\|(.*?)\|")
def abbrFn(m):
    return '<abbr expan="%s"/>' % m.group(1)


line = inh.readline()
while line:
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

    # Now process actual lines
    # First strip out comments
    commIdx = line.find('(')
    while commIdx > -1:
        # Find end, check for nesting
        endIdx = line.find(')')
        if endIdx == -1:
            # make entire line comment
            print "Warning: Line with no closing ')'"
            print line
            print "currFolio '%s' " % currFolio
            print "currLine '%s' " % currLine
            line = line[:commIdx]
        elif endIdx < commIdx:
            print "WARNING: Broken comment line:"
            print line
            print "currFolio '%s' " % currFolio
            print "currLine '%s' " % currLine
            print "letter '%s' " % letter
            break
        else:
            comm = line[commIdx:endIdx+1]
            line = line[:commIdx] + line[endIdx+1:]
            nest = comm.count('(') - comm.count(')')
            for x in range(nest):
                # consume further close comment delims
                endIdx = line.find(')')
                line = line[:commIdx] + line[endIdx:]
        commIdx = line.find('(')

    # Initials can only appear at beginning of line
    m = initialRe.match(line)
    if m:
        outline= '<initial extent="%s">%s</initial>' % (m.group(2), m.group(1))
        line = line[m.end():]
    else:
        outline = ""

    # process out & <> so we can put in xml
    line = line.replace("<", "<superscript*")
    line = line.replace(">", "</superscript>")
    line = line.replace("<superscript*", "<superscript>")
    line = line.replace("&", '&amp;')

    # singles
    line = line.replace("\xc3\xb7", "<rhyme/>")
    line = line.replace("PM ", "<para/>")

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

    if percentcount > hashcount + 1:
	print 'Name-opening percents outnumber closing hashes by 2.  Percents ='
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
    
    line = line.replace("%", "<name>")
    line = line.replace("#", "</name>")
    line = line.replace("$", '<ink type="red">')
    line = line.replace("£", "</ink>")
    line = line.replace("+", '<supplied>')
    line = line.replace("~", "</supplied>")
    line = line.replace("•", "&#x95;")
    line = line.replace("·", "&#xb7;")
    # Bullet "•", &#x95;
    # Middle Dot, Georgian Comma "·", &#xb7;

    line = line.replace("\x2192", "&#x2192;")
    # Rightwards Arrow (see above^) 
    line = line.replace("\x2190", "&#x2190;")
    # above Leftwards Arrow is converted to a hexadecimal entity

    # Abbreviations |...|
    # assume nothing else within abbrs
    if line.find('|') > -1:
        line = abbrRe.sub(abbrFn, line)

    currLine += 1
    outh.write(('<lb n="%s%s:%s"/>&#x9;&#x20;&#x20;' % (currFolio, letter, currLine) + outline + line))
    outh.flush()
    line = inh.readline()

                 
inh.close()
outh.close()

print "Done"
