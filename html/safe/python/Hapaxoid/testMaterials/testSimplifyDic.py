import cPickle, hap, graphics

def run():
	process('hapSets/blasmerHapSet.pkl', True)
	process('hapSets/blasmerHapSet.pkl', False)
	doulourUnwanted = ['doul\xe7our', 'doulceur']
	process('hapSets/doulourHapSet.pkl', True, doulourUnwanted)
	process('hapSets/doulourHapSet.pkl', False, doulourUnwanted)

def process(filename, separateRectoVerso, unwanted=[]):
	file = open(filename, 'r')
	hapSet = cPickle.load(file)
	file.close()
	dic = hap.sortCitations(hapSet, unwanted)[0]
	print graphics.simplifyDic(dic, separateRectoVerso)