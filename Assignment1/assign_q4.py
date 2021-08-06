import pandas as pd
import json
import csv
import numpy as np

final_output = []
dict_for_q6_week={}
final_output_month=[]
dict_for_q6_month={}
final_output_overall=[]
dict_for_q6_overall={}

with open('output.json') as json_file:
    matched_districts = json.load(json_file)
with open('neighbor-district-modified.json') as json_file:
    allData = json.load(json_file)
with open('q4_week_json.json') as json_file:
	week_data = json.load(json_file)
with open('q4_month_json.json') as json_file:
	month_data = json.load(json_file)
with open('q4_overall_json.json') as json_file:
	overall_data = json.load(json_file)


for week_id in range(1,26):
	for dis,neigh in allData.items():
		array=[]
		for neigh_ele in neigh:
			dis_id=matched_districts[neigh_ele]
			cases=week_data[str(dis_id)+'/'+str(week_id)]
			array.append(cases)
										
		final_output.append({'district id':matched_districts[dis],'week id':week_id, 'neighbormean':round(np.mean(array),2),'neighborstdev':round(np.std(array),2)})
		dict_for_q6_week[str(matched_districts[dis])+'/'+str(week_id)+'/nm']={'neighbormean':round(np.mean(array),2),'neighborstdev':round(np.std(array),2)}
	
csv_columns = ['district id','week id','neighbormean','neighborstdev']
try:
    with open("neighbor-week.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(final_output)
except IOError:
    print("I/O error")

with open('dict_for_q6_week.json', 'w') as fp:
    json.dump(dict_for_q6_week, fp)




for month_id in range(1,8):
	for dis,neigh in allData.items():
		array=[]
		for neigh_ele in neigh:
			dis_id=matched_districts[neigh_ele]
			cases=month_data[str(dis_id)+'/'+str(month_id)]
			array.append(cases)
						
		final_output_month.append({'district id':matched_districts[dis],'month id':month_id, 'neighbormean':round(np.mean(array),2),'neighborstdev':round(np.std(array),2)})
		dict_for_q6_month[str(matched_districts[dis])+'/'+str(month_id)+'/nm']={'neighbormean':round(np.mean(array),2),'neighborstdev':round(np.std(array),2)}
	
csv_month_columns = ['district id','month id','neighbormean','neighborstdev']
try:
    with open("neighbor-month.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_month_columns)
        writer.writeheader()
        writer.writerows(final_output_month)
except IOError:
    print("I/O error")

with open('dict_for_q6_month.json', 'w') as fp:
    json.dump(dict_for_q6_month, fp)


for dis,neigh in allData.items():
	array=[]
	for neigh_ele in neigh:	
		dis_id=matched_districts[neigh_ele]
		cases=overall_data[str(dis_id)+'/1']
		array.append(cases)
			
	final_output_overall.append({'district id':matched_districts[dis],'overall id':1, 'neighbormean':round(np.mean(array),2),'neighborstdev':round(np.std(array),2)})
	dict_for_q6_overall[str(matched_districts[dis])+'/1/nm']={'neighbormean':round(np.mean(array),2),'neighborstdev':round(np.std(array),2)}
	
csv_overall_columns = ['district id','overall id','neighbormean','neighborstdev']
try:
    with open("neighbor-overall.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_overall_columns)
        writer.writeheader()
        writer.writerows(final_output_overall)
except IOError:
    print("I/O error")

with open('dict_for_q6_overall.json', 'w') as fp:
    json.dump(dict_for_q6_overall, fp)



