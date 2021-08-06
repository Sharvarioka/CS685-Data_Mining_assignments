import pandas as pd
import json
import csv
import numpy as np

final_output = []
dict_for_q6_week_state={}
final_output_month=[]
dict_for_q6_month_state={}
final_output_overall=[]
dict_for_q6_overall_state={}
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
	for dis in allData.keys():
		array=[]
		for neigh in allData.keys():
			if dis==neigh:
				continue
			else:			
				if dis.split("/")[2]==neigh.split("/")[2]:
					dis_id=matched_districts[neigh]
					cases=week_data[str(dis_id)+'/'+str(week_id)]
					array.append(cases)
		
		if len(array)==0:
			final_output.append({'district id':matched_districts[dis],'week id':week_id, 'statemean':0,'statestdev':0})
			dict_for_q6_week_state[str(matched_districts[dis])+'/'+str(week_id)+'/sm']={'statemean':0,'statestdev':0}
		else:
			final_output.append({'district id':matched_districts[dis],'week id':week_id, 'statemean':round(np.mean(array),2),'statestdev':round(np.std(array),2)})
			dict_for_q6_week_state[str(matched_districts[dis])+'/'+str(week_id)+'/sm']={'statemean':round(np.mean(array),2),'statestdev':round(np.std(array),2)}
csv_columns = ['district id','week id','statemean','statestdev']
try:
    with open("state-week.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(final_output)
except IOError:
    print("I/O error")

with open('dict_for_q6_week_state.json', 'w') as fp:
    json.dump(dict_for_q6_week_state, fp)

for month_id in range(1,8):
	for dis in allData.keys():
		array=[]
		for neigh in allData.keys():
			if dis==neigh:
				continue
			else:			
				if dis.split("/")[2]==neigh.split("/")[2]:
					dis_id=matched_districts[neigh]
					cases=month_data[str(dis_id)+'/'+str(month_id)]
					array.append(cases)
		
		if len(array)==0:
			final_output_month.append({'district id':matched_districts[dis],'month id':month_id, 'statemean':0,'statestdev':0})
			dict_for_q6_month_state[str(matched_districts[dis])+'/'+str(month_id)+'/sm']={'statemean':0,'statestdev':0}
		else:
			final_output_month.append({'district id':matched_districts[dis],'month id':month_id, 'statemean':round(np.mean(array),2),'statestdev':round(np.std(array),2)})
			dict_for_q6_month_state[str(matched_districts[dis])+'/'+str(month_id)+'/sm']={'statemean':round(np.mean(array),2),'statestdev':round(np.std(array),2)}
csv_columns = ['district id','month id','statemean','statestdev']
try:
    with open("state-month.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(final_output_month)
except IOError:
    print("I/O error")
with open('dict_for_q6_month_state.json', 'w') as fp:
    json.dump(dict_for_q6_month_state, fp)


for dis in allData.keys():
		array=[]
		for neigh in allData.keys():
			if dis==neigh:
				continue
			else:			
				if dis.split("/")[2]==neigh.split("/")[2]:
					dis_id=matched_districts[neigh]
					cases=overall_data[str(dis_id)+'/1']
					array.append(cases)
		

		if len(array)==0:
			final_output_overall.append({'district id':matched_districts[dis],'overall id':1, 'statemean':0,'statestdev':0})
			dict_for_q6_overall_state[str(matched_districts[dis])+'/1/sm']={'statemean':0,'statestdev':0}

		else:
			final_output_overall.append({'district id':matched_districts[dis],'overall id':1, 'statemean':round(np.mean(array),2),'statestdev':round(np.std(array),2)})
			dict_for_q6_overall_state[str(matched_districts[dis])+'/1/sm']={'statemean':round(np.mean(array),2),'statestdev':round(np.std(array),2)}

csv_columns = ['district id','overall id','statemean','statestdev']
try:
    with open("state-overall.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(final_output_overall)
except IOError:
    print("I/O error")
with open('dict_for_q6_overall_state.json', 'w') as fp:
    json.dump(dict_for_q6_overall_state, fp)




