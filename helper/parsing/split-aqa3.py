import re

in_file = 'aqa3.txt'

count = 1


fa = [68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,
      91,92,93,94,95,96,97,98,99,100,101,102,103,104,122,131,132,133, 137,
      140,143,146,147,181,201,217,218,219,220,221,232,242,243,244,245,247,
      248,250,254,259,272,278,279,280,281,282,283,284,285,286,287,288,289,
      290,291,292,293,294,295,296,297,298,308,309,312,322,328,335,336,337,
      350,351,357,360,367,368,369,370,371,372,373,374,376,377,378,379,380,
      381,382,384,386,388,393,395,397,398,399,400,401,403,405,406,407,408,
      409,410,411,412,413,414,416,423,427,429,430,431,433,434,447,448,449,
      450,451,455,466,473,475,478,481,484,489,504,506,508,510,511,512,514,
      515,517,518]

with open(in_file, 'r') as f:
	content = f.read()
	x = re.split("\(\d*\)", str(content))
	x.pop(0)

for i in x:
	if count in fa:
		lanuguage = 'fa'
	else:
		lanuguage = 'ar'
	out_file = open('bahaullah-aqa3-{}-{}.txt'.format(count, lanuguage), 'w')
	out_file.write(i)
	count += 1
f.close()
    