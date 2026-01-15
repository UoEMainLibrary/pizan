'''
This module serves the hapSetToGraph.py script, which is part of
an application called Hapaxoid, written by Tommy Herbert for Charlie
Mansfield and Jim Laidlaw.  Please see readme.txt for an overview.

Version 1.0
15th August 2008
'''

# Import some standard Python modules.  For information about the
# graphics libraries, see www.pythonware.com/library/pil/handbook.
import Image, ImageDraw, ImageFont, copy
# A constant specifying the number of pages in the manuscript.
PAGES = 796
# Change these measurements if you don't like the layout of the graph
# images.
defaultImageHeight = 250
spaceBelowAxis = 50
axisMargin = 30
lineClearance = 2
lineHeight = 15
legendClearance = 15
legendRowSpacing = 10
legendColumnSpacing = 12
legendKeySeparation = 10
legendMargin = 12
legendTitleSpace = 4
titleClearance = 15
# With the following list, most graphs should be readable by
# colour-blind people.
colours = ['red', 'rgb(36,178,80)', 'blue', 'darkOrange',
           'rgb(255,135,255)', 'rgb(167,227,31)', 'gray',
           'mediumTurquoise', 'rgb(176,48,96)', 'slateBlue',
           'saddleBrown', 'gold']

def makeGraph(citationsDic,
              keys,
              spellings,
              filename,
              networked=False,
              imageWidth=900,
              separateRectoVerso=True,
              pageRange=(0,'end')):
   '''The main function for this module: creates a new image file and
   draws a graph on it representing the citations in the first
   argument.  For discussion of all eight parameters, see the
   hapSetToGraph.py script.'''
   
   # If there are more than 12 distinct spellings in the list,
   # complain and give up.  I found that more than 12 easily
   # distinguishable hues are tricky to come up with. If it becomes
   # an issue, though, there's probably room for 3 or 4 more; after
   # that, you'd need to start using patterns or something.  Above
   # 20, you may need to look at planLegend and drawTitle to make
   # sure everything's going to fit in and look nice.
   if len(spellings) > 12:
      print "Error: the makeGraph function isn't designed to " + \
            'deal with more than 12 hapaxoids at once.'
      return
   # Some other checks.
   if len(spellings) < 1:
      print 'Error: the input to the makeGraph function appears ' + \
            'to be empty.'
      return
   if checkRange(separateRectoVerso, pageRange) == False:
      print 'Error: makeGraph has been asked to examine pages ' + \
            "that don't exist. Try changing one or both of the " + \
            'pageRange and separateRectoVerso parameters.'
      return
   # Load in the fonts from their folder.
   roman = ImageFont.truetype('fonts/luxisr.ttf', 12)
   italic = ImageFont.truetype('fonts/luxisri.ttf', 12)
   bold = ImageFont.truetype('fonts/luxisb.ttf', 12)
   fonts = (roman, italic, bold)
   # Plan the position and other measurements for the legend.
   (imageHeight,
    legendPosition,
    legendRows,
    legendColumns,    
    legendWidth,
    legendHeight,
    legendTitleHeight,
    legendColumnWidth,
    legendRowHeight) = planLegend(spellings, fonts, imageWidth)
   # Bundle the two settings for the overall image's size into one
   # tuple.
   imageDimensions = (imageWidth, imageHeight)
   # Initialise an image for drawing on.
   graph = Image.new('RGB', imageDimensions, 'white')
   draw = ImageDraw.Draw(graph)
   # Add the graph's title.  (If the image is too narrow, this may
   # fail.)
   titleSuccess = drawTitle(draw,
                            imageDimensions,
                            legendPosition,
                            fonts,            
                            spellings,
                            networked)
   if not titleSuccess:
      return
   # Add the legend in the top right.
   drawLegend(draw,
              legendPosition,
              legendRows,
              legendColumns,
              legendWidth,
              legendHeight,
              legendTitleHeight,
              legendColumnWidth,
              legendRowHeight,
              fonts,
              spellings)
   # Work out some measurements for the graph's axis.
   axisData = planAxis(imageDimensions,
                       separateRectoVerso,
                       fonts,
                       pageRange)
   # Draw the axis.
   drawAxis(draw, axisData, fonts)
   # Process the citations dictionary so that it has simple integers
   # for page numbers, just like the axis labels.
   simpleDic = simplifyDic(citationsDic, separateRectoVerso)
   # Add the coloured lines that represent the data.
   drawLines(draw, axisData, simpleDic, spellings)
   # Save the image as a new PNG file with a user-specified name.
   graph.save(filename + '.png', 'PNG')

