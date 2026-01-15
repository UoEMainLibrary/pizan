import cPickle, hap, graphics, ImageFont, Image, ImageDraw

roman = ImageFont.truetype('fonts/luxisr.ttf', 12)
italic = ImageFont.truetype('fonts/luxisri.ttf', 12)
bold = ImageFont.truetype('fonts/luxisb.ttf', 12)
fonts = (roman, italic, bold)

doulourUnwanted = ['doul\xe7our', 'doulceur']

input = [
		  ((900, 250), True, fonts, (0, 'end'), 'blasmer', []),
		  ((900, 250), False, fonts, (0, 'end'), 'blasmer', []),
		  ((900, 250), True, fonts, (45, 70), 'doulour',
		  															doulourUnwanted),
		  ((900, 250), False, fonts, (45, 70), 'doulour', 
		  															doulourUnwanted),
		  ((900, 250), True, fonts, (10, 'end'), 'doulour', 
		  															doulourUnwanted),
		  ((900, 250), False, fonts, (10, 'end'), 'doulour', 
		  															doulourUnwanted),
		  ((900, 250), True, fonts, (12, 786), 'doulour', 
		  															doulourUnwanted),
		  ((900, 250), True, fonts, (145, 147), 'doulour', 
		  															doulourUnwanted),
		  ((900, 250), True, fonts, (0, 'end'), 'doulour', 
		  															doulourUnwanted)
		  ]

def batchTest(filename='test'):
	counter = 1
	for paramSet in input:
		fullFilename = filename + (str(counter) + '.png')
		graph = test(paramSet, fullFilename)
		counter += 1

def test(paramSet, outputFilename):
	(imageDimensions,
	 separateRectoVerso,
	 fonts,
	 pageRange,
	 pickleFilename,
	 unwanted) = paramSet
	graph = Image.new('RGB', imageDimensions, 'white')
	draw = ImageDraw.Draw(graph)
	axisData = graphics.planAxis(imageDimensions,
										  separateRectoVerso,
										  fonts,
										  pageRange)
	graphics.drawAxis(draw, axisData, fonts)
	pickleFilename = 'hapSets/' + pickleFilename + 'HapSet.pkl'
	pickleFile = open(pickleFilename, 'r')
	hapSet = cPickle.load(pickleFile)
	pickleFile.close()
	(dic, keys, spellings) = hap.sortCitations(hapSet, unwanted)
	simpleDic = graphics.simplifyDic(dic, separateRectoVerso)
	graphics.drawLines(draw, axisData, simpleDic, spellings)
	graph.save(outputFilename, 'PNG')