import json
import csv
data=[]
sorted_alpha = []

r_filenameTSV = open('categories.tsv')
tsv_read = csv.reader(r_filenameTSV, delimiter='\t')
list_tsv_read=list(tsv_read)

for i in range(0,len(list_tsv_read)):
	if i<13:
		continue
	else:
		data.append(list_tsv_read[i][1])

array1 = []
array2 = []
array3 = []
array4 = []
array5 = []
array6 = []
array=[]

for cat in data:
	temp = cat.split('.')
	for i in range(0, len(temp)):
		newCat = '.'.join(temp[0:i+1])
		newCatCount = '.'.join(temp[0:i+1]).count('.')
		if newCatCount == 1:
			array1.append(newCat)
		elif newCatCount == 2:
			array2.append(newCat)
		elif newCatCount == 3:
			array3.append(newCat)
		elif newCatCount == 4:
			array4.append(newCat)
		elif newCatCount == 5:
			array5.append(newCat)
		elif newCatCount == 6:
			array6.append(newCat)
		else:
			array.append(newCat)
		
final= sorted(list(set(array)))+sorted(list(set(array1)))+sorted(list(set(array2)))+sorted(list(set(array3)))+sorted(list(set(array4)))+sorted(list(set(array5)))
counter=1

for i in final:
	sorted_alpha.append({'Category_Name': i, 'Category_ID': 'C'+str(counter).zfill(4)})
	counter+=1

try:
	with open("category-ids.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['Category_Name', 'Category_ID'])
		writer.writeheader()
		writer.writerows(sorted_alpha)
except IOError:
    print("I/O error")