def checkRange(separateRectoVerso, pageRange):
   '''Ensures that the first page comes before the last page, and
   that neither falls outside the manuscript, given the numbering
   convention specified by separateRectoVerso (where True means that
   the recto side of each sheet of paper has a separate page number
   from the verso side).'''
   (firstPage, lastPage) = pageRange
   if lastPage == 'end':
      if firstPage < (PAGES / 2):
         return True
      elif separateRectoVerso and firstPage < PAGES:
         return True
      else:
         return False
   else:
      if firstPage >= lastPage:
         return False
      elif lastPage <= (PAGES / 2):
         return True
      elif separateRectoVerso and lastPage <= PAGES:
         return True
      else:
         return False

def planLegend(spellings, fonts, imageWidth):
   '''Calculates most of the numbers required to draw the legend.
   These measurements also affect where the graph's title will go.'''
   
   # Decide the number of columns in the legend's table, based on the
   # number of different spellings it has to accommodate.
   spellingCount = len(spellings)
   if spellingCount < 4:
      columns = 1
   elif spellingCount < 9:
      columns = 2
   elif spellingCount < 16:
      columns = 3
   else:
      columns = 4
   # That in turn dictates the number of rows.
   rows = spellingCount / columns
   # The result of the above operation is rounded down to the nearest
   # integer, so add a row if there's a remainder.
   if (spellingCount % columns) > 0:
      rows += 1
   # Unpack the three fonts.
   (roman, italic, bold) = fonts
   # Calculate the width of each column in the legend by finding the
   # widest label.
   columnWidth = maxWidth(spellings, roman) + legendKeySeparation + 1
   # Add up the overall width of the legend.
   legendWidth = (columns * columnWidth) + \
                 ((columns - 1) * legendColumnSpacing) + \
                 (legendMargin * 2) + 2
   # Similarly, get the heights of a single row and the whole legend.
   # This time, an extra consideration is the legend's title, which
   # stands proud of the main box.
   rowHeight = max(maxHeight(spellings, roman), lineHeight)
   legendTitleHeight = bold.getsize('Legend')[1]
   legendHeight = (rows * rowHeight) + \
                  ((rows - 1) * legendRowSpacing) + \
                  (legendMargin * 2) + 2 + (legendTitleHeight / 2)
   # The legend's position is defined in terms of its highest and
   # leftmost points.  As with all positions in this module, the
   # origin is the top left corner of the image.
   positionX = imageWidth - (legendWidth + legendClearance)
   positionY = legendClearance
   position = (positionX, positionY)
   # Fitting the axis, the data and the legend in gives a minimum
   # height for the overall image.
   requiredImageHeight = spaceBelowAxis + 1 + lineClearance + \
                         lineHeight + (legendClearance * 2) + \
                         legendHeight
   # But there's no need to have a really squat image just because
   # it's possible.
   imageHeight = max(defaultImageHeight, requiredImageHeight)
   # Return the results of all calculations.
   return (imageHeight,
           position,
           rows,
           columns,
           legendWidth,
           legendHeight,
           legendTitleHeight,
           columnWidth,
           rowHeight)

def maxWidth(strings, font):
   '''Returns the width in pixels of the widest of a list of strings,
   given a particular font.'''
   return maxSize(strings, font, 0)

def maxHeight(strings, font):
   '''Returns the height in pixels of the highest of a list of
   strings, given a particular font.'''
   return maxSize(strings, font, 1)

def maxSize(strings, font, dimension):
   '''Returns the size in pixels of the largest of a list of strings,
   given a particular font and dimension along which to measure.'''
   max = 0
   for string in strings:
      size = font.getsize(string)[dimension]
      if size > max:
         max = size
   return max

