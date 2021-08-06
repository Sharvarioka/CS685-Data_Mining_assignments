import json
import csv
data_article=[]
data_categoty=[]
sorted_alpha = []
result=[]
data=[]

r_filenameTSV = open('categories.tsv')
tsv_read = csv.reader(r_filenameTSV, delimiter='\t')
list_tsv_read=list(tsv_read)

article_open= open('article-ids.csv')
csv_read_article = csv.reader(article_open)
list_csv_read_article=list(csv_read_article)

category_open = open('category-ids.csv')
csv_read_category = csv.reader(category_open, delimiter=',')
list_csv_read_category=list(csv_read_category)
# print(list_csv_read_article)
# print(list_tsv_read)
for i in range(0,len(list_tsv_read)):
	if i<13:
		continue
	else:
		data.append(list_tsv_read[i])


for i in range(1,len(list_csv_read_article)):
	article_name=list_csv_read_article[i][0]   
	list_category_id=[]
	for j in range(0,len(data)):
		if article_name==data[j][0]:
			category_name=data[j][1]  #subject.Countries
			for k in range(0,len(list_csv_read_category)):
				if category_name==list_csv_read_category[k][0]:
					list_category_id.append(list_csv_read_category[k][1])
	# result[list_csv_read_article[i][0]]=list_category_id
	if len(list_category_id)==0:
		result.append({'Article_ID':list_csv_read_article[i][1], 'Category_ID':['C0001']})
	else:	
		result.append({'Article_ID':list_csv_read_article[i][1], 'Category_ID':list_category_id})
# print(result)
try:
	with open("article-categories.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['Article_ID', 'Category_ID'])
		writer.writeheader()
		writer.writerows(result)
except IOError:
    print("I/O error")
