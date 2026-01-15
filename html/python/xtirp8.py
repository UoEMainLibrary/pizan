#!/usr/bin/python
# -*- coding: cp1252 -*-

# 05-Jun-06 xtirp8 Charlie Mansfield
# Script to convert accented characters to UTF-8 entities in hex for XHTML
# les appels de caractère numériques en hex pour les codages UTF-8 

import sys, os, re

print "Script to convert accented characters to UTF-8 entities in hex"
print "xtirp8 is running..."

filename = "t.txt"

if not os.path.exists(filename):
    print "Error:  File '%s' does not exist" % filename
    print "Usage:  %s <filename>" % sys.argv[0]
    sys.exit()

inh = file(filename)
outh = file("%s.htm" % filename, 'w')

letter = ''
currFolio = 0
currColumn = 0
currLine = 0
hashcount = 0
percentcount = 0
dollarcount = 0
poundcount = 0

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


    # Count Dollars and Hashes
    if line.find('#') > -1:
        hashcount += 1

    if line.find('%') > -1:
        percentcount += 1

    if hashcount > percentcount + 1:
	print hashcount, percentcount
	print line
	hashcount = 0
	percentcount = 0

    if line.find('$') > -1:
        dollarcount += 1

    if line.find('£') > -1:
        poundcount += 1

    if dollarcount > poundcount + 1:
	print dollarcount, poundcount
	print line
	dollarcount = 0
	poundcount = 0

# Currencies and Special Symbols to Hex UTF-8 
    line = line.replace("&", "&#x26;")	
    line = line.replace("%", "&#x25;")
    line = line.replace("#", "&#x23;")
    line = line.replace("$", "&#x24;")
    line = line.replace("£", "&#xa3;")
    line = line.replace("+", "&#x2b;")
    line = line.replace("~", "&#x7e;")
    line = line.replace("•", "&#x95;")
    line = line.replace("·", "&#xb7;")
    # Bullet "•", &#x95;
    # Middle Dot, Georgian Comma "·", &#xb7;
    line = line.replace("\xc3\xb7", "&#xf7;")


# The usual accented characters for Modern and Middle French
    line = line.replace("À", "&#xc0;")
    line = line.replace("Ç", "&#xc7;")
    line = line.replace("É", "&#xc9;")
    line = line.replace("Ö", "&#xd6;")
    line = line.replace("Ÿ", "&#x9f;")
    line = line.replace("à", "&#xe0;")
    line = line.replace("â", "&#xe2;")
    line = line.replace("ç", "&#xe7;")
    line = line.replace("è", "&#xe8;")
    line = line.replace("é", "&#xe9;")
    line = line.replace("ê", "&#xea;")
    line = line.replace("ë", "&#xeb;")
    line = line.replace("î", "&#xee;")
    line = line.replace("ï", "&#xef;")
    line = line.replace("ô", "&#xf4;")
    line = line.replace("ö", "&#xf6;")
    line = line.replace("ù", "&#xf9;")
    line = line.replace("û", "&#xfb;")
    line = line.replace("ÿ", "&#xff;")
    line = line.replace("œ", "&#x9c;")

    line = line.replace("ü", "&#xfc;")

# The older WORD6 renderings of French accents with REMark just before
    # ç c cedilla just below this REMark, which shows as &#x2021;
    line = line.replace("‡", "&#xe7;")
    # &#x201a;  é just below this REM
    line = line.replace("‚", "&#xe9;")
    
    # ï &#65533;
    line = line.replace("‹", "&#xef;")
    #  y diaeresis   une diérèse
    line = line.replace("˜", "&#xff;")
    #  a grave:
    line = line.replace("…", "&#xe0;")
    #  u diaeresis
    line = line.replace("\x81", "&#xfc;")
    #  e grave:
    line = line.replace("Š", "&#xe8;")
    #  u grave
    line = line.replace("—", "&#xf9;")
    #  e diaeresis
    line = line.replace("‰", "&#xeb;")

    currLine += 1
    outh.write(line)
    outh.flush()
    line = inh.readline()

                 
inh.close()
outh.close()

print "Done"