def drawTitle(draw,
              imageDimensions,
              legendPosition,
              fonts,           
              spellings,
              networked):
   '''Adds the graph's title to the image.  Note that currently,
   drawTitle doesn't use the 'networked' parameter, but it's there in
   case you want to vary the wording of the title.'''
   
   # Unpack the image's dimensions, the legend's position and the
   # fonts.
   (imageWidth, imageHeight) = imageDimensions
   (legendX, legendY) = legendPosition
   (roman, italic, bold) = fonts
   # Change this if you don't like the wording of the graphs' titles.
   romanTitle = 'Spelling variations by page number: '
   # The title is completed in italics with the spelling of the first
   # word on the list.
   italicTitle = spellings[0]
   # Calculate the title's width and height.
   (romanWidth, romanHeight) = roman.getsize(romanTitle)
   (italicWidth, italicHeight) = italic.getsize(italicTitle)
   titleWidth = romanWidth + italicWidth
   titleHeight = max(romanHeight, italicHeight)
   # Check whether the legend comes up so high that it needs to
   # squeeze the title leftwards.
   if (legendY < (titleHeight + (titleClearance * 2))):
      legendInterferes = True
   else:
      legendInterferes = False
   # If the legend doesn't leave room for the title, give up on the
   # whole affair.
   if legendInterferes and \
                     (legendX < (titleWidth + (titleClearance * 2))):
      print 'Error: the requested width is too small to fit in ' + \
            'the title and the legend.  Try a wider graph.'
      return False
   # Even if the legend isn't in the way, the user may have picked
   # such a small number for the width that the title won't fit.
   # Give up in that case, too.  To improve this code, by the way,
   # one could introduce multi-line titles.
   if imageWidth < (titleWidth + (titleClearance * 2)):
      print 'Error: the requested width is too small to fit in ' + \
            ' the title.  Try a wider graph.'
      return False
   # Centre the title in the available space.
   if legendInterferes:
      titleCentre = legendX / 2
   else:
      titleCentre = imageWidth / 2
   # Calculate the title's leftmost point.
   titleX = titleCentre - (titleWidth / 2)
   # Put the roman and italic components of the title onto the image.
   # Note that the y-coordinate is specified among the constants at
   # the top of this file.
   draw.text((titleX, titleClearance),
             romanTitle,
             font=roman,
             fill='black')
   titleX += romanWidth
   draw.text((titleX, titleClearance),
             italicTitle,
             font=italic,
             fill='black')
   # Report success.
   return True

def drawLegend(draw, position, rows, columns, width, height,
               titleHeight, columnWidth, rowHeight, fonts,
               spellings):
   '''Puts the legend into the image.'''
   
   # Unpack the legend's coordinates.
   (positionX, positionY) = position
   # Because the legend's title stands proud of the box, the
   # position of the top of the box needs another calculation.
   boxTopLeft = (positionX, positionY + (titleHeight / 2))
   boxTopRight = (positionX + width - 1,
                  positionY + (titleHeight / 2))
   boxBottomLeft = (positionX, positionY + height - 1)
   boxBottomRight = (positionX + width - 1, positionY + height - 1)
   # Unpack the fonts.
   (roman, italic, bold) = fonts
   # Find the title's width and centre it at the top of the box.
   title = 'Legend'
   titleWidth = bold.getsize(title)[0]
   centreX = positionX + (width / 2)
   titlePosition = (centreX - (titleWidth / 2), positionY)
   # Calculate the final two vertices needed for drawing the box with
   # a gap for the title.
   titleGapLeft = (titlePosition[0] - legendTitleSpace,
                   positionY + (titleHeight / 2))
   titleGapRight = (titlePosition[0] + titleWidth + legendTitleSpace,
                    positionY + (titleHeight / 2))
   # Count the labels that need to go into the legend.
   spellingsCount = len(spellings)
   # Draw the box.
   draw.line([titleGapRight,
              boxTopRight,
              boxBottomRight,
              boxBottomLeft,
              boxTopLeft,
              titleGapLeft], fill='black')
   # Put the title in.
   draw.text(titlePosition, title, font=italic, fill='black')
   # Draw the labels and coloured lines.
   for column in range(columns):
      for row in range(rows):
         spellingIndex = (column * rows) + row
         if spellingIndex < spellingsCount:
            spelling = spellings[spellingIndex]
            lineX = positionX + 1 + legendMargin + \
                    ((columnWidth + legendColumnSpacing) * column)
            lineTopY = boxTopLeft[1] + 1 + legendMargin + \
                       ((rowHeight + legendRowSpacing) * row)
            lineBottomY = lineTopY + lineHeight
            spellingPositionX = lineX + 1 + legendKeySeparation
            spellingPositionY = lineTopY
            draw.line([(lineX, lineTopY), (lineX, lineBottomY)],
                      fill=colours[spellingIndex])
            draw.text((spellingPositionX, spellingPositionY),
                      spelling, font=roman, fill='black')

