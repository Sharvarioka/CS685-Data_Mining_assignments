import pandas as pd
import json
import time
from datetime import datetime, timedelta
import csv
from calendar import monthrange

final_output = {}
final_output_month={}
final_output_overall={}
with open('output.json') as json_file:
    matched_districts = json.load(json_file)
with open('data-all.json') as json_file:
    allData = json.load(json_file)


##########
# the anlaytics part

week=1
init_static_date = '2020-03-15'
init_date = '2020-03-15'
end_date = '2020-09-05'
while init_date <= end_date:
    for week_range in range(1,8):
        if init_date > end_date:
            break
        date_time_obj = datetime.strptime(init_date, '%Y-%m-%d')
        date_string = date_time_obj.strftime('%Y-%m-%d')
        # print(date_string)
        # print(week)
        if date_string in allData.keys():
            for every_state_code, district_info in allData[date_string].items():
                if 'districts' in district_info.keys():
                    for every_district_name, metadata in district_info.get('districts').items():
                        test=0
                        if 'delta' in metadata.keys():
                            if 'confirmed' in metadata.get('delta').keys():
                                test = abs(metadata['delta']['confirmed'])                       	
                            else:
                                test = 0
                        for dist_keys in matched_districts.keys():
                            if dist_keys.split('/')[0].lower()==every_district_name.lower() and dist_keys.split('/')[2].lower()==every_state_code.lower():
                                if str(matched_districts.get(dist_keys))+'/'+str(week) in final_output.keys():
                                    current_count = final_output.pop(str(matched_districts.get(dist_keys))+'/'+str(week))
                                    final_output[str(matched_districts.get(dist_keys))+'/'+str(week)] = test + current_count
                                else:
                                    final_output[str(matched_districts.get(dist_keys))+'/'+str(week)] = test     	
        init_date = (datetime.strptime(init_static_date, '%Y-%m-%d') + timedelta(days=week_range)).strftime('%Y-%m-%d')
    already_keys=[]
    for key in final_output.keys():
        already_keys.append(key)
    for dis_id in matched_districts.values():
        if str(dis_id)+'/'+str(week) not in already_keys:
           final_output[str(dis_id)+'/'+str(week)]=0
    week=week+1
    init_static_date = init_date

csv_columns = ['district id','week id','cases']

try:
    with open("cases-week.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for district_week,cases in final_output.items():
            array=district_week.split("/")
            dictionary_week={'district id':array[0],'week id':array[1],'cases':cases}
            writer.writerow(dictionary_week)
except IOError:
    print("I/O error")

with open('q4_week_json.json', 'w') as fp:
    json.dump(final_output, fp)


##### for analytics part for month

def last_day_of_month(date_value):
    return date_value.replace(day = monthrange(date_value.year, date_value.month)[1])

month=1
#init_static_date = '2020-03-15'
init_date = '2020-03-15'
end_date = '2020-09-05'
while init_date <= end_date:
    date_time_obj = datetime.strptime(init_date, '%Y-%m-%d')
    month_end_date_obj=last_day_of_month(date_time_obj)
    delta = month_end_date_obj - date_time_obj
    for i in range(delta.days + 1):
        day = date_time_obj + timedelta(days=i)
        date_string = day.strftime('%Y-%m-%d')
   
        if date_string in allData.keys():
            for every_state_code, district_info in allData[date_string].items():
                if 'districts' in district_info.keys():
                    for every_district_name, metadata in district_info.get('districts').items():
                        test=0
                        if 'delta' in metadata.keys():
                            if 'confirmed' in metadata.get('delta').keys():
                                test = abs(metadata['delta']['confirmed'])                       	
                            else:
                                test = 0
	                        
                        for dist_keys in matched_districts:
                            if dist_keys.split('/')[0].lower()==every_district_name.lower() and dist_keys.split('/')[2].lower()==every_state_code.lower():
                                if str(matched_districts.get(dist_keys))+'/'+str(month) in final_output_month.keys():
                                    current_count = final_output_month.pop(str(matched_districts.get(dist_keys))+'/'+str(month))
                                    final_output_month[str(matched_districts.get(dist_keys))+'/'+str(month)] = test + current_count
                                else:
                                    final_output_month[str(matched_districts.get(dist_keys))+'/'+str(month)] = test 
	                                         
        init_date = (datetime.strptime(date_string, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
    already_keys=[]
    for key in final_output_month.keys():
        already_keys.append(key)
    for dis_id in matched_districts.values():
        if str(dis_id)+'/'+str(month) not in already_keys:
           final_output_month[str(dis_id)+'/'+str(month)]=0
    month=month+1
csv_columns_month = ['district id','month id','cases']

try:
    with open("cases-month.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns_month)
        writer.writeheader()
        for district_month,cases in final_output_month.items():
            array=district_month.split("/")
            dictionary_month={'district id':array[0],'month id':array[1],'cases':cases}
            writer.writerow(dictionary_month)
except IOError:
    print("I/O error")

with open('q4_month_json.json', 'w') as fp:
    json.dump(final_output_month, fp)




##analysis part year


init_date = '2020-03-15'
end_date = '2020-09-05'

date_time_obj = datetime.strptime(init_date, '%Y-%m-%d')
date_time_obj_end_date = datetime.strptime(end_date, '%Y-%m-%d')
 
delta = date_time_obj_end_date - date_time_obj       # as timedelta
for i in range(delta.days + 1):
    day = date_time_obj + timedelta(days=i)
    date_string = day.strftime('%Y-%m-%d')
  
    if date_string in allData.keys():
        for every_state_code, district_info in allData[date_string].items():
            if 'districts' in district_info.keys():
                for every_district_name, metadata in district_info.get('districts').items():
                    test=0
                    if 'delta' in metadata.keys():
                        if 'confirmed' in metadata.get('delta').keys():
                            test = abs(metadata['delta']['confirmed'])
                        else:
                            test=0
	                                               
                    for dist_keys in matched_districts.keys():
	                    if dist_keys.split('/')[0].lower()==every_district_name.lower() and dist_keys.split('/')[2].lower()==every_state_code.lower():
	                        if str(matched_districts.get(dist_keys))+'/1' in final_output_overall.keys():
	                            current_count = final_output_overall.pop(str(matched_districts.get(dist_keys))+'/1')
	                            final_output_overall[str(matched_districts.get(dist_keys))+'/1'] = test + current_count
	                        else:
	                            final_output_overall[str(matched_districts.get(dist_keys))+'/1'] = test
already_keys=[]
for key in final_output_overall.keys():
    already_keys.append(key)
for dis_id in matched_districts.values():
    if str(dis_id)+'/1' not in already_keys:
       final_output_overall[str(dis_id)+'/1']=0




csv_columns_overall = ['district id','year id','cases']

try:
    with open("cases-overall.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns_overall)
        writer.writeheader()
        for district_year,cases in final_output_overall.items():
            array=district_year.split("/")
            dictionary_year={'district id':array[0],'year id':array[1],'cases':cases}
            writer.writerow(dictionary_year)
except IOError:
    print("I/O error")  

with open('q4_overall_json.json', 'w') as fp:
    json.dump(final_output_overall, fp)       






