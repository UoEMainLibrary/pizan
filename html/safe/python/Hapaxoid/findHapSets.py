# -*- coding=utf-8

'''
This script is part of Hapaxoid, written by Tommy Herbert for Charlie
Mansfield and Jim Laidlaw.  Please see readme.txt for an overview.

Version 1.0
15th August 2008

---------------------------------------------------------------------

The instructions below search an input file for sets of words that
resemble one another closely enough to be considered potential
hapaxoids.  These sets are then recorded in two forms: a
human-readable file with a .txt extension and a computer-readable one
with a .pkl extension.  You can then open the text output and examine
it to see which words are promising.  A typical line would look like
this (although that first colon depends on the 'networked'
parameter):

doulour (57): doulçour (36), douloir (22), douleur (121), doulceur (40)

This shows that 'doulour', which appears 57 times in the manuscript,
has four relations which might or might not be variant spellings of
the same word, and that they appear 36, 22, 121 and 40 times
respectively.  I don't know anything about medieval French, but if I
had to guess, I'd say that doulçour and doulceur were etymologically
unrelated to doulour, but that the other two deserved further
investigation.  I might therefore use the script hapSetToText.py to
get a list of the page numbers where doulour, douloir and douleur
appear (see that file for instructions on how this is done).
Alternatively, I might use hapSetToGraph.py to display the same
information visually (again, please refer to the notes in that file).
'''

# Parameters: change these before running the script to get the
# behaviour you want.

dataFilename = 't.txt' # The location of a text file containing a
                       # transcription of the Queen's Manuscript.

initialMatches = 3     # To be potential hapaxoids, two words must
                       # start the same: they must share this number
                       # of letters, counting from the left.

finalMatches = 1       # They must also share this number of letters,
                       # counting from the right.

minLength = 5          # Only consider words that are at least this
                       # long.

minOccurrences = 3     # Ignore very rare words: a word must appear
                       # in the manuscript at least this many times
                       # to be considered.

maxDifferences = 2     # This setting is the core of the Hapaxoid
                       # system.  Words are considered to be related
                       # to one another if they are spelt similarly.
                       # The maxDifferences parameter limits the
                       # number of steps you're allowed to take to
                       # transform one word into another - any more,
                       # and the words aren't related after all.  A
                       # single step can be any of three actions:
                       # Insert a letter, as in 'heat' -> 'heart'.
                       # Delete a letter, as in 'heat' -> 'hat'.
                       # Change a letter, as in 'heat' -> 'meat'.

networked = False      # When a set contains more than two words,
                       # there are various possible ways in which one
                       # might want to apply the relatedness
                       # constraint described above.  When this
                       # parameter is set to False, the first word in
                       # a set is considered to be the important one:
                       # all other words must be related to it.  On
                       # the other hand, setting it to True will tend
                       # to increase the size of a set, because it
                       # relaxes the requirements for membership.
                       # This time, no word has special status - a
                       # word can join the set if it's related to any
                       # word already in the set. Note that there's
                       # currently no way to insist that each word in
                       # a set is related to _every_ other.

outputFilename = 'output/hapSets' # The script will create two new
                                  # files with this path and basic
                                  # name.  Note that the name
                                  # doesn't have an extension yet:
                                  # '.txt' will be appended to make
                                  # one full filename; '.pkl' will
                                  # be appended to make another.

# I hope you won't have to alter anything below this line.
# -------------------------------------------------------------------

# Import some utilities from the standard Python library.
import os, cPickle
# Import the source code for use.
import hap
# Scan the input file for all sets of words that satisfy the
# parameters above.  If anything is missing from this function call,
# by the way, listHaps will silently insert default values.  Using
# such values, the function takes about twelve minutes to run on my
# rickety laptop, but fiddling with the parameters can increase that
# to over two hours.
haps = hap.listHaps(dataFilename,
                    initialMatches,
                    finalMatches,
                    minLength,
                    minOccurrences,
                    maxDifferences,
                    networked)
# Create the computer-readable record of the exercise.
pickleFilename = outputFilename + '.pkl'
pickleFile = open(pickleFilename, 'w')
cPickle.dump(haps, pickleFile)
pickleFile.close()
# Create the human-readable text file.
textFilename = outputFilename + '.txt'
hap.textDump(haps, textFilename)
