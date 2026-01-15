import graphics, hap, cPickle

doulourUnwanted = ['doul\xe7our', 'doulceur']
appUnwanted = ['appellent', 'appelloient', 'appelloit',
					'appellerent', 'appetit']

input = [
			('blasmer', [], '01', False, 900, True, (0, 'end')),
			('doulour', doulourUnwanted, '02', False, 900, True,
																			(0, 'end')),
			('doulour', [], '03', False, 900, True, (0, 'end')),
			('acquist', [], '04', False, 900, True, (0, 'end')),
			('acquistNetworked', [], '05', True, 900, True, (0, 'end')),
			('doulour', [], '06', False, 500, True, (0, 'end')),
			('doulour', [], '07', False, 250, True, (0, 'end')),
			('doulour', [], '08', False, 900, False, (0, 'end')),
			('doulour', doulourUnwanted, '09', False, 900, True,
																			(10, 200)),
			('apportoientNetworked', appUnwanted, '10', True, 900, True,
																			(0, 'end'))
		  ]

def batchTest():
	for params in input:
		test(params)

def test(params):
	(pickleFilename,
	 unwanted,
	 outputFilename,
	 networked,
	 width,
	 separateRectoVerso,
	 pageRange) = params
	pickleFilename = 'hapSets/' + pickleFilename + 'HapSet.pkl'
	pickleFile = open(pickleFilename, 'r')
	hapSet = cPickle.load(pickleFile)
	pickleFile.close()
	(dic, keys, spellings) = hap.sortCitations(hapSet, unwanted)
	graphics.makeGraph(dic, keys, spellings, outputFilename,
							 networked, width, separateRectoVerso,
							 pageRange)