def planAxis((imageWidth, imageHeight),
             separateRectoVerso,
             fonts,
             pageRange):
   '''Calculates the coordinates for the axis.'''
   axisY = imageHeight - spaceBelowAxis
   axisLeftX = axisMargin
   axisRightX = imageWidth - axisMargin
   # Find the first and last page numbers to be represented.
   firstPage = pageRange[0]
   if pageRange[1] == 'end':
      if separateRectoVerso:
         lastPage = PAGES
      else:
         lastPage = PAGES / 2
   else:
      lastPage = pageRange[1]
   # Find a good way of dividing up the page range.
   (incrementsCount,
    pagesPerIncrement,
    rounding) = findIncrements(imageWidth, firstPage, lastPage)
   # Extract the roman font.
   roman = fonts[0]
   # Calculate the length of the axis.
   axisLength = (axisRightX - axisLeftX) + 1
   # Calculate the horizontal distance that represents each page. 
   pixelsPerPage = float(axisLength) / (lastPage - firstPage)
   # Calculate the labels and coordinates for all increments.
   increments = {}
   for i in range(incrementsCount + 1):
      # Calculate the page number represented by the marker.
      if i == 0:
         page = firstPage
      elif i == incrementsCount:
         page = lastPage
      else:
         page = firstPage + (pagesPerIncrement * i)
         page = myRound(page, rounding)
      # Calculate the x-coordinate for the marker.
      if i == incrementsCount:
         markerX = axisRightX
      else:
         markerX = axisLeftX + \
                   int((page - firstPage) * pixelsPerPage)
      # Create the label.
      label = str(page)
      # Calculate the x-coordinate for the label.
      labelWidth = roman.getsize(label)[0]
      labelX = markerX - (labelWidth / 2)
      # Add all three pieces of information to the dictionary.
      increments[label] = [markerX, labelX]
   # Calculate the label and coordinates for the last increment.
   label = str(lastPage)
   labelWidth = roman.getsize(label)[0]
   labelX = axisRightX - (labelWidth / 2)
   increments[label] = [axisRightX, labelX]
   # Hand in your work.
   return (axisLeftX, axisRightX, axisY, increments,
           firstPage, lastPage)

def findIncrements(imageWidth, firstPage, lastPage):
   '''Finds a good way of dividing up the page range.'''
   
   # Calculate the number of increments to mark on the axis.
   if imageWidth >= 800:
      incrementsCount = 4
   elif imageWidth >= 400:
      incrementsCount = 3
   else:
      incrementsCount = 2
   # Make sure the pageRange can support the number of increments.
   if (lastPage - firstPage) < incrementsCount:
      incrementsCount = lastPage - firstPage
   # Decide how many pages should be represented by each increment.
   pagesPerIncrement = float(lastPage - firstPage) \
                       / incrementsCount
   if pagesPerIncrement >= 50:
      roundingNumber = 50
   elif pagesPerIncrement >= 10:
      roundingNumber = 10
   else:
      roundingNumber = 1
   pagesPerIncrement = myRound(pagesPerIncrement, roundingNumber)
   # If the last two increments will appear too close
   # together, drop one.
   penult = firstPage + (pagesPerIncrement * (incrementsCount - 1))
   penult = myRound(penult, roundingNumber)
   if (lastPage - penult) < (pagesPerIncrement / 4):
      incrementsCount -= 1
   return (incrementsCount, pagesPerIncrement, roundingNumber)

