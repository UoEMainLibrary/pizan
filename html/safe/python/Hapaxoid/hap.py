'''
This module is part of Hapaxoid, written by Tommy Herbert for Charlie
Mansfield and Jim Laidlaw.  Please see readme.txt for an overview.

Version 1.0
15th August 2008
'''

# Import some standard Python modules.
import copy, time
# Import other Hapaxoid modules.
import cases, codes, relatedness

class WordForm:
   '''Instances of this class stand for individual word-forms in the
   manuscript.  Each one contains a record of its spelling, a list of
   the places where it appears in the manuscript, a list of other
   word-forms that are similar in spelling, and a counter that keeps
   track of the number of times it occurs in the manuscript.'''
   def __init__(self, orthography):
      '''This method is automatically called when a new instance of
      the class is created.  It initialises four variables.'''
      self.orthography = orthography # The word's spelling.
      self.citations = [] # A list that will eventually contain
                          # binary tuples of the form (page, line).
                          # It starts off empty, though.
      self.relations = [] # A list that will eventually contain other
                          # WordForms.  It starts empty too.
      self.frequency = 0 # A counter that records how many times this
                         # word appears in the manuscript.  Its
                         # default setting is 0.
   def getOrthography(self):
      '''Returns this word's spelling.'''
      return self.orthography
   def getCitations(self):
      '''Returns a list of all the places where one can find this
      word in the manuscript.'''
      return copy.copy(self.citations)
   def addCitation(self, code):
      '''Adds a new citation to the list of places where this word
      appears and increment the frequency counter.'''
      if not codes.conforms(code):
         print 'Error: WordForm.addCitation was passed the code ' + \
               code + ", which isn't of the right form."
         return
      code = code[1:-1] # Strip the brackets.
      [page, line] = code.split(':')
      self.citations.append((page, line))
      self.frequency += 1
   def alreadyRelation(self, otherForm):
      '''Returns True if the argument is already on this word's
      relations list; otherwise, return False.'''
      return otherForm in self.relations
   def getRelations(self):
      '''Returns a copy of this word's relations list.'''
      return copy.copy(self.relations)
   def addRelations(self, newRelations):
      '''The argument to this method should be a list of WordForms,
      which it will then merge with the existing relations list.'''
      for newRelation in newRelations:
         if not newRelation in self.relations and \
            newRelation.getOrthography() != self.orthography:
            self.relations.append(newRelation)
   def getFrequency(self):
      '''Returns the value of this word's frequency counter.'''
      return self.frequency

class HapSet:
   '''A set of WordForms which have similar spellings.'''
   def __init__(self, wordForms=[], networked=False):
      '''This method is automatically called when a new instance of
      the class is created.  It initialises two variables.'''
      self.wordForms = wordForms # List of WordForms.
      self.networked = networked # Boolean flag that records whether
                                 # this hapaxoid-set was created with
                                 # the 'networked' parameter set to
                                 # True.  See the findHapSets.py
                                 # script for an explanation.
   def __str__(self):
      '''Returns a string summarising the HapSet's contents.'''
      returnString = ''
      length = len(self.wordForms)
      for i in range(length):
         form = self.wordForms[i]
         returnString += (form.getOrthography() + ' (' + \
                          str(form.getFrequency()) + ')')
         if i == 0 and not self.networked:
            returnString += ': '
         elif i < (length - 1):
            returnString += ', '
      return returnString
   def getWordForms(self):
      '''Returns the list of WordForms that belong to this set.'''
      return copy.copy(self.wordForms)
   def isNetworked(self):
      '''Returns the value of this HapSet's 'networked' flag.'''
      return self.networked

def listHaps(dataFilename='t.txt',
             initialMatches=3,
             finalMatches=1,
             minLength=5,
             minOccurrences=3,
             maxDifferences=2,
             networked=False):
   '''Hapaxoid's core function: searches through the file specified
   in the first argument for sets of related words, where 'related'
   means that the sets satisfy the constraints defined by the other
   six arguments.  See the findHapSets.py script for an explanation
   of each parameter.'''
   
   # Bundle the last six parameters into a tuple.
   parameters = (initialMatches,
                 finalMatches,
                 minLength,
                 minOccurrences,
                 maxDifferences,
                 networked)
   # Open the input file for reading.
   dataFile = open(dataFilename, 'r')
   # Go through the file recording all instances of all words (except
   # short ones).
   attestedForms = collectCitations(dataFile, parameters)
   # Close the input file again.
   dataFile.close()
   # Use the citation records to compile sets of related words, and
   # return the results.
   hapSets = makeHapSets(attestedForms, parameters)
   return hapSets

