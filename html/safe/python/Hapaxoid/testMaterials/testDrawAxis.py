import graphics, ImageFont, Image, ImageDraw

roman = ImageFont.truetype('fonts/luxisr.ttf', 12)
italic = ImageFont.truetype('fonts/luxisri.ttf', 12)
bold = ImageFont.truetype('fonts/luxisb.ttf', 12)
fonts = (roman, italic, bold)

parameters = [((900, 250), True, fonts, (0, 'end')),
				 ((900, 250), False, fonts, (0, 'end')),
				 ((900, 250), True, fonts, (45, 70)),
				 ((900, 250), True, fonts, (45, 69)),
				 ((900, 250), True, fonts, (45, 68)),
				 ((900, 250), False, fonts, (45, 68)),
				 ((900, 250), True, fonts, (10, 'end')),
				 ((900, 250), False, fonts, (10, 'end')),
				 ((900, 250), True, fonts, (12, 786)),
				 ((900, 250), True, fonts, (145, 147))]

def test():
	counter = 1
	for (imageDimensions,
		  separateRectoVerso,
		  fonts,
		  pageRange) in parameters:
		graph = Image.new('RGB', imageDimensions, 'white')
		draw = ImageDraw.Draw(graph)
		axisData = graphics.planAxis(imageDimensions,
											  separateRectoVerso,
											  fonts,
											  pageRange)
		graphics.drawAxis(draw, axisData, fonts)
		filename = 'test' + str(counter) + '.png'
		graph.save(filename, 'PNG')
		counter += 1