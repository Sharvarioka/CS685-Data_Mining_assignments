import pandas as pd
import json
import csv

final_output = []
dict_for_q6_week_zscore_state={}
final_output_month=[]
dict_for_q6_month_zscore_state={}
final_output_overall=[]
dict_for_q6_overall_zscore_state={}
with open('output.json') as json_file:
    matched_districts = json.load(json_file)
with open('neighbor-district-modified.json') as json_file:
    allData = json.load(json_file)

with open('dict_for_q6_week.json') as json_file:
	dict_for_q6_week = json.load(json_file)


with open('dict_for_q6_week_state.json') as json_file:
	dict_for_q6_week_state = json.load(json_file)

with open('dict_for_q6_month.json') as json_file:
	dict_for_q6_month = json.load(json_file)


with open('dict_for_q6_month_state.json') as json_file:
	dict_for_q6_month_state= json.load(json_file)

with open('dict_for_q6_overall.json') as json_file:
	dict_for_q6_overall = json.load(json_file)


with open('dict_for_q6_overall_state.json') as json_file:
	dict_for_q6_overall_state = json.load(json_file)

with open('q4_week_json.json') as json_file:
	week_data = json.load(json_file)
with open('q4_month_json.json') as json_file:
	month_data = json.load(json_file)
with open('q4_overall_json.json') as json_file:
	overall_data = json.load(json_file)

#week part
for week_id in range(1,26):
	for dis in allData.keys():
		dis_id=matched_districts[dis]
		
		if dict_for_q6_week[str(dis_id)+'/'+str(week_id)+'/nm']['neighborstdev']!=0:
			zscore=round((week_data[str(dis_id)+'/'+str(week_id)]-dict_for_q6_week[str(dis_id)+'/'+str(week_id)+'/nm']['neighbormean'])/dict_for_q6_week[str(dis_id)+'/'+str(week_id)+'/nm']['neighborstdev'],2)
		else: 
			zscore='NA'

		if dict_for_q6_week_state[str(dis_id)+'/'+str(week_id)+'/sm']['statestdev']!=0:
			state_zscore=round((week_data[str(dis_id)+'/'+str(week_id)]-dict_for_q6_week_state[str(dis_id)+'/'+str(week_id)+'/sm']['statemean'])/dict_for_q6_week_state[str(dis_id)+'/'+str(week_id)+'/sm']['statestdev'],2)
		else:
			state_zscore='NA'
			
		final_output.append({'district id':dis_id,'week id':week_id, 'neighborhoodzscore':zscore,'statezscore':state_zscore})
		dict_for_q6_week_zscore_state[str(matched_districts[dis])+'/'+str(week_id)+'/snz']={'neighborhoodzscore':zscore,'statezscore':state_zscore}

csv_columns = ['district id','week id','neighborhoodzscore','statezscore']
try:
    with open("zscore-week.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(final_output)
except IOError:
    print("I/O error")

with open('dict_for_q6_week_zscore_state.json', 'w') as fp:
    json.dump(dict_for_q6_week_zscore_state, fp)

#month part
for month_id in range(1,8):
	for dis in allData.keys():
		dis_id=matched_districts[dis]
		

		if dict_for_q6_month[str(dis_id)+'/'+str(month_id)+'/nm']['neighborstdev']!=0:
			zscore=round((month_data[str(dis_id)+'/'+str(month_id)]-dict_for_q6_month[str(dis_id)+'/'+str(month_id)+'/nm']['neighbormean'])/dict_for_q6_month[str(dis_id)+'/'+str(month_id)+'/nm']['neighborstdev'],2)
		else: 
			zscore='NA'

		if dict_for_q6_month_state[str(matched_districts[dis])+'/'+str(month_id)+'/sm']['statestdev']!=0:
			state_zscore=round((month_data[str(dis_id)+'/'+str(month_id)]-dict_for_q6_month_state[str(dis_id)+'/'+str(month_id)+'/sm']['statemean'])/dict_for_q6_month_state[str(dis_id)+'/'+str(month_id)+'/sm']['statestdev'],2)
		else:
			state_zscore='NA'
		
		final_output_month.append({'district id':dis_id,'month id':month_id, 'neighborhoodzscore':zscore,'statezscore':state_zscore})
		
		dict_for_q6_month_zscore_state[str(dis_id)+'/'+str(month_id)+'/snz']={'neighborhoodzscore':zscore,'statezscore':state_zscore}

csv_columns_month = ['district id','month id','neighborhoodzscore','statezscore']
try:
    with open("zscore-month.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns_month)
        writer.writeheader()
        writer.writerows(final_output_month)
except IOError:
    print("I/O error")

with open('dict_for_q6_month_zscore_state.json', 'w') as fp:
    json.dump(dict_for_q6_month_zscore_state, fp)

#year part
for dis in allData.keys():
	dis_id=matched_districts[dis]
	
	if dict_for_q6_overall[str(dis_id)+'/1/nm']['neighborstdev']!=0:
		zscore=round((overall_data[str(dis_id)+'/1']-dict_for_q6_overall[str(dis_id)+'/1/nm']['neighbormean'])/dict_for_q6_overall[str(dis_id)+'/1/nm']['neighborstdev'],2)
	else: 
		zscore='NA'

	if dict_for_q6_overall_state[str(dis_id)+'/1/sm']['statestdev']!=0:
		state_zscore=round((overall_data[str(dis_id)+'/1']-dict_for_q6_overall_state[str(dis_id)+'/1/sm']['statemean'])/dict_for_q6_overall_state[str(dis_id)+'/1/sm']['statestdev'],2)
	else:
		state_zscore='NA'

	final_output_overall.append({'district id':dis_id,'overall id':1, 'neighborhoodzscore':zscore,'statezscore':state_zscore})
	
	dict_for_q6_overall_zscore_state[str(dis_id)+'/1/snz']={'neighborhoodzscore':zscore,'statezscore':state_zscore}

csv_columns_overall = ['district id','overall id','neighborhoodzscore','statezscore']
try:
    with open("zscore-overall.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns_overall)
        writer.writeheader()
        writer.writerows(final_output_overall)
except IOError:
    print("I/O error")

with open('dict_for_q6_overall_zscore_state.json', 'w') as fp:
    json.dump(dict_for_q6_overall_zscore_state, fp)