def collectCitations(dataFile, parameters):
   '''Goes through the file specified in the first argument,
   recording all instances of all words (except the ones below the
   minimum length, as set in the second argument).'''
   
   # Extract the minimum length parameter from the tuple.
   minLength = parameters[2]
   # Initialise a counter for keeping track of progress.
   counter = 0
   # Initialise a dictionary for recording the occurrences of each
   # word.  The keys in this dictionary will be strings like
   # 'doulour'; the values will be instances of the WordForm class.
   attestedForms = {}
   # Use a built-in Python function to check the clock, since this
   # can be a lengthy process.
   time = getTime()
   # Reassure the user that something is indeed going on, albeit
   # slowly.
   print time + ' - Collecting citations; printing a dot for ' + \
         'every thousand lines of the file processed:'
   # Extract the first line of data from the file.
   line = dataFile.readline()
   # Loop through this block until there are no more lines of data.
   while line != '':
      # Update the record of the number of lines processed.
      counter += 1
      # Report progress every thousand lines.
      if counter % 1000 == 0:
         print '.'
      # Split the line up into words (using whitespace as a
      # separator).
      tokens = line.split()
      # Ignore empty lines and lines that consist only of a number.
      if len(tokens) > 1:
         # Find the line numbering code.
         code = tokens[0]
      # For each word in the line that's long enough, add it to the
      # dictionary with a record of the page number.
      for token in tokens[1:]:
         if len(token) >= minLength:
            update(attestedForms, token, code, parameters)
      # Move onto the next line of data.
      line = dataFile.readline()
   # Check the clock again.  (With default settings, the above loop
   # usually takes about 12 minutes to complete on my laptop.)
   time = getTime()
   # Report success and return the dictionary.
   print time + ' - Finished collecting citations.'
   return attestedForms

def getTime():
   '''Uses a built-in Python function to check the clock.  Edits out
   things like the date and padding zeroes, then returns what's left
   as a string.'''
   currentTime = list(time.localtime()[3:6])
   for i in range(3):
      element = str(currentTime[i])
      if len(element) == 1:
         element = '0' + element
      currentTime[i] = element
   return currentTime[0] + ':' + \
          currentTime[1] + ':' + \
          currentTime[2]

def update(attestedForms, token, code, parameters):
   '''Adds a new citation to the record being built up by the
   collectCitations function.  If this pushes the word's frequency
   counter past a point specified in the 'parameters' argument,
   notifies the collectRelations function.'''
   
   # Convert the word to lower case.
   token = cases.myLower(token)
   # From the parameters tuple, extract the setting that determines
   # how many times a word must appear in the manuscript for it to be
   # taken seriously.
   minOccurrences = parameters[3]
   # If the word is known already, add this citation to its entry in
   # the dictionary.  If that pushes the frequency over the minimum,
   # call collectCitations.
   if attestedForms.has_key(token):
      wordForm = attestedForms[token]
      wordForm.addCitation(code)
      frequency = wordForm.getFrequency()
      if frequency == minOccurrences:
         collectRelations(wordForm, attestedForms, parameters)
   # If the word isn't known already, create a new entry for it in
   # the dictionary.
   else:
      wordForm = WordForm(token)
      wordForm.addCitation(code)
      attestedForms[token] = wordForm

def collectRelations(wordForm, attestedForms, parameters):
   '''Searches through a (possibly only partially-constructed)
   dictionary of attested word-forms for the ones which are similar
   in spelling to the first argument.'''
   
   # Get the word's spelling.
   orthography = wordForm.getOrthography()
   # Extract the relevant parameter from the tuple.
   minOccurrences = parameters[3]
   # Go through the dictionary one entry at a time.
   for candidateKey in attestedForms.keys():
      # Get a WordForm from the dictionary to compare with the one in
      # hand.
      candidate = attestedForms[candidateKey]
      # Check whether the word in the dictionary is common enough, as
      # well as being distinct from but related to the spelling of
      # the other word.  If so, each word becomes a relation of the
      # other.
      candidateFrequency = candidate.getFrequency()
      if    candidateFrequency >= minOccurrences \
      and   candidateKey != orthography \
      and   directlyRelated(candidateKey, orthography, parameters):
         candidate.addRelations([wordForm])
         wordForm.addRelations([candidate])

