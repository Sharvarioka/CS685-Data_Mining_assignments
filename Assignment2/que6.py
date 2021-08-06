import csv
import json

data=[]
all_lines=[]
# data_id_rev={}
final=[]
final_wbl=[]

file = open('paths_finished.tsv')
tsv_read = csv.reader(file, delimiter='\t')
list_tsv_finished_paths=list(tsv_read)

with open('articles-ids.json') as json_file:
    data_id = json.load(json_file)
# print(data_id)
with open('shortest-path-distance-matrix.txt') as f:
    for _ in range(17):
        next(f)
    for line in f:
        all_lines.append(line)
# print(all_lines)
'''
for key,value in data_id.items():
	variable=data_id[key]
	data_id_rev[variable]=key
# print(data_id_rev)
'''
for i in range(0,len(list_tsv_finished_paths)):
	if i<16:
		continue
	else:
		data.append(list_tsv_finished_paths[i][3])
# print(data)

for i in range(0,len(data)):
	back_link_count=0
	array_split=data[i].split(';')
	# print(array_split)

	num=len(data[i].split(';'))
	human_path=num-1
	shortest=all_lines[(int(data_id[array_split[0]].lstrip('A')))-1][(int(data_id[array_split[human_path]].lstrip('A')))-1]
	
	if num==1 or data_id[array_split[0]]==data_id[array_split[human_path]] or shortest=="_":
		continue
	ratio=human_path/int(shortest)

	back_link_count=array_split.count('<')

	
	human_path_wbl=num-1-2*back_link_count
	# print(human_path)
	
	
	
	ratio_wbl=human_path_wbl/int(shortest)

	# print(ratio)
	final.append({'Human_Path_Length': human_path,'Shortest_Path_Length': shortest,'Ratio': ratio})
	final_wbl.append({'Human_Path_Length': human_path_wbl,'Shortest_Path_Length': shortest,'Ratio': ratio_wbl})

try:
	with open("finished-paths-back.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['Human_Path_Length','Shortest_Path_Length','Ratio'])
		writer.writeheader()
		writer.writerows(final)
except IOError:
    print("I/O error")

try:
	with open("finished-paths-no-back.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['Human_Path_Length','Shortest_Path_Length','Ratio'])
		writer.writeheader()
		writer.writerows(final_wbl)
except IOError:
    print("I/O error")
