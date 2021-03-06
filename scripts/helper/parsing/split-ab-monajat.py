import os, re

in_file = '../abdulbaha-monajat.txt'

count = 1

ar = [0,2,6,7,8,13,14,15,19,22,23,30,31,32,44,53,56,58,59,60,61,62,63,67,68,
     69,74,76,77,78,79,80,81,82,83,85,86,87,88,89,90,91,92,93,94,95,96,100,105,
	 112,114,115,116,117,118,122,123,125,131,138,139,140,141,144,160,172,177,
	 179,180,182,183,184,186,189,191,197,198,204,208,209,210,212,213,214,215,
	 216,217,218,219,220,221,222,223,224,225,226,227,228,231,232,236,238,243,
	 244,247,258,261,265,270,271,273,274,281,282,283,285,287,288,289,291,292,
	 296,305,314,315,316,319,321,322,323,324,325,328,330,339,341,342,343,344,
	 345,346,347,349,350,352,353,357,360,364,374,376,379,380,384,386,387,388,
	 389,391,393,394,400,408,413,415,418,419,421,429,433,443,445,449,455,458]

with open(in_file, 'r') as f:
	content = f.read()
	x = re.split("\(\d*\)", str(content))
	x.pop(0)
	print(len(x))

output = os.makedirs("output")

for i in x:
	if count in ar:
		language = 'ar'
	else:
		language = 'fa'
	# os.makedirs(os.path.dirname('output'), exist_ok=True)
	with open('output/abdulbaha-monajat-{}-{}.txt'.format(count, language), 'w') as out_file:
		out_file.write(i)
		count += 1