def directlyRelated(word1, word2, parameters):
   '''Uses the relatedness module (a separate file of source code) to
   establish whether two words are spelt similarly enough to be of
   interest.  If so, returns True; otherwise, returns False.'''
   
   # Convert both words to lower case.
   word1 = cases.myLower(word1)
   word2 = cases.myLower(word2)
   # Extract the various relevant constraints from the parameters
   # tuple.
   initialMatches = parameters[0]
   finalMatches = parameters[1]
   maxDifferences = parameters[4]
   # Check that both words start the same way.
   if word1[:initialMatches] != word2[:initialMatches]:
      return False
   # Check that both words end the same way.
   if finalMatches > 0:
      finalMatchPoint = 0 - finalMatches
      if word1[finalMatchPoint:] != word2[finalMatchPoint:]:
         return False
   # Work out how many steps it takes to transform one word into
   # another.  (For discussion of what counts as a step, see the
   # findHapSets.py script.)  Check whether this number exceeds the
   # maximum set in the parameters.
   return relatedness.steps(word1, word2) <= maxDifferences

def makeHapSets(attestedForms, parameters):
   '''Given a dictionary of words where each entry includes a list
   of relations, return all the sets of relations.'''
   
   # Check whether a set consists of a single important word and its
   # relations (easy) or a whole network of words that are all
   # indirectly related to one another (more complicated).
   networked = parameters[5]
   # Report that the process is underway.
   print 'Building sets of related hapaxoids.'
   # Initialise the list of hapaxoid sets which will be returned.
   hapSets = []
   if networked: # The more complicated way.
      # Gradually delete entries from the dictionary as you deal with
      # them, and stop when it's empty.
      while attestedForms != {}:
         # Look at the first word in the dictionary.
         word = attestedForms.keys()[0]
         wordForm = attestedForms[word]
         # Look at the word's relations.
         relations = wordForm.getRelations()
         # If it doesn't have any, delete it.  (For rare words, none
         # will have been collected.)
         if relations == []:
            del attestedForms[word]
         else: # If it does have relations...
            # Initialise a hapaxoid set consisting of the word and
            # its direct relations.
            haps = [wordForm] + relations
            # Add to the set all relations of relations, and all
            # _their_ relations, and so one.
            collectingRelations = True
            while collectingRelations:
               collectingRelations = False
               for hap in haps:
                  newRelations = hap.getRelations()
                  for newRelation in newRelations:
                     if not newRelation in haps:
                        collectingRelations = True
                        haps.append(newRelation)
            # Create an instance of the HapSet object to represent
            # the set.
            hapSet = HapSet(haps, networked=True)
            # Add the set to the list which will be returned.
            hapSets.append(hapSet)
            # Delete all the words in the set from the dictionary.
            for wordForm in haps:
               key = wordForm.getOrthography()
               del attestedForms[key]
   else: # The easy way.
      # Work through the dictionary, adding a HapSet to the
      # return-list for each entry.
      for key in attestedForms.keys():
         wordForm = attestedForms[key]
         relations = wordForm.getRelations()
         if relations != []:
            # This time, the HapSet simply consists of the word and
            # its direct relations.  Not that there will be another
            # HapSet for each of the relations, which will also
            # contain this word, but which may well have other words
            # that don't appear in this set.
            haps = [wordForm] + relations
            hapSet = HapSet(haps, networked=False)
            hapSets.append(hapSet)
   # Sort the return-list.
   hapSets = alphabetise(hapSets)
   # Report success and return the list.
   print 'Finished building sets.'
   return hapSets

def alphabetise(hapSets):
   '''Sorts a list of HapSet objects alphabetically by the first word
   in the set.'''
   dic = {}
   for hapSet in hapSets:
      wordForms = hapSet.getWordForms()
      key = wordForms[0].getOrthography()
      dic[key] = hapSet
   keys = dic.keys()
   keys.sort()
   returnList = []
   for key in keys:
      returnList.append(dic[key])
   return returnList

