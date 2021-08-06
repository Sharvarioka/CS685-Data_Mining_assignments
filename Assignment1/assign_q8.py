import pandas as pd
import json
import csv
from heapq import nlargest,nsmallest

with open('output.json') as json_file:
    matched_districts = json.load(json_file)
with open('neighbor-district-modified.json') as json_file:
    allData = json.load(json_file)

with open('dict_for_q6_week_zscore_state.json') as json_file:
	dict_for_q6_week_zscore_state = json.load(json_file)

with open('dict_for_q6_month_zscore_state.json') as json_file:
	dict_for_q6_month_zscore_state = json.load(json_file)

with open('dict_for_q6_overall_zscore_state.json') as json_file:
	dict_for_q6_overall_zscore_state = json.load(json_file)

with open('q4_week_json.json') as json_file:
	week_data = json.load(json_file)

top_5_neigh_week=[]
top_5_neigh_month=[]
top_5_neigh_overall=[]

top_5_state_week=[]
top_5_state_month=[]
top_5_state_overall=[]


output_q8_week=[]
output_q8_month=[]
output_q8_overall=[]

#week part
for week_id in range(1,26):
	#array_zscore=[]
	top_5_neigh_week=[]
	top_5_state_week=[]
	for dis in allData.keys():
		zscore=dict_for_q6_week_zscore_state[str(matched_districts[dis])+'/'+str(week_id)+'/snz']['neighborhoodzscore']
		if zscore !='NA':
			top_5_neigh_week.append({'week id' :week_id, 'spot':'hot','district id':matched_districts[dis],'neighborhoodzscore':zscore})
		
		zscore_state=dict_for_q6_week_zscore_state[str(matched_districts[dis])+'/'+str(week_id)+'/snz']['statezscore']
		if zscore_state !='NA':
			top_5_state_week.append({'week id' :week_id, 'spot':'hot','district id':matched_districts[dis],'statezscore':zscore_state})
		
	if len(top_5_neigh_week)>4:
		top_5_hot=nlargest(5, top_5_neigh_week, key=lambda item: item["neighborhoodzscore"])
		res = [ sub['district id'] for sub in top_5_hot ] 
		output_q8_week.append({'week id':week_id,'spot':'hot','method':'neighborhood','district id 1':res[0],'district id 2':res[1],'district id 3':res[2],'district id 4':res[3],'district id 5':res[4]})
		

		top_5_cold=nsmallest(5, top_5_neigh_week, key=lambda item: item["neighborhoodzscore"])
		res = [ sub['district id'] for sub in top_5_cold ] 
		output_q8_week.append({'week id':week_id,'spot':'cold','method':'neighborhood','district id 1':res[0],'district id 2':res[1],'district id 3':res[2],'district id 4':res[3],'district id 5':res[4]})
	if len(top_5_state_week)>4:
		top_5_hot=nlargest(5, top_5_state_week, key=lambda item: item["statezscore"])
		res = [ sub['district id'] for sub in top_5_hot ] 
		output_q8_week.append({'week id':week_id,'spot':'hot','method':'state','district id 1':res[0],'district id 2':res[1],'district id 3':res[2],'district id 4':res[3],'district id 5':res[4]})
		
		top_5_cold=nsmallest(5, top_5_state_week, key=lambda item: item["statezscore"])
		res = [ sub['district id'] for sub in top_5_cold ] 
		output_q8_week.append({'week id':week_id,'spot':'cold','method':'state','district id 1':res[0],'district id 2':res[1],'district id 3':res[2],'district id 4':res[3],'district id 5':res[4]})
		
	
