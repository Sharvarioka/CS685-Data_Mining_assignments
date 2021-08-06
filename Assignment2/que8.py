import csv
import json
import ast
from collections import defaultdict
import networkx as nx
data=[]
# data_id_rev={}
art_cat_dict={}
cat_q1={}
cat_q2={}
cat_q1_shortest={}
cat_q2_shortest={}
result=[]
new_data=[]
edges=[]
path_explored={}

edge_open= open('edges.csv')
csv_read_edge = csv.reader(edge_open)
list_csv_read_edge=list(csv_read_edge)
# print(list_csv_read_edge)

length=len(list_csv_read_edge)
G = nx.DiGraph()
for i in range(1,length):
   G.add_edge(list_csv_read_edge[i][0],list_csv_read_edge[i][1])


file = open('paths_finished.tsv')
tsv_read = csv.reader(file, delimiter='\t')
list_tsv_finished_paths=list(tsv_read)

# print(list_tsv_finished_paths[0])
art_cat_file = open('article-categories.csv')
art_cat_csv= csv.reader(art_cat_file)
art_cat_list=list(art_cat_csv)


cat_file = open('category-ids.csv')
cat_csv= csv.reader(cat_file)
cat_list=list(cat_csv)

for i in range(1,len(cat_list)):
	cat_q1[cat_list[i][1]]=0
	cat_q2[cat_list[i][1]]=0

for i in range(1,len(cat_list)):
	cat_q1_shortest[cat_list[i][1]]=0
	cat_q2_shortest[cat_list[i][1]]=0


# article id [category ids related]
for i in range(1,len(art_cat_list)):
	art_cat_dict[art_cat_list[i][0]]=ast.literal_eval(art_cat_list[i][1]) 


#   article name,  article id
with open('articles-ids.json') as json_file:
	data_id = json.load(json_file)
# print(data_id)


for i in range(0,len(list_tsv_finished_paths)):
	if i<16:
		continue
	else:
		if list_tsv_finished_paths[i][3]=='Bird;Wikipedia_Text_of_the_GNU_Free_Documentation_License':
			continue
		else:
			data.append(list_tsv_finished_paths[i][3])

for i in range(0,len(data)):
	cat_no_angular=[]
	array_no_angular=data[i].split(';')
	for j in range(0,len(array_no_angular)):
		if array_no_angular[j] !='<':
			cat_no_angular.append(array_no_angular[j])
		else:
			cat_no_angular.pop()
	new_data.append(cat_no_angular)


for i in range(0,len(new_data)):
	# print(new_data[i])
	cat_array=[]
	
	cat_array_shortest=[]
	
	
	num=len(new_data[i])
	if num>1:
		human_path=num-1
		source=data_id[new_data[i][0]]
		target=data_id[new_data[i][human_path]]
		path=nx.shortest_path(G,source,target)
		
		for article in new_data[i]:
			for j in art_cat_dict[data_id[article]]:
				cat_array.append(j)

		for m in list(set(cat_array)):
			cat_q1[m]+=1 

		for m in cat_array:
			cat_q2[m]+=1
		
		for article_id in path:
			for j in art_cat_dict[article_id]:
				cat_array_shortest.append(j)

		for s in list(set(cat_array_shortest)):
			cat_q1_shortest[s]+=1

		for s in cat_array_shortest:
			cat_q2_shortest[s]+=1
		
for cat in cat_q2.keys():
	result.append({'Category_ID':cat,'Number_of_human_paths_traversed':cat_q1[cat],'Number_of_human_times_traversed':cat_q2[cat],'Number_of_shortest_paths_traversed':cat_q1_shortest[cat],'Number_of_shortest_times_traversed':cat_q2_shortest[cat]})

try:
	with open("category-paths.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['Category_ID','Number_of_human_paths_traversed', 'Number_of_human_times_traversed','Number_of_shortest_paths_traversed', 'Number_of_shortest_times_traversed'])
		writer.writeheader()
		writer.writerows(result)
except IOError:
    print("I/O error")

				