def textDump(hapSets, outputFilename):
   '''Creates a new text file and write a summary to it for each
   hapaxoid-set in the list.  This function is called directly by the
   findHapSets.py script.'''
   outputFile = open(outputFilename, 'w')
   for hapSet in hapSets:
      outputFile.write(str(hapSet) + '\n')
   outputFile.close()

def showPages(hapSet, unwantedList=[]):
   '''I've left this function in because you might want to call it,
   but it's been superseded by the hapSetToText.py script, which
   calls the sortCitations and writeCitationsDic functions below.  It
   prints out all the citations for a particular hapaxoid set to the
   standard output, along with a preamble.'''
   (citationsDic, keys, spellings) = \
                                 sortCitations(hapSet, unwantedList)
   if hapSet.isNetworked():
      output = 'Here are the citations for the set '
      for spelling in spellings:
         output += (spelling + '/')
      output = output[:-1] + ':'
      print output
   else:
      output = 'The word ' + spellings[0] + ' might be related to '
      numberOfVariations = len(spellings[1:])
      for i in range(numberOfVariations):
         output += spellings[i+1]
         if i < (numberOfVariations - 2):
            output += ', '
         elif i == (numberOfVariations - 2):
            output += ' and '
      print output + '. Here are the citations for these forms:'
   printCitationsDic(citationsDic, keys)

def sortCitations(hapSet, unwantedList=[]):
   '''Given a HapSet object and an optional list of words to exclude,
   compiles a dictionary, organised by page number, showing where
   each word appears.  This dictionary can be used as the input for
   printCitationsDic, writeCitationsDic or the makeGraph function in
   the graphics module.  This function is therefore called by the
   scripts hapSetToText.py and hapSetToGraph.py.'''
   forms = hapSet.getWordForms()
   spellings = []
   # The citations dictionary starts off empty, but its keys will be
   # page numbers (strictly speaking, they're book-page-column codes,
   # as in 'EROS.244a') and its values will be lists of spellings.
   citationsDic = {}
   for form in forms:
      spelling = form.getOrthography()
      if spelling in unwantedList:
         continue
      spellings.append(spelling)
      citationsList = form.getCitations()
      for (page, line) in citationsList:
         if citationsDic.has_key(page):
            citationsDic[page].append(spelling)
         else:
            citationsDic[page] = [spelling]
   keys = citationsDic.keys()
   keys.sort(codes.comparePages)
   # Apart from the dictionary itself, the function returns 'keys',
   # which orders the dictionary's entries according to the
   # manuscript's pages, and 'spellings', which contains a list of
   # the set's variant spellings.
   return (citationsDic, keys, spellings)

def printCitationsDic(citationsDic, keys):
   '''I've left this function in because you might want to call it,
   but it's been superseded by the hapSetToText.py script, which
   calls the sortCitations and writeCitationsDic functions.  It
   prints out all the citations for a particular hapaxoid set to the
   standard output.'''
   currentSpelling = ''
   for key in keys:
      spellings = citationsDic[key]
      spellings = removeDupes(spellings)
      output = spellings[0]
      if len(spellings) > 1:
         for spelling in spellings[1:]:
            output += (', ' + spelling)
      if output == currentSpelling:
         print '\t' + key
      else:
         currentSpelling = output
         print output + ': ' + key

def writeCitationsDic(citationsDic, keys, outputFilename):
   '''Creates a new text file and writes out all the citations for a
   particular hapaxoid set.  Called by the hapSetToText.py script.'''
   outputFile = open(outputFilename, 'w')
   currentSpelling = ''
   for key in keys:
      spellings = citationsDic[key]
      spellings = removeDupes(spellings)
      output = spellings[0]
      if len(spellings) > 1:
         for spelling in spellings[1:]:
            output += (', ' + spelling)
      if output == currentSpelling:
         outputFile.write('\t' + key + '\n')
      else:
         currentSpelling = output
         outputFile.write(output + ': ' + key + '\n')
   outputFile.close()

def removeDupes(list):
   '''Little function that serves writeCitationsDic (and, for what
   it's worth, printCitationsDic).  Takes a list which may contain
   duplicate members and returns one which doesn't.'''
   returnList = []
   for item in list:
      if not item in returnList:
         returnList.append(item)
   return returnList
