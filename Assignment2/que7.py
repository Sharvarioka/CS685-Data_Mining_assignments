import csv
final=[]
final_array=[]
row=[]

final_back=[]
final_array_back=[]
row_back=[]


file1 = open('finished-paths-no-back.csv') #ignoring '<'
csv_read1 = csv.reader(file1, delimiter=',')
list_finished_paths_no_back=list(csv_read1)


file2 = open('finished-paths-back.csv') #not ignoring'<'
csv_read2 = csv.reader(file2, delimiter=',')
list_finished_paths_back=list(csv_read2)

count_dict={}
count_dict_back={}
for i in range(1,len(list_finished_paths_back)):
	diff=int(list_finished_paths_no_back[i][0])-int(list_finished_paths_no_back[i][1])
	if diff in count_dict.keys():
		count_dict[diff]+=1
	else:
		count_dict[diff]=1

sum=0
ratio=count_dict[0]/(len(list_finished_paths_no_back)-1)
final.append({'Path difference':0, 'Ratio': ratio*100})

for i in range(1,11):
	ratio=count_dict[i]/(len(list_finished_paths_no_back)-1)
	final.append({'Path difference':i, 'Ratio': ratio*100})
	
for i in range(11,max(count_dict,key=int)+1):
	if i in count_dict.keys():
		sum+=count_dict[i]
		
ratio=sum/(len(list_finished_paths_no_back)-1)
final.append({'Path difference':'>11', 'Ratio': ratio*100})

for ele in final:
	final_array.append(ele['Ratio'])

row.append({'Equal_Length':final_array[0],'Larger_by_1':final_array[1],'Larger_by_2':final_array[2],
			'Larger_by_3':final_array[3],'Larger_by_4':final_array[4],'Larger_by_5':final_array[5],
			'Larger_by_6':final_array[6],'Larger_by_7':final_array[7],'Larger_by_8':final_array[8],
			'Larger_by_9':final_array[9],'Larger_by_10':final_array[10],'Larger_by_more_than_10':final_array[11]})


try:
	with open("percentage-paths-no-back.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['Equal_Length','Larger_by_1','Larger_by_2','Larger_by_3',
			'Larger_by_4','Larger_by_5','Larger_by_6','Larger_by_7','Larger_by_8',
			'Larger_by_9','Larger_by_10','Larger_by_more_than_10'])
		writer.writeheader()
		writer.writerows(row)
except IOError:
    print("I/O error")


for i in range(1,len(list_finished_paths_back)):
	diff=int(list_finished_paths_back[i][0])-int(list_finished_paths_back[i][1])
	if diff in count_dict_back.keys():
		count_dict_back[diff]+=1
	else:
		count_dict_back[diff]=1
# print(count_dict_back)	
# print(max(count_dict,key=int))
sum=0
ratio=count_dict_back[0]/(len(list_finished_paths_back))
final_back.append({'Path difference':0, 'Ratio': ratio*100})

for i in range(1,11):
	ratio=count_dict_back[i]/(len(list_finished_paths_back))
	final_back.append({'Path difference':i, 'Ratio': ratio*100})
	
for i in range(11,max(count_dict,key=int)+1):
	if i in count_dict_back.keys():
		sum+=count_dict_back[i]
ratio=sum/(len(list_finished_paths_back))
final_back.append({'Path difference':'>11', 'Ratio': ratio*100})
# print(final)
for ele in final_back:
	final_array_back.append(ele['Ratio'])
# print(final_array_back)
# print(final_array[3])
row_back.append({'Equal_Length':final_array_back[0],'Larger_by_1':final_array_back[1],'Larger_by_2':final_array_back[2],
			'Larger_by_3':final_array_back[3],'Larger_by_4':final_array_back[4],'Larger_by_5':final_array_back[5],
			'Larger_by_6':final_array_back[6],'Larger_by_7':final_array_back[7],'Larger_by_8':final_array_back[8],
			'Larger_by_9':final_array_back[9],'Larger_by_10':final_array_back[10],'Larger_by_more_than_10':final_array_back[11]})


try:
	with open("percentage-paths-back.csv", 'w') as csvfile1:
		writer1 = csv.DictWriter(csvfile1, fieldnames=['Equal_Length','Larger_by_1','Larger_by_2','Larger_by_3',
			'Larger_by_4','Larger_by_5','Larger_by_6','Larger_by_7','Larger_by_8',
			'Larger_by_9','Larger_by_10','Larger_by_more_than_10'])
		writer1.writeheader()
		writer1.writerows(row_back)
except IOError:
    print("I/O error")

