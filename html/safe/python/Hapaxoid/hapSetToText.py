# -*- coding=utf-8

'''
This script is part of Hapaxoid, written by Tommy Herbert for Charlie
Mansfield and Jim Laidlaw.  Please see readme.txt for an overview.

Version 1.0
15th August 2008

---------------------------------------------------------------------

The instructions below are for processing a file that has been output
by the findHapSets.py script.  See that script for details on how to
produce such a file.

Assuming you've run findHapSets.py with the outputFilename parameter
set to 'output/example', there should be two files in the 'output'
directory called example.txt and example.pkl respectively.  Let's say
you open example.txt and find that line 1087 looks like this:

doulour (57): doulçour (36), douloir (22), douleur (121), doulceur (40)

Now, let's say you're interested in the relationship between
'doulour', 'douloir' and 'douleur' (don't laugh - I haven't got the
first clue about this language).  You'd set the parameters below to
produce a list of the pages where those three words appear, like
this:

Set inputFilename to 'output/example' (or 'output/example.txt'
or 'output/example.pkl' - it comes to the same thing).

Set hapSetID to 'doulour' or '1087' (recall that it's line number
1087).

Set the 'unwanted' parameter to [2, 5], since 'doulçour' and
'doulceur' are the second and fifth words on line 1087 and you want
to exclude them from the analysis.  Alternatively, you could specify
the unwanted words by name, but this is a little difficult when
there's a ç in one of them: ['doul\xe7our', 'doulceur'].

Set the outputFilename parameter to a name that isn't in use for an
existing file - like 'output/doulour'.  Note that Hapaxoid will
automatically append the extension '.txt'.

Then you'd run the script and a new text file would be created giving
all the citations for the words you've chosen to focus on.  You can
open the text file and examine the page numbers.  If you decide you
want a graphical representation of the same information, see the
script hapSetToGraph.py.
'''

inputFilename = 'output/hapSets.pkl' # The name of the data file output
                                 # by the findHapSets.py script,
                                 # which acts as input here.

hapSetID = 'abile' # The first word of the hapaxoid-set you want to
                     # investigate (you could also enter the set's
                     # line number in the text version of the input
                     # file).

unwanted = [] # The positions within the hapaxoid-set of any
                  # words you want to exclude from the output.  You
                  # could also name the words in inverted commas.  If
                  # you don't want to exclude any words, the setting
                  # should be [].

outputFilename = 'output/example' # A filename that isn't in use yet,
                                  # for the output.  Note that
                                  # Hapaxoid will automatically
                                  # append a .txt extension.

# I hope you won't have to alter anything below this line.
# -------------------------------------------------------------------

# Import some utilities from the standard Python library.
import cPickle
from types import *
# Import the source code for use.
import hap
# Load in the data (with some tolerance).
if inputFilename[-4:] == '.txt':
   inputFilename = inputFilename[:-4]
if inputFilename[-4:] != '.pkl':
   inputFilename += '.pkl'
inputFile = open(inputFilename, 'r')
haps = cPickle.load(inputFile)
inputFile.close()
# Find the hapaxoid set in question, again flexibly.
if hapSetID.isdigit():
   index = int(hapSetID) - 1
   hapSet = haps[index]
else:
   for candidate in haps:
      firstWord = candidate.getWordForms()[0]
      if hapSetID == firstWord.getOrthography():
         hapSet = candidate
# Convert the unwanted list to text form if necessary.
textUnwanted = []
spellings = []
for unwantedItem in unwanted:
   if type(unwantedItem) == IntType:
      if spellings == []:
         forms = hapSet.getWordForms()
         spellings = []
         for form in forms:
            spellings.append(form.getOrthography())
      unwantedIndex = unwantedItem - 1
      textUnwanted.append(spellings[unwantedIndex])
   else:
      textUnwanted.append(unwantedItem)
# Create a dictionary containing all the required citations in order.
(citationsDic, keys, spellings) = \
                              hap.sortCitations(hapSet, textUnwanted)
# Append '.txt' to the output filename.
outputFilename += '.txt'
# Create a text file and write the data to it nicely.
hap.writeCitationsDic(citationsDic, keys, outputFilename)
print 'Done.'
