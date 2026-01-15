import hap, cPickle

'''
dataFilename
initialMatches
finalMatches
minLength
minOccurrences
maxDifferences
networked
'''

paramSets = [('../t.txt', 3, 1, 5, 3, 2, False, 'haps.pkl'),
				 ('../t.txt', 3, 1, 5, 3, 2, True, 'hapsNetworked.pkl'),
				 ('../t.txt', 3, 1, 5, 3, 3, False, 'haps3diffs.pkl'),
				 ('../t.txt', 3, 1, 4, 3, 2, False, 'haps4length.pkl'),
				 ('../t.txt', 2, 1, 5, 3, 2, False, 'haps2initial.pkl'),
				 ('../t.txt', 3, 0, 5, 3, 2, False, 'haps0final.pkl'),
				 ('../t.txt', 3, 1, 5, 2, 2, False, 'haps2occurrences.pkl'),
				 ('../t.txt', 1, 0, 4, 5, 2, False, 'haps10452.pkl'),
				 ('../t.txt', 1, 0, 4, 5, 2, True, 'haps10452networked.pkl')]

def run():
	for paramSet in paramSets:
		getHaps(paramSet)

def getHaps(params):
	haps = hap.listHaps(params[0],
							  params[1],
							  params[2],
							  params[3],
							  params[4],
							  params[5],
							  params[6])
	file = open(params[7], 'w')
	cPickle.dump(haps, file)
	file.close()