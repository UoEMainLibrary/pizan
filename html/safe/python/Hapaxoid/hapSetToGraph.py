# -*- coding=utf-8

'''
This script is part of Hapaxoid, written by Tommy Herbert for Charlie
Mansfield and Jim Laidlaw.  Please see readme.txt for an overview.

Version 1.0
15th August 2008

---------------------------------------------------------------------

The instructions below are for building a graph using a file that has
been output by the findHapSets.py script.  See that script for
details on how to produce such a file.

Assuming you've run findHapSets.py with the outputFilename parameter
set to 'output/example', there should be two files in the 'output'
directory called example.txt and example.pkl respectively.  Let's say
you open example.txt and find that line 1087 looks like this:

doulour (57): doulçour (36), douloir (22), douleur (121), doulceur (40)

Now, let's say you want your graph to show occurrences of 'doulour',
'douloir' and 'douleur' (don't laugh - I haven't got the first clue
about this language).  You'd set the parameters below like this:

Set inputFilename to 'output/example' (or 'output/example.txt'
or 'output/example.pkl' - it comes to the same thing).

Set hapSetID to 'doulour' or '1087' (recall that it's line number
1087).

Set the 'unwanted' parameter to [2, 5], since 'doulçour' and
'doulceur' are the second and fifth words on line 1087 and you want
to exclude them from the analysis.  Alternatively, you could specify
the unwanted words by name, but this is a little difficult when
there's a ç in one of them: ['doul\xe7our', 'doulceur'].

Set the imageWidth parameter to a reasonable number of pixels, like
900.

Set separateRectoVerso to either False or True, depending on whether
you want the page numbering to run up to just under 400 (as in the
notation used in the Queen's Manuscript transcription file) or to
just under 800 (as in conventional books).

Set pageRange to [0, 'end'], since you want the graph to show the
whole manuscript rather than some section of it.

Set the outputFilename parameter to a name that isn't in use for an
existing file - like 'output/doulour'.  Hapaxoid will automatically
append a '.png' extension to your chosen name.

Then you'd run the script and a image would be created showing all
the occurrences of the words you've chosen to focus on.  If you
also need a list of citations so that you can look them up in the
manuscript, see the script hapSetToText.py.
'''

inputFilename = 'output/example' # The name of the data file output
                                 # by the findHapSets.py script,
                                 # which acts as input here.

hapSetID = 'doulour' # The first word of the hapaxoid-set you want to
                     # represent graphically (you could also enter
                     # the set's line number in the text version of
                     # the input file).

unwanted = [2, 5] # The positions within the hapaxoid-set of any
                  # words you want to exclude from the output.  You
                  # could also name the words in inverted commas.  If
                  # you don't want to exclude any words, the setting
                  # should be [].

imageWidth = 900 # The picture's width in pixels.  If it's too small
                 # to fit the title and legend in, Hapaxoid will
                 # complain.

separateRectoVerso = True # Set to True if you want the recto side of
                          # each sheet of paper to be assigned a
                          # different page number from the verso
                          # side; False otherwise.

pageRange = [0, 'end'] # You can use this setting to make a graph
                       # showing how your chosen words appear in a
                       # section of the manuscript, which can be
                       # useful as a way of zooming in on a crowded
                       # graph.  For example, [110, 125] would show
                       # citations of your chosen words on pages 110
                       # to 125 inclusive.  Most of the time, I
                       # expect you'll want to set this parameter to
                       # [0, 'end'], which asks Hapaxoid to show all
                       # pages.

outputFilename = 'output/doulour' # A filename that isn't in use yet,
                                  # for the output.  Note that
                                  # Hapaxoid will automatically
                                  # append a .png extension.

# I hope you won't have to alter anything below this line.
# -------------------------------------------------------------------

# Import some utilities from the standard Python library.
import cPickle
from types import *
# Import the source code for use.
import hap, graphics
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
# Check whether the hapaxoid set was created with the 'networked'
# parameter set to True.
networked = hapSet.isNetworked()
# Create an image file and draw a graph in it.
graphics.makeGraph(citationsDic,
                   keys,
                   spellings,
                   outputFilename,
                   networked,
                   imageWidth,
                   separateRectoVerso,
                   pageRange)
print 'Done.'
