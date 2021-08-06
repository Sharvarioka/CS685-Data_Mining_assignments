###for que 9

import csv
import json
import ast
import networkx as nx

# declarations

data=[]
result=[]
new_data=[]
cat_dict={}
art_cat_dict={}
cat_q1_unique_article={}
cat_q2_repeat_article={}
cat_q1_shortest={}
cat_q2_shortest={}
cat_dict_rev={}
cat_substring={}
marked={}

edge_open= open('edges.csv')
csv_read_edge = csv.reader(edge_open)
list_csv_read_edge=list(csv_read_edge)
# print(list_csv_read_edge)
length=len(list_csv_read_edge)
G = nx.DiGraph()
for i in range(1,length):
   G.add_edge(list_csv_read_edge[i][0],list_csv_read_edge[i][1])


# reading the paths file
file_read = open('paths_finished.tsv')
tsv_read = csv.reader(file_read, delimiter='\t')
list_tsv_finished_paths=list(tsv_read)

# removing first 16 lines from paths list
for i in range(0,len(list_tsv_finished_paths)):
	if i<16:
		continue
	else:
		if list_tsv_finished_paths[i][3]=='Bird;Wikipedia_Text_of_the_GNU_Free_Documentation_License':
			continue
		else:
			data.append(list_tsv_finished_paths[i][3])


# reading the article categories file
art_cat_file = open('article-categories.csv')
art_cat_csv= csv.reader(art_cat_file)
art_cat_list=list(art_cat_csv)

for i in range(1,len(art_cat_list)):
	art_cat_dict[art_cat_list[i][0]]=ast.literal_eval(art_cat_list[i][1]) 

# reading the categories - catid file
cat_file = open('category-ids.csv')
cat_csv= csv.reader(cat_file)
cat_list=list(cat_csv)


# cat_dict (id: name)
for i in range(1,len(cat_list)):
	cat_dict[cat_list[i][1]]=cat_list[i][0]
# print(cat_dict)

# cat_dict_rev (name:id)
for i in range(1,len(cat_list)):
	cat_dict_rev[cat_list[i][0]]=cat_list[i][1]

# reading the id - articles file
with open('articles-ids.json') as json_file:
    data_id = json.load(json_file)
for i in range(1,len(cat_list)):
	marked[cat_list[i][1]]=0
# print(marked)
# initializing result dicts
for i in range(1,len(cat_list)):
	cat_q1_unique_article[cat_list[i][1]]=0
	cat_q2_repeat_article[cat_list[i][1]]=0

for i in range(1,len(cat_list)):
	cat_q1_shortest[cat_list[i][1]]=0
	cat_q2_shortest[cat_list[i][1]]=0

# getting list of list for  article without < for every path 
for i in range(0,len(data)):
	article_array=[]
	# article_array_shortest=[]
	all_articles_in_path=data[i].split(';')
	# category_id_array=[]
	# category_id_shortest=[]

	
	for article in all_articles_in_path:
		if article !='<':
			article_array.append(article)
		else:
			article_array.pop()
	new_data.append(article_array)



for i in range(0,len(new_data)):
	arr=[]
	arr_shortest=[]	
	category_id_array=[]
	category_id_shortest=[]
	article_array=new_data[i]
	num=len(article_array)
	if num>1:
		human_path=num-1

		source=data_id[article_array[0]]
		target=data_id[article_array[human_path]]
		path=nx.shortest_path(G,source=source,target=target)
		# print(path)


		for article in article_array:
			for j in art_cat_dict[data_id[article]]:
				category_id_array.append(j)
		# print("cat id array in human path")	
		# print(category_id_array)
		
		for c_id in category_id_array:
			cat_name=cat_dict[c_id]           
			for value in cat_dict.values():
				if value in cat_name:
					cat_q2_repeat_article[cat_dict_rev[value]]+=1 
		


		for c_id in list(set(category_id_array)):
			cat_name=cat_dict[c_id]
		
			for value in cat_dict.values():
				if value in cat_name:
					arr.append(value)
					
		for temp in list(set(arr)):
			cat_q1_unique_article[cat_dict_rev[temp]]+=1



			
		for article_id in path:
			for j in art_cat_dict[article_id]:
					category_id_shortest.append(j)
			
		
		for c_id in category_id_shortest:
			cat_name=cat_dict[c_id]
			for value in cat_dict.values():
				if value in cat_name:
					cat_q2_shortest[cat_dict_rev[value]]+=1 
		
		for c_id in list(set(category_id_shortest)):
			cat_name=cat_dict[c_id]
			for value in cat_dict.values():
				if value in cat_name:
					arr_shortest.append(value)

		for temp in list(set(arr_shortest)):
			cat_q1_shortest[cat_dict_rev[temp]]+=1	
					 			
			
for cat in cat_q2_repeat_article.keys():
	result.append({'Category_ID':cat,
		'Number_of_human_paths_traversed':cat_q1_unique_article[cat],
		'Number_of_human_times_traversed':cat_q2_repeat_article[cat],
		'Number_of_shortest_paths_traversed':cat_q1_shortest[cat],
		'Number_of_shortest_times_traversed':cat_q2_shortest[cat]})

try:
	with open("category-subtree-paths.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['Category_ID',
			'Number_of_human_paths_traversed', 
			'Number_of_human_times_traversed',
			'Number_of_shortest_paths_traversed',
			'Number_of_shortest_times_traversed'
			])
		writer.writeheader()
		writer.writerows(result)
except IOError:
    print("I/O error")


    			