def myRound(unroundedNumber, roundingNumber):
   '''Each argument can be any positive number.  Returns whichever
   multiple of the second argument is closest to the first argument
   (unless the second argument isn't an integer - then the result is
   close to a multiple).'''
   roundedDown = int(int(unroundedNumber / roundingNumber) \
                 * roundingNumber)
   roundedUp = roundedDown + roundingNumber
   distanceDownwards = abs(unroundedNumber - roundedDown) 
   distanceUpwards = abs(unroundedNumber - roundedUp)
   if distanceDownwards < distanceUpwards:
      return roundedDown
   else:
      return roundedUp

def drawAxis(draw, axisData, fonts):
   '''Puts the graph's axis onto the image.'''
   
   # Extract all necessary information.
   (axisLeftX, axisRightX, axisY, increments) = axisData[:4]
   roman = fonts[0]
   # Draw the main horizontal line.
   draw.line([(axisLeftX, axisY), (axisRightX, axisY)], fill='black')
   # Draw the marker and label for each increment.
   for label in increments.keys():
      [markerX, labelX] = increments[label]
      draw.line([(markerX, axisY + 1), (markerX, axisY + 4)],
                fill='black')
      draw.text((labelX, axisY + 7), label, font=roman, fill='black')

def simplifyDic(citationsDic, separateRectoVerso):
   '''Prepares the citations data for use by drawLines.  The keys in
   citationsDic are column codes like 'EROS.244a'; the values are
   lists of spellings.  Return a dictionary where keys are ordinary
   page numbers (which means merging some of the entries in
   citationsDic).'''
   simpleDic = {}
   for key in citationsDic.keys():
      simpleKey = simplifyKey(key, separateRectoVerso)
      if simpleDic.has_key(simpleKey):
         simpleDic[simpleKey].extend(citationsDic[key])
      else:
         simpleDic[simpleKey] = copy.copy(citationsDic[key])
      # Rearrange the spellings so that they appear in blocks of
      # similar ones.  That way, the graph won't appear bitty.
      simpleDic[simpleKey].sort()
   return simpleDic

def simplifyKey(key, separateRectoVerso):
   '''Translates a page/column code of the type 'EROS.244a' to the
   kind of page number used to label the graph's axis.'''
   pageCode = key.split('.')[1]
   page = int(pageCode[:-1])
   column = pageCode[-1]
   if separateRectoVerso:
      simpleKey = page * 2
      if column in 'rab':
         simpleKey -= 1
   else:
      simpleKey = page
   return simpleKey

def drawLines(draw, axisData, simpleDic, spellings):
   '''Adds the citation data to the graph.  Where multiple spellings
   appear on the same page, the lines are drawn next to each other.
   If the graph is wide enough, some pages will therefore show up as
   a rectangle - possibly multicoloured.'''
   (axisLeftX, axisRightX, axisY) = axisData[:3]
   (firstPage, lastPage) = axisData[4:]
   pixelsPerPage =   (float(axisRightX) + 1 - axisLeftX) \
                   / (lastPage - firstPage)
   lineBottomY = axisY - 3
   lineTopY = lineBottomY - (lineHeight - 1)
   for page in range(firstPage, lastPage + 1):
      if simpleDic.has_key(page):
         spellingsCount = len(simpleDic[page])
         for i in range(spellingsCount):
            spelling = simpleDic[page][i]
            colour = colours[spellings.index(spelling)]
            # Establishing the horizontal position of the line is a
            # bit fiddly.  If this is the only entry for this page
            # number, then draw the line at the centre of the area
            # representing the page.  If there are more, though, we
            # want the whole block centred and sorted for colour.
            # Therefore, draw the line left of centre if this entry
            # is in the first half of the list, and right if it's in
            # the second half.
            centreX = int(axisLeftX + \
                          ((page - firstPage) * pixelsPerPage))
            displacement = i - (spellingsCount / 2)
            lineX = centreX + displacement
            draw.line([(lineX, lineTopY), (lineX, lineBottomY)],
                      fill=colour)
