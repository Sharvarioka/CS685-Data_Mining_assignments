import csv
all_lines=[]
edge_dict={}
article_id={}

for i in range(1,4605):
	article_id[str(i-1)]='A'+str(i).zfill(4)
 
# print(article_id)

with open('shortest-path-distance-matrix.txt') as f:
    for _ in range(17):
        next(f)
    for line in f:
        all_lines.append(line)
# print(len(all_lines))
for row in range(0,len(all_lines)):
	edges=[]
	for col in range(0,len(all_lines)):
		if all_lines[row][col]=='1':
			edges.append(article_id[str(col)])
	edge_dict[article_id[str(row)]]=edges

# print(edge_dict)
edge_list=[]
for k,v in edge_dict.items():
	edge_array=[]
	for article in v:
		edge_array.append(k)
		edge_array.append(article)
		edge_list.append({'From_ArticleID':edge_array[0],'To_ArticleID':edge_array[1]})
		edge_array=[]
# print(edge_list)


try:
	with open("edges.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['From_ArticleID','To_ArticleID'])
		writer.writeheader()
		writer.writerows(edge_list)
except IOError:
    print("I/O error")


