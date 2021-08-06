import pandas as pd
import json
import csv

final_output_week = []
final_output_month=[]
final_output_overall=[]

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


with open('dict_for_q6_week_state.json') as json_file:
	dict_for_q6_week_state = json.load(json_file)


with open('dict_for_q6_month_state.json') as json_file:
	dict_for_q6_month_state = json.load(json_file)


with open('dict_for_q6_overall_state.json') as json_file:
	dict_for_q6_overall_state = json.load(json_file)

with open('dict_for_q6_week.json') as json_file:
	dict_for_q6_week = json.load(json_file)


with open('dict_for_q6_month.json') as json_file:
	dict_for_q6_month = json.load(json_file)


with open('dict_for_q6_overall.json') as json_file:
	dict_for_q6_overall = json.load(json_file)



# week ,hot,neighbor
for week_id in range(1,26):
	for dis in allData.keys():
		dis_id=matched_districts[dis]
		neigh_zscore=dict_for_q6_week_zscore_state[str(dis_id)+'/'+str(week_id)+'/snz']['neighborhoodzscore']
		state_zscore=dict_for_q6_week_zscore_state[str(dis_id)+'/'+str(week_id)+'/snz']['statezscore']
		if neigh_zscore!='NA':
			if neigh_zscore>1:
				final_output_week.append({'week id':week_id,'method':'neighborhood', 'spot':'hot', 'district id' :dis_id})
			if neigh_zscore<-1:
				final_output_week.append({'week id':week_id,'method':'neighborhood', 'spot':'cold', 'district id' :dis_id})
		if state_zscore!='NA':
			if state_zscore>1:
				final_output_week.append({'week id':week_id,'method':'state', 'spot':'hot', 'district id' :dis_id})
			if state_zscore<-1:
				final_output_week.append({'week id':week_id,'method':'state', 'spot':'cold', 'district id' :dis_id})
		
csv_columns = ['week id','method','spot','district id']
try:
    with open("method-spot-week.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(final_output_week)
except IOError:
    print("I/O error")


# month,hot,neighbor
for month_id in range(1,8):
	for dis in allData.keys():
		dis_id=matched_districts[dis]
		neigh_zscore=dict_for_q6_month_zscore_state[str(dis_id)+'/'+str(month_id)+'/snz']['neighborhoodzscore']
		state_zscore=dict_for_q6_month_zscore_state[str(dis_id)+'/'+str(month_id)+'/snz']['statezscore']
		if neigh_zscore!='NA':
			if neigh_zscore>1:
				final_output_month.append({'month id':month_id,'method':'neighborhood', 'spot':'hot', 'district id' :dis_id})
			if neigh_zscore<-1:
				final_output_month.append({'month id':month_id,'method':'neighborhood', 'spot':'cold', 'district id' :dis_id})

		if state_zscore!='NA':
			if state_zscore>1:
				final_output_month.append({'month id':month_id,'method':'state', 'spot':'hot', 'district id' :dis_id})
			if state_zscore<-1:
				final_output_month.append({'month id':month_id,'method':'state', 'spot':'cold', 'district id' :dis_id})

csv_columns = ['month id','method','spot','district id']
try:
    with open("method-spot-month.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(final_output_month)
except IOError:
    print("I/O error")

# overall ,hot,neighbor

for dis in allData.keys():
	dis_id=matched_districts[dis]
	neigh_zscore=dict_for_q6_overall_zscore_state[str(dis_id)+'/1/snz']['neighborhoodzscore']
	state_zscore=dict_for_q6_overall_zscore_state[str(dis_id)+'/1/snz']['statezscore']
	if neigh_zscore!="NA":
		if neigh_zscore > 1:
			final_output_overall.append({'overall id':1,'method':'neighborhood', 'spot':'hot', 'district id' :dis_id})
		if neigh_zscore<-1:
			final_output_overall.append({'overall id':1,'method':'neighborhood', 'spot':'cold', 'district id' :dis_id})

	if state_zscore!="NA":
		if state_zscore > 1:
			final_output_overall.append({'overall id':1,'method':'state', 'spot':'hot', 'district id' :dis_id})
		if state_zscore<-1:
			final_output_overall.append({'overall id':1,'method':'state', 'spot':'cold', 'district id' :dis_id})


csv_columns = ['overall id','method','spot','district id']
try:
    with open("method-spot-overall.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(final_output_overall)
except IOError:
    print("I/O error")












