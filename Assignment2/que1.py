import pandas as pd
import csv
from itertools import zip_longest 
import json


data=[]
data_array=[]
data_dict={}
data_array_record=[]
# r_file = 'articles.tsv'
# w_file = 'article-ids.csv'

r_filenameTSV = open('articles.tsv')
# w_filenameCSV = open('article-ids.csv')

tsv_read = csv.reader(r_filenameTSV, delimiter='\t')
list_tsv_read=list(tsv_read)
# print(list(tsv_read))
for i in range(0,len(list_tsv_read)):
	if i<12:
		continue
	else:
		data.append(list_tsv_read[i][0])

# print(sorted(data))
for (i,record) in zip(range(1,4605),data):
	data_dict[record]='A'+str(i).zfill(4)
	data_array.append({'Article_Name':record,'Article_ID':'A'+str(i).zfill(4)})

try:
	with open("article-ids.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['Article_Name','Article_ID'])
		writer.writeheader()
		writer.writerows(data_array)
except IOError:
    print("I/O error")
with open('articles-ids.json', 'w') as fp:
    json.dump(data_dict, fp)
