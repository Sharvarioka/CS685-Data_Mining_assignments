Following points describe the plugins and dependencies needed to run the assignment.It is mentioned question wise.
1. Run assign_question1.sh
---> It generates two files after running assign_question1.sh

neighbor-district-modified.json
---> which consists of districts arranged in alphabetical order for which I have used 'data-all.json' from COVID-19 portal to map the districts with districts in 'neighbor-districts.json'. To treat the case where the smaller districts need to be merged as a bigger one I created a new district which matched the district name in COVID-19 data-all.json and merged their neighbors as well. Keys with smaller districts and empty array as neighbors were removed. 

output.json
---> which contains the matched district names and ids assigned from 101. Some districts are added which are exact matched and some of the districts are added manually.

2. Run case-generator.sh
It creates 3 files:
	cases-week.csv,
	cases-month.csv,
	cases-overall.csv

It produces 3 json files for internal processing:
 	q4_week_json.json,
 	q4_month_json.json,
 	q4_overall_json.json

I have considered numbers under the key 'confirmed' in 'data-all.json' to calculate the cases in week, month, year.

3. Run edge-generator.sh
It creates edge-graph.csv.

4. Run neighbor-generator.sh
It creates 3 files: 
	neighbor-week.csv,
	neighbor-month.csv,
	neighbor-overall.csv.

It produces 3 json files for internal processing:
 	dict_for_q6_week.json,
 	dict_for_q6_month.json,
 	dict_for_q6_overall.json

5. Run state-generator.sh
It creates 3 files:
	 state-week.csv,
	 state-month.csv,
	 state-overall.csv

It generates 3 json files for internal processing: 
	 dict_for_q6_week_state.json,
	 dict_for_q6_month_state.json,
	 dict_for_q6_overall_state.json

If a state has only one district present then the statemean and the stateStdDev will be 0.

6. Run zscore-generator.sh
It creates 3 files:
	 zscore-week.csv,
	 zscore-month.csv,
	 zscore-overall.csv

It generates 3 json files for internal processing: 
	 dict_for_q6_week_zscore_state.json,
	 dict_for_q6_month_zscore_state.json,
	 dict_for_q6_overall_zscore_state.json
	 
Z-score is considered as 'NA' where the respective standard deviation for state/neighborhood is 0.	 
	 

7. Run method-spot-generator.sh
It creates 3 files:
	 method-spot-week.csv,
	 method-spot-month.csv,
	 method-spot-overall.csv


8. Run top-generator.sh
It creates 3 files:
	 top-week.csv,
	 top-month.csv,
	 top-overall.csv