csv_columns = ['week id','spot','method','district id 1','district id 2','district id 3','district id 4','district id 5']
try:
    with open("top-week.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(output_q8_week)
except IOError:
    print("I/O error")
		
#month part
for month_id in range(1,8):
	top_5_neigh_month=[]
	top_5_state_month=[]

	for dis in allData.keys():
		zscore=dict_for_q6_month_zscore_state[str(matched_districts[dis])+'/'+str(month_id)+'/snz']['neighborhoodzscore']
		if zscore !='NA':
			top_5_neigh_month.append({'month id' :month_id, 'spot':'hot','district id':matched_districts[dis],'neighborhoodzscore':zscore})
		
		zscore_state=dict_for_q6_month_zscore_state[str(matched_districts[dis])+'/'+str(month_id)+'/snz']['statezscore']
		if zscore_state !='NA':
			top_5_state_month.append({'month id' :month_id, 'spot':'hot','district id':matched_districts[dis],'statezscore':zscore_state})
	if len(top_5_neigh_month)>4:	
		top_5_hot=nlargest(5, top_5_neigh_month, key=lambda item: item["neighborhoodzscore"])
		res = [ sub['district id'] for sub in top_5_hot ] 
		output_q8_month.append({'month id':month_id,'spot':'hot','method':'neighborhood','district id 1':res[0],'district id 2':res[1],'district id 3':res[2],'district id 4':res[3],'district id 5':res[4]})
		
		top_5_cold=nsmallest(5, top_5_neigh_month, key=lambda item: item["neighborhoodzscore"])
		res = [ sub['district id'] for sub in top_5_cold ] 
		output_q8_month.append({'month id':month_id,'spot':'cold','method':'neighborhood','district id 1':res[0],'district id 2':res[1],'district id 3':res[2],'district id 4':res[3],'district id 5':res[4]})
	
	if len(top_5_state_month)>4:
		top_5_hot=nlargest(5, top_5_state_month, key=lambda item: item['statezscore'])
		res = [ sub['district id'] for sub in top_5_hot ] 
		output_q8_month.append({'month id':month_id,'spot':'hot','method':'state','district id 1':res[0],'district id 2':res[1],'district id 3':res[2],'district id 4':res[3],'district id 5':res[4]})
		
		top_5_cold=nsmallest(5, top_5_state_month, key=lambda item: item['statezscore'])
		res = [ sub['district id'] for sub in top_5_cold ] 
		output_q8_month.append({'month id':month_id,'spot':'cold','method':'state','district id 1':res[0],'district id 2':res[1],'district id 3':res[2],'district id 4':res[3],'district id 5':res[4]})
		

csv_columns = ['month id','spot','method','district id 1','district id 2','district id 3','district id 4','district id 5']
try:
    with open("top-month.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(output_q8_month)
except IOError:
    print("I/O error")		


#year part
top_5_neigh_overall=[]
top_5_state_overall=[]
for dis in allData.keys():
	zscore=dict_for_q6_overall_zscore_state[str(matched_districts[dis])+'/1/snz']['neighborhoodzscore']
	if zscore !='NA':
		top_5_neigh_overall.append({'overall id' :1, 'spot':'hot','district id':matched_districts[dis],'neighborhoodzscore':zscore})
	
	zscore_state=dict_for_q6_overall_zscore_state[str(matched_districts[dis])+'/1/snz']['statezscore']
	if zscore_state !='NA':
		top_5_state_overall.append({'overall id' :1, 'spot':'hot','district id':matched_districts[dis],'statezscore':zscore_state})

if len(top_5_neigh_overall)>4:	
	top_5_hot=nlargest(5, top_5_neigh_overall, key=lambda item: item["neighborhoodzscore"])
	res = [ sub['district id'] for sub in top_5_hot ] 
	output_q8_overall.append({'overall id':1,'spot':'hot','method':'neighborhood','district id 1':res[0],'district id 2':res[1],'district id 3':res[2],'district id 4':res[3],'district id 5':res[4]})

	top_5_cold=nsmallest(5, top_5_neigh_overall, key=lambda item: item["neighborhoodzscore"])
	res = [ sub['district id'] for sub in top_5_cold ] 
	output_q8_overall.append({'overall id':1,'spot':'cold','method':'neighborhood','district id 1':res[0],'district id 2':res[1],'district id 3':res[2],'district id 4':res[3],'district id 5':res[4]})

if len(top_5_state_overall)>4:
	top_5_hot=nlargest(5, top_5_state_overall, key=lambda item: item['statezscore'])
	res = [ sub['district id'] for sub in top_5_hot ] 
	output_q8_overall.append({'overall id':1,'spot':'hot','method':'state','district id 1':res[0],'district id 2':res[1],'district id 3':res[2],'district id 4':res[3],'district id 5':res[4]})

	top_5_cold=nsmallest(5, top_5_state_overall, key=lambda item: item['statezscore'])
	res = [ sub['district id'] for sub in top_5_cold ] 
	output_q8_overall.append({'overall id':1,'spot':'cold','method':'state','district id 1':res[0],'district id 2':res[1],'district id 3':res[2],'district id 4':res[3],'district id 5':res[4]})

csv_columns = ['overall id','spot','method','district id 1','district id 2','district id 3','district id 4','district id 5']
try:
    with open("top-overall.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(output_q8_overall)
except IOError:
    print("I/O error")		
