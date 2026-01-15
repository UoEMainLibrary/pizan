#!/usr/bin/python
# -*- coding: cp1252 -*-

# undash.py Python Script to remove hyphens from Laidlaw-encoded UTF-8 text
# 11-Apr-07 Mansfield added end lines to close files
print "Did you? - Save As t.txt as UTF-8 "
import sys, os, re
import codecs
filename = "t.txt"

if not os.path.exists(filename):
    print "Error:  File '%s' does not exist" % filename
    print "Usage:  %s <filename>" % sys.argv[0]
    sys.exit()

inh = codecs.open(filename, 'r', 'utf8')
outh = codecs.open("%s.joined.txt" % filename, 'w', 'utf8')

print "Removes hyphens from file t.txt"

splitWordRe = re.compile("-$")

line = inh.readline() 
kept = []
comments = []
while line:
    line = line[:-1]
    if kept and line:
        # Check for [] () or empty
        if line[0] in ['[', '(']:
            kept.append(line)
        elif line == "":
            kept.append(line)
        else:
            words = line.split(' ')
            kept[0] += words[0]
            line = ' '.join(words[1:])
            for k in kept:
                outh.write(k + "\n")
            kept = []
    # Strip trailing comments
    line = line.strip()    
    comment = ""

    if line and line[-1] == ")":
        idx = line.rfind("(")
        comment = line[idx:]
        line = line[:idx]
        line = line.strip()    
    elif line and line[-1:] == u"\xa3":
        line = line[:-1].strip()
        comment = u"\xa3"
    elif line and line[-1:] == "#":
        line = line[:-1].strip()
        comment = "#"
    m = splitWordRe.search(line)
    if m:
        nline = line[:m.start()]
        nline = nline.strip()
        kept.append(nline)
        comments.append(comment)
    elif not kept:
        outh.write(line + comment + "\n")
    line = inh.readline()

inh.close()
outh.close()

print "Done."





