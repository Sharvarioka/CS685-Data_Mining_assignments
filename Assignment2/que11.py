import csv
import json
import ast


source_dest_fin={}
art_cat_dict={}
cat_dict={}
final_cat_output={}
data=[]
result=[]

all_lines=[]
cat_dict_rev={}

path_fin= open('paths_finished.tsv')
path_finished = csv.reader(path_fin, delimiter='\t')
list_path_finished=list(path_finished)

with open('articles-ids.json') as json_file:
    data_id = json.load(json_file)


with open('shortest-path-distance-matrix.txt') as f:
    for _ in range(17):
        next(f)
    for line in f:
        all_lines.append(line)

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

for i in range(1,len(cat_list)):
	cat_dict[cat_list[i][1]]=cat_list[i][0]

for i in range(1,len(cat_list)):
	cat_dict_rev[cat_list[i][0]]=cat_list[i][1]




for i in range(0,len(list_path_finished)):
	if i<16:
		continue
	else:
		data.append(list_path_finished[i][3])


		
# (source_dest)
def getCategories(article):
	temp=[]
	if article in data_id.keys():

		cats = art_cat_dict[data_id[article]]
		for c_id in cats:
			cat_name=cat_dict[c_id]
			for value in cat_dict.values():
				if value in cat_name:
					temp.append(cat_dict_rev[value])

	
	return temp

# print(data)
for i in range(0,len(data)):
	cat_no_angular=[]
	array_no_angular=data[i].split(';')
	num=len(data[i].split(';'))
	human_path=num-1
	shortest=all_lines[(int(data_id[array_no_angular[0]].lstrip('A')))-1][(int(data_id[array_no_angular[human_path]].lstrip('A')))-1]
	
	if num==1 or data_id[array_no_angular[0]]==data_id[array_no_angular[human_path]] or shortest=="_":
		continue

	back_link_count=array_no_angular.count('<')

	
	human_path_wbl=num-1-2*back_link_count
	# ratio_wbl=human_path_wbl/int(shortest)


# for i in range(0,len(data)):
	count=0
	count_shortest=0	
	category_id_shortest=[]
	category_id_array=[]
	# article_array=data[i]

	category_source=getCategories(array_no_angular[0])
	category_destination=getCategories(array_no_angular[-1])
	unique_combinations = [[x,y] for x in category_source for y in category_destination]

	for entry in unique_combinations:
		key = str(entry[0])+'/'+str(entry[1])
		human=0
		short=0
		# for ele in entry:
		# 	human+=category_id_array.count(ele)
		# 	short+=category_id_shortest.count(ele)
		if key not in final_cat_output.keys():
			final_cat_output[key] = {"human": human_path_wbl, "short": int(shortest)}

		else:
			temp_human = final_cat_output[key]['human']
			temp_short = final_cat_output[key]['short']
			final_cat_output[key] = {"human": temp_human+human_path_wbl, "short": temp_short+int(shortest)}

# print(final_cat_output)
for cats, path in sorted(final_cat_output.items()):
	result.append({
		'From_Category':cats.split('/')[0],
		'To_Category':cats.split('/')[1], 
		'Ratio_of_human_to_shortest':path['human']/int(path['short'])
		})
	
try:
	with open("category-ratios.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=[
			'From_Category',
			'To_Category',
			'Ratio_of_human_to_shortest'
			])
		writer.writeheader()
		writer.writerows(result)
except IOError:
    print("I/O error")


			
