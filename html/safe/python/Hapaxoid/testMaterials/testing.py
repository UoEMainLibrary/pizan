import cases, codes, relatedness

def testCases(outputFilename):
	outputFile = open(outputFilename, 'w')
	outputFile.write('casePairs:\n')
	for pair in cases.casePairs:
		outputFile.write(pair[0] + ' ' + pair[1] + '\n')
	outputFile.write('\nmyUpper:\n')
	for letter in 'abcdefghijklmnopqrstuvwxyz':
		outputFile.write(cases.myUpper(letter) + ' ')
	for pair in casePairs:
		outputFile.write(cases.myUpper(pair[1]) + ' ')
	outputFile.write('\n\nmyLower:\n')
	for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
		outputFile.write(cases.myLower(letter) + ' ')
	for pair in casePairs:
		outputFile.write(cases.myLower(pair[0]) + ' ')
	outputFile.close()
	print 'Done.'

def testConforms(dataFilename):
	dataFile = open(dataFilename, 'r')
	line = dataFile.readline()
	while line != '':
		tokens = line.split()
		if len(tokens) > 0 and not codes.conforms(tokens[0]):
			print 'Test failed: ' + tokens[0] + " doesn't conform."
			return
		line = dataFile.readline()
	dataFile.close()
	print 'Test successful: all codes in ' + dataFilename + \
			' conform.'

def testSteps(testSetFilename):
	file = open(testSetFilename, 'r')
	line = file.readline()
	while line != '':
		tokens = line.split()
		word1 = tokens[0]
		word2 = tokens[1]
		expectedSteps = int(tokens[2])
		stepCount = relatedness.steps(word1, word2)
		if stepCount != expectedSteps:
			print 'Error: ' + str(stepCount) + \
					' steps estimated between ' + word1 + ' and ' + \
					word2 + ' (' + str(expectedSteps) + ' expected).'
		line = file.readline()
	file.close()