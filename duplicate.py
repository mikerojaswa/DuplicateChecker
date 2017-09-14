inputfile = open('{NAME_OF_FILE_HERE}')
emails = inputfile.readlines()
myfuckingset = set()
counter = 0
linecounter = 0
print("Duplicates:")
for line in emails:
	linecounter = linecounter + 1
	if line not in myfuckingset:
		myfuckingset.add(line)
	else:
		print(line)
		counter = counter + 1
print("Number of duplicates:")
print(counter)

	
