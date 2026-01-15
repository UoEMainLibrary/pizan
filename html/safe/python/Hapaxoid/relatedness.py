# -*- coding=utf-8

'''
This module supports the hap.py module.  They belong to an
application called Hapaxoid, which was written by Tommy Herbert for
Charlie Mansfield and Jim Laidlaw.  Please see readme.txt for an
overview.

Version 1.0
15th August 2008
'''

def steps(startWord, goalWord):
   '''The main function of this module: returns the number of steps
   needed to transform the first word into the second.  For
   discussion of what counts as a step, see the findHapSets.py
   script.'''
   
   # Initialise the bestCost variable with a large number.
   bestCost = 100
   # See if there's any work to do.
   if startWord == goalWord:
      return 0
   # Work out which word is longer.
   if len(startWord) > len(goalWord):
      longerWord = startWord
      shorterWord = goalWord
   else:
      longerWord = goalWord
      shorterWord = startWord
   # Line the two words up and see how many times the same letter
   # occurs in the same position.  Or, strictly speaking, how many
   # times it doesn't.
   mismatches = countMismatches(shorterWord, longerWord)
   # Look for ways to shunt a section of the shorter word leftwards
   # or rightwards to decrease the number of mismatches.  A shift
   # only counts as useful if it's cheaper than decreasing the
   # mismatches just by changing one letter at a time.  The thinking
   # is that sometimes inserting or deleting the odd character is
   # the most efficient way of transforming the word.
   shifts = findUsefulShifts(shorterWord, longerWord, mismatches)
   # If there are no useful shifts, the cost is simple to calculate
   # because it equals the number of mismatches.
   if shifts == []:
      return mismatches
   # Recursively call this function again as many times as it takes
   # to work out which shift to perform first.  This exhaustive,
   # depth-first search will always find the optimal solution.
   for (candidate, shiftCost) in shifts:
      costOfRest = steps(candidate, longerWord)
      pathCost = shiftCost + costOfRest
      if pathCost < bestCost:
         bestCost = pathCost
   # Return the cost of that best first shift plus the steps that
   # followed it at deeper levels of recursion.
   return bestCost

def countMismatches(word1, word2):
   '''Line the two words up and see how many times the same letter
   occurs in the same position.  Or, strictly speaking, how many
   times it doesn't.'''
   matches = 0
   if len(word1) < len(word2):
      shorterWord = word1
      longerWord = word2
   else:
      shorterWord = word2
      longerWord = word1
   for i in range(len(shorterWord)):
      if shorterWord[i] == longerWord[i]:
         matches += 1
   mismatches = len(longerWord) - matches
   return mismatches

def findUsefulShifts(shorterWord, longerWord, existingMismatches):
   '''Look for ways to shunt a section of the shorter word leftwards
   or rightwards to decrease the number of mismatches.  A shift only
   counts as useful if it's cheaper than decreasing the mismatches
   just by changing one letter at a time.'''
   
   # Initialise the list of shifts as empty.
   shifts = []
   # Consider both leftward and rightward shifts.
   for direction in ['leftwards', 'rightwards']:
      # The right-hand end of the span to be shifted will almost
      # always be at least two positions from the start of the word.
      # The exception is a one-letter word.
      if direction == 'rightwards' and len(shorterWord) == 1:
         earliestEnd = 1
      else:
         earliestEnd = 2
      # Examine all possible positions for the right-hand end of the
      # span. 
      for spanEnd in range(earliestEnd, len(shorterWord) + 1):
         # You might want to shift the last letter rightwards;
         # otherwise, useful shifts need multi-letter spans.
         if direction == 'rightwards' and \
                                       spanEnd == len(shorterWord):
            latestStart = len(shorterWord) - 1
         else:
            latestStart = spanEnd - 2
         # Examine all possible positions for the left-hand end of
         # the span.
         for spanStart in range(latestStart + 1):
            # Various factors limit how far you can usefully shift
            # the chosen span.
            maxDisplacement = findMaxDisplacement(shorterWord,
                                                  longerWord,
                                                  spanStart,
                                                  spanEnd,
                                                  direction)
            # Given that, examine all possibilities for the extent of
            # the shift.
            for displacement in range(1, maxDisplacement + 1):
               # Finally, we've completely specified a particular
               # shift and can calculate its cost.
               (candidate, cost) = shift(shorterWord,
                                         longerWord,
                                         spanStart,
                                         spanEnd,
                                         direction,
                                         displacement)
               # To gauge whether the shift is useful, that cost must
               # be weighed against the benefit the shift brings in
               # terms of mismatch reduction.
               mismatches = countMismatches(candidate, longerWord)
               mismatchReduction = existingMismatches - mismatches
               if mismatchReduction < 1:
                  # A shift is useless if it doesn't reduce
                  # mismatches.
                  continue
               else:
                  costPerImprovement = \
                              float(cost) / float(mismatchReduction)
                  # A shift is useless if it can't beat the simpler
                  # strategy of reducing mismatches by changing
                  # letters one at a time.
                  if costPerImprovement < 1:
                     shifts.append((candidate, cost))
   # Return a list of shifts, each labelled with its own cost.
   return shifts

def findMaxDisplacement(shorterWord, longerWord,
                        spanStart, spanEnd,
                        direction):
   '''Given two words, a span of letters to move and a direction to
   move them in, decide how far to consider moving them.'''
   if (direction == 'rightwards') and (spanEnd == len(shorterWord)):
      return len(longerWord) - spanStart - 1
   else:
      return spanEnd - spanStart - 1

def shift(shorterWord, longerWord,
          spanStart, spanEnd,
          direction, displacement):
   '''Works out what new word results if you shift a span of letters
   a certain number of spaces in a certain direction.  If a span is
   moving towards non-moving letters, it disappears (using deletion
   operations) as it gets shoved into them.  The space that opens up
   on the other side gets filled with letters that match their
   counterparts in the target word (using insertion operations).
   Along with the new word, this function also returns the cost of
   the shift.'''
   if direction == 'rightwards':
      if spanEnd == len(shorterWord):
         # Shifting a word-final span rightwards is cheaper because
         # there's no deletion involved.
         newBit = longerWord[spanStart : spanStart + displacement]
         newWord = shorterWord[:spanStart] + \
                   newBit + \
                   shorterWord[spanStart:]
         cost = displacement
      else: # Rightward shifts for non-final spans.
         newBit = longerWord[spanStart : spanStart + displacement]
         spanRemainder = \
                     shorterWord[spanStart : spanEnd - displacement]
         newWord = shorterWord[:spanStart] + \
                   newBit + \
                   spanRemainder + \
                   shorterWord[spanEnd:]
         cost = displacement * 2
   else: # Leftward shifts.
      spanRemainder = shorterWord[spanStart + displacement : spanEnd]
      newBit = longerWord[spanEnd - displacement : spanEnd]
      newWord = shorterWord[:spanStart] + \
                spanRemainder + \
                newBit + \
                shorterWord[spanEnd:]
      cost = displacement * 2
   return (newWord, cost)
