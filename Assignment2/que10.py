import csv
import json
import ast

source_dest={}
source_dest_fin={}
art_cat_dict={}
data_id_rev={}
cat_dict={}
final_cat_output={}
cat_dict_rev={}
result=[]

# reading the unfinished paths 
path_un= open('paths_unfinished.tsv')
path_unfinished = csv.reader(path_un, delimiter='\t')
list_path_unfinished=list(path_unfinished)

for i in range(0,len(list_path_unfinished)):
	if i<17:
		continue
	else:
		src=''
		dest=''
		if list_path_unfinished[i][3].split(';')[0]=='Long_peper' : 
			src='Long_pepper'
		if list_path_unfinished[i][4]=='Long_peper':
			dest='Long_pepper'


		if list_path_unfinished[i][3].split(';')[0]=='Adolph_Hitler' : 
			src='Adolf_Hitler'
		if list_path_unfinished[i][4]=='Adolph_Hitler':
			dest='Adolf_Hitler'


		if list_path_unfinished[i][3].split(';')[0]=='Podcast' : 
			src='Podcasting'
		if list_path_unfinished[i][4]=='Podcast':
			dest='Podcasting'

		if list_path_unfinished[i][3].split(';')[0]=='Charlottes_web': 
			src='Charlotte%27s_Web'
		if list_path_unfinished[i][4]=='Charlottes_web':
			dest='Charlotte%27s_Web'


		if list_path_unfinished[i][3].split(';')[0]=='Macedonia': 
			src='Macedon'
		if list_path_unfinished[i][4]=='Macedonia':
			dest='Macedon'

		if list_path_unfinished[i][3].split(';')[0]=='Kashmir': 
			src='Kashmir_region'
		if list_path_unfinished[i][4]=='Kashmir':
			dest='Kashmir_region'

		if list_path_unfinished[i][3].split(';')[0]=='Bogota': 
			src='Bogot%C3%A1'
		if list_path_unfinished[i][4]=='Bogota':
			dest='Bogot%C3%A1'

		if list_path_unfinished[i][3].split(';')[0]=='rss': 
			src='RSS_%28file_format%29'
		if list_path_unfinished[i][4]=='rss':
			dest='RSS_%28file_format%29'

		# print(dest or list_path_unfinished[i][4])

		# print((src or list_path_unfinished[i][3].split(';')[0])+'/'+(dest or list_path_unfinished[i][4]))

		source_dest[(src or list_path_unfinished[i][3].split(';')[0])+'/'+(dest or list_path_unfinished[i][4])+'/'+str(i)]=0

# print(source_dest)

# reading the finished paths 
path_fin= open('paths_finished.tsv')
path_finished = csv.reader(path_fin, delimiter='\t')
list_path_finished=list(path_finished)

for i in range(0,len(list_path_finished)):
	if i<16:
		continue
	else:
		split_char = list_path_finished[i][3].split(';')
		if len(split_char)>1:
			source_dest_fin[split_char[0]+'/'+split_char[len(split_char)-1]+'/'+str(i)]=0

# reading the article categories file
art_cat_file = open('article-categories.csv')
art_cat_csv= csv.reader(art_cat_file)
art_cat_list=list(art_cat_csv)

for i in range(1,len(art_cat_list)):
	art_cat_dict[art_cat_list[i][0]]=ast.literal_eval(art_cat_list[i][1])

with open('articles-ids.json') as json_file:
    data_id = json.load(json_file)


# reading the categories - catid file
cat_file = open('category-ids.csv')
cat_csv= csv.reader(cat_file)
cat_list=list(cat_csv)

for i in range(1,len(cat_list)):
	cat_dict[cat_list[i][1]]=cat_list[i][0]

for i in range(1,len(cat_list)):
	cat_dict_rev[cat_list[i][0]]=cat_list[i][1]

		
# print(source_dest)
def getCategories(article):
	temp=[]
	if article in data_id.keys():

		cats = art_cat_dict[data_id[article]]
		

		for c_id in cats:
			cat_name=cat_dict[c_id]
			for value in cat_dict.values():
				if value in cat_name:
					temp.append(cat_dict_rev[value])
	else:
		pass
		# print(article)
		# temp.append('C0001')
	return temp


# getting list of list for category for every path for unifinished
for key,value in source_dest.items():
	#article_array=[]
	arr_src=[]
	arr_dest=[]
	count=0
	source_dest_split=key.split('/')
	category_id_array=[]

	category_source=list(set(getCategories(source_dest_split[0])))
	category_destination=list(set(getCategories(source_dest_split[1])))
		
	unique_combinations = [[x,y] for x in category_source for y in category_destination] 
	
	for entry in unique_combinations:
		key = str(entry[0])+'/'+str(entry[1])
		if key not in final_cat_output.keys():
			final_cat_output[key] = {"unfin":1, "fin": 0}
		else:
			temp = final_cat_output[key]['unfin']
			final_cat_output[key] = {"unfin": temp+1, "fin": 0}
	

# getting list of list for category for every path for finished
for key,value in source_dest_fin.items():
	#article_array=[]
	count=0
	source_dest_split=key.split('/')
	category_id_array=[]

	category_source=list(set(getCategories(source_dest_split[0])))
	category_destination=list(set(getCategories(source_dest_split[1])))

	

	unique_combinations = [[x,y] for x in category_source for y in category_destination] 
  	
	for entry in unique_combinations:
		key = str(entry[0])+'/'+str(entry[1])
		if key not in final_cat_output.keys():
			final_cat_output[key] = {"fin":1, "unfin": 0}
		else:
			temp = final_cat_output[key]['fin']
			final_cat_output[key] = {"fin": temp+1, "unfin": final_cat_output[key]['unfin']}

# sum_fin=sum([value['fin'] for value in final_cat_output.values()])
# sum_unfin=sum([value['unfin'] for value in final_cat_output.values()])
for cats, path in sorted(final_cat_output.items()):
	result.append({
		'From_Category':cats.split('/')[0],
		'To_Category':cats.split('/')[1], 
		'Percentage_of_finished_paths':(path['fin']*100)/(path['fin']+path['unfin']),
		'Percentage_of_unfinished_paths':(path['unfin']*100)/(path['fin']+path['unfin'])
		})
	
try:
	with open("category-pairs.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=[
			'From_Category',
			'To_Category',
			'Percentage_of_finished_paths',
			'Percentage_of_unfinished_paths'
			])
		writer.writeheader()
		writer.writerows(result)
except IOError:
    print("I/O error")


			
