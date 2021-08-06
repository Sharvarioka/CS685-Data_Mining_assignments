import pandas as pd
import json
import sys
import random

# df = pd.read_csv('district_wise.csv')
# df_without_extension_districts = pd.read_csv('districts.csv')
# sorted_districts_with_keys_in_csv = sorted(df["District_Key"].unique())
# sorted_districts_in_csv = sorted(df_without_extension_districts["District"].unique())
dict_data = {}
final_output = {}
with open('neighbor-districts.json') as json_file:
    data = json.load(json_file)

array_dists_with_state_from_data_all = []

with open('data-all.json') as json_file:
    dataAllInfo = json.load(json_file)

for value in dataAllInfo.values():
    for state_code, dist_info in value.items():
        if 'districts' in dist_info.keys():
            for every_district_name in dist_info.get('districts').keys():
                array_dists_with_state_from_data_all.append(every_district_name.lower()+'/'+state_code)


i = 101
keylist = data.keys()

'''
remove districts and '_' in all the district names in neighbor-dist.json
and assign the temp ids from 101
'''

for key in sorted(keylist):
    dict_data[key] = i
    i = i+1
    buff_val = ""
    if "_" in key:
        variable = dict_data.pop(key)
        dict_data[key.replace("_", " ")] = variable
        buff_val = key.replace("_", " ")
    if " district" in buff_val:
        variable = dict_data.pop(buff_val)
        dict_data[buff_val.replace(" district", "")] = variable
      
matched_districts = {}

data_processsing_copy=sorted(list(set(array_dists_with_state_from_data_all.copy())))
test = dict(sorted(dict_data.copy().items())) 
matched_array=[]
for dis in data_processsing_copy:  
    disArray = dis.split('/')
    for neigh_dis in test.keys(): 
        if (neigh_dis.lower().split("/")[0]) == disArray[0]:
            if neigh_dis in dict_data.keys():
                district_number = dict_data.pop(neigh_dis)
                matched_districts[district_number] = neigh_dis+'/'+disArray[1]
                matched_array.append(neigh_dis+'/'+disArray[1])
                break

district_number = dict_data.pop('central delhi/Q107941')
matched_districts[district_number] = 'delhi'+'/Q'+str(random.randint(400000, 500000))+'/'+'DL'
district_number = dict_data.pop('east delhi/Q107960')
matched_districts[district_number] = 'delhi'+'/Q'+str(random.randint(400000, 500000))+'/'+'DL'
district_number = dict_data.pop('new delhi/Q987')
matched_districts[district_number] = 'delhi'+'/Q'+str(random.randint(400000, 500000))+'/'+'DL'
district_number = dict_data.pop('north delhi/Q693367')
matched_districts[district_number] = 'delhi'+'/Q'+str(random.randint(400000, 500000))+'/'+'DL'
district_number = dict_data.pop('north east delhi/Q429329')
matched_districts[district_number] = 'delhi'+'/Q'+str(random.randint(400000, 500000))+'/'+'DL'
district_number = dict_data.pop('north west delhi/Q766125')
matched_districts[district_number] = 'delhi'+'/Q'+str(random.randint(400000, 500000))+'/'+'DL'
district_number = dict_data.pop('south delhi/Q2061938')
matched_districts[district_number] = 'delhi'+'/Q'+str(random.randint(400000, 500000))+'/'+'DL'
district_number = dict_data.pop('south east delhi/Q25553535')
matched_districts[district_number] = 'delhi'+'/Q'+str(random.randint(400000, 500000))+'/'+'DL'
district_number = dict_data.pop('south west delhi/Q2379189')
matched_districts[district_number] = 'delhi'+'/Q'+str(random.randint(400000, 500000))+'/'+'DL'
district_number = dict_data.pop('west delhi/Q549807')
matched_districts[district_number] = 'delhi'+'/Q'+str(random.randint(400000, 500000))+'/'+'DL'



district_number = dict_data.pop('aizwal/Q1947322')
matched_districts[district_number] = 'aizawl'+'/Q'+str(random.randint(400000, 500000))+'/'+'MZ'

district_number = dict_data.pop('anugul/Q1772807')
matched_districts[district_number] = 'angul'+'/Q'+str(random.randint(400000, 500000))+'/'+'OR'

district_number = dict_data.pop('ashok nagar/Q2246416')
matched_districts[district_number] = 'ashoknagar'+'/Q'+str(random.randint(400000, 500000))+'/'+'MP'

district_number = dict_data.pop('badgam/Q2594218')
matched_districts[district_number] = 'budgam'+'/Q'+str(random.randint(400000, 500000))+'/'+'JK'

district_number = dict_data.pop('banas kantha/Q806125')
matched_districts[district_number] = 'banaskantha'+'/Q'+str(random.randint(400000, 500000))+'/'+'GJ'

district_number = dict_data.pop('bangalore rural/Q806464')
matched_districts[district_number] = 'bengaluru rural'+'/Q'+str(random.randint(400000, 500000))+'/'+'KA'

district_number = dict_data.pop('bangalore urban/Q806463')
matched_districts[district_number] = 'bengaluru urban'+'/Q'+str(random.randint(400000, 500000))+'/'+'KA'

district_number = dict_data.pop('jyotiba phule nagar/Q1891677')
matched_districts[district_number] = 'amroha'+'/Q'+str(random.randint(400000, 500000))+'/UP'

district_number = dict_data.pop('sant ravidas nagar/Q127533')
matched_districts[district_number] = 'bhadohi'+'/Q'+str(random.randint(400000, 500000))+'/UP'

district_number = dict_data.pop('palghat/Q1535742')
matched_districts[district_number] = 'palakkad'+'/Q'+str(random.randint(400000, 500000))+'/KL'

district_number = dict_data.pop('faizabad/Q1814132')
matched_districts[district_number] = 'ayodhya'+'/Q'+str(random.randint(400000, 500000))+'/UP'

district_number = dict_data.pop('baleshwar/Q2022279')
matched_districts[district_number] = 'balasore'+'/Q'+str(random.randint(400000, 500000))+'/OR'

district_number = dict_data.pop('nagarkurnool/Q28169773')
matched_districts[district_number] = 'Kurnool'+'/Q'+str(random.randint(400000, 500000))+'/AP'


district_number = dict_data.pop('sri potti sriramulu nellore/Q15383')
matched_districts[district_number] = 's.p.s. nellore'+'/Q'+str(random.randint(400000, 500000))+'/AP'


district_number = dict_data.pop('kaimur (bhabua)/Q77367')
matched_districts[district_number] = 'kaimur'+'/Q'+str(random.randint(400000, 500000))+'/BR'

district_number = dict_data.pop('baramula/Q1912057')
matched_districts[district_number] = 'baramulla'+'/Q'+str(random.randint(400000, 500000))+'/JK'


district_number = dict_data.pop('baudh/Q2363639')
matched_districts[district_number] = 'boudh'+'/Q'+str(random.randint(400000, 500000))+'/OR'

district_number = dict_data.pop('belgaum/Q815464')
matched_districts[district_number] = 'belagavi'+'/Q'+str(random.randint(400000, 500000))+'/KA'

district_number = dict_data.pop('bellary/Q1791926')
matched_districts[district_number] = 'ballari'+'/Q'+str(random.randint(400000, 500000))+'/KA'

district_number = dict_data.pop('bemetara/Q16254159')
matched_districts[district_number] = 'bametara'+'/Q'+str(random.randint(400000, 500000))+'/CT'

district_number = dict_data.pop('bid/Q814037')
matched_districts[district_number] = 'beed'+'/Q'+str(random.randint(400000, 500000))+'/MH'

district_number = dict_data.pop('dantewada/Q100211')
matched_districts[district_number] = 'dakshin bastar dantewada'+'/Q'+str(random.randint(400000, 500000))+'/CT'

district_number = dict_data.pop('debagarh/Q2269639')
matched_districts[district_number] = 'deogarh'+'/Q'+str(random.randint(400000, 500000))+'/OR'

district_number = dict_data.pop('devbhumi dwaraka/Q14594717')
matched_districts[district_number] = 'jamnagar'+'/Q'+str(random.randint(400000, 500000))+'/GJ'

district_number = dict_data.pop('dhaulpur/Q1207709')
matched_districts[district_number] = 'dholpur'+'/Q'+str(random.randint(400000, 500000))+'/RJ'

district_number = dict_data.pop('fategarh sahib/Q172485')
matched_districts[district_number] = 'fatehgarh sahib'+'/Q'+str(random.randint(400000, 500000))+'/PB'

district_number = dict_data.pop('firozpur/Q172385')
matched_districts[district_number] = 'ferozepur'+'/Q'+str(random.randint(400000, 500000))+'/PB'

district_number = dict_data.pop('gondiya/Q1917227')
matched_districts[district_number] = 'gondia'+'/Q'+str(random.randint(400000, 500000))+'/MH'

district_number = dict_data.pop('hugli/Q548518')
matched_districts[district_number] = 'hooghly'+'/Q'+str(random.randint(400000, 500000))+'/WB'

district_number = dict_data.pop('jagatsinghapur/Q971581')
matched_districts[district_number] = 'jagatsinghpur'+'/Q'+str(random.randint(400000, 500000))+'/OR'

district_number = dict_data.pop('jajapur/Q2087771')
matched_districts[district_number] = 'jajpur'+'/Q'+str(random.randint(400000, 500000))+'/OR'

district_number = dict_data.pop('jalor/Q1460832')
matched_districts[district_number] = 'jalore'+'/Q'+str(random.randint(400000, 500000))+'/RJ'

district_number = dict_data.pop('jhunjhunun/Q1471427')
matched_districts[district_number] = 'jhunjhunu'+'/Q'+str(random.randint(400000, 500000))+'/RJ'


district_number = dict_data.pop('janjgir-champa/Q2575633')
matched_districts[district_number] = 'janjgir champa'+'/Q'+str(random.randint(400000, 500000))+'/CT'

district_number = dict_data.pop('kabirdham/Q2450255')
matched_districts[district_number] = 'kabeerdham'+'/Q'+str(random.randint(400000, 500000))+'/CT'

district_number = dict_data.pop('kanchipuram/Q15157')
matched_districts[district_number] = 'kancheepuram'+'/Q'+str(random.randint(400000, 500000))+'/TN'

district_number = dict_data.pop('kheri/Q1755447')
matched_districts[district_number] = 'lakhimpur kheri'+'/Q'+str(random.randint(400000, 500000))+'/UP'

district_number = dict_data.pop('kochbihar/Q2728658')
matched_districts[district_number] = 'cooch behar'+'/Q'+str(random.randint(400000, 500000))+'/WB'

district_number = dict_data.pop('kodarma/Q2085480')
matched_districts[district_number] = 'koderma'+'/Q'+str(random.randint(400000, 500000))+'/JH'

district_number = dict_data.pop('lahul and spiti/Q837595')
matched_districts[district_number] = 'lahaul and spiti'+'/Q'+str(random.randint(400000, 500000))+'/HP'

district_number = dict_data.pop('lakhimpur/Q42743')
matched_districts[district_number] = 'lakhimpur kheri'+'/Q'+str(random.randint(400000, 500000))+'/UP'

district_number = dict_data.pop('mahesana/Q2019694')
matched_districts[district_number] = 'mehsana'+'/Q'+str(random.randint(400000, 500000))+'/GJ'

district_number = dict_data.pop('mahrajganj/Q1356139')
matched_districts[district_number] = 'maharajganj'+'/Q'+str(random.randint(400000, 500000))+'/UP'

district_number = dict_data.pop('maldah/Q2049820')
matched_districts[district_number] = 'malda'+'/Q'+str(random.randint(400000, 500000))+'/WB'

district_number = dict_data.pop('muktsar/Q1947359')
matched_districts[district_number] = 'sri muktsar sahib'+'/Q'+str(random.randint(400000, 500000))+'/PB'

district_number = dict_data.pop('mumbai suburban/Q2085374')
matched_districts[district_number] = 'mumbai'+'/Q'+str(random.randint(400000, 500000))+'/MH'

district_number = dict_data.pop('mumbai city/Q2341660')
matched_districts[district_number] = 'mumbai'+'/Q'+str(random.randint(400000, 500000))+'/MH'


district_number = dict_data.pop('nandubar/Q1623525')
matched_districts[district_number] = 'nandurbar'+'/Q'+str(random.randint(400000, 500000))+'/MH'

district_number = dict_data.pop('narsimhapur/Q2341616')
matched_districts[district_number] = 'narsinghpur'+'/Q'+str(random.randint(400000, 500000))+'/MP'

district_number = dict_data.pop('nav sari/Q1797349')
matched_districts[district_number] = 'navsari'+'/Q'+str(random.randint(400000, 500000))+'/GJ'

district_number = dict_data.pop('pakaur/Q2295930')
matched_districts[district_number] = 'pakur'+'/Q'+str(random.randint(400000, 500000))+'/JH'

district_number = dict_data.pop('panch mahal/Q1781463')
matched_districts[district_number] = 'panchmahal'+'/Q'+str(random.randint(400000, 500000))+'/GJ'

district_number = dict_data.pop('purba champaran/Q49159')
matched_districts[district_number] = 'east Champaran'+'/Q'+str(random.randint(400000, 500000))+'/BR'

district_number = dict_data.pop('pashchim champaran/Q100124')
matched_districts[district_number] = 'west Champaran'+'/Q'+str(random.randint(400000, 500000))+'/BR'

district_number = dict_data.pop('pashchimi singhbhum/Q1950527')
matched_districts[district_number] = 'west singhbhum'+'/Q'+str(random.randint(400000, 500000))+'/JH'

district_number = dict_data.pop('pattanamtitta/Q634935')
matched_districts[district_number] = 'pathanamthitta'+'/Q'+str(random.randint(400000, 500000))+'/KL'

district_number = dict_data.pop('purbi singhbhum/Q2452921')
matched_districts[district_number] = 'east singhbhum'+'/Q'+str(random.randint(400000, 500000))+'/JH'

district_number = dict_data.pop('puruliya/Q307474')
matched_districts[district_number] = 'purulia'+'/Q'+str(random.randint(400000, 500000))+'/WB'

district_number = dict_data.pop('rae bareilly/Q1321157')
matched_districts[district_number] = 'rae bareli'+'/Q'+str(random.randint(400000, 500000))+'/UP'


district_number = dict_data.pop('rajauri/Q544279')
matched_districts[district_number] = 'rajouri'+'/Q'+str(random.randint(400000, 500000))+'/JK'

district_number = dict_data.pop('ri-bhoi/Q1884672')
matched_districts[district_number] = 'ribhoi'+'/Q'+str(random.randint(400000, 500000))+'/ML'

district_number = dict_data.pop('sabar kantha/Q1772856')
matched_districts[district_number] = 'sabarkantha'+'/Q'+str(random.randint(400000, 500000))+'/GJ'

district_number = dict_data.pop('sait kibir nagar/Q1945445')
matched_districts[district_number] = 'sant kabir nagar'+'/Q'+str(random.randint(400000, 500000))+'/UP'

district_number = dict_data.pop('seraikela kharsawan/Q2362658')
matched_districts[district_number] = 'saraikela-kharsawan'+'/Q'+str(random.randint(400000, 500000))+'/JH'

district_number = dict_data.pop('shaheed bhagat singh nagar/Q202710')
matched_districts[district_number] = 'shahid bhagat singh nagar'+'/Q'+str(random.randint(400000, 500000))+'/PB'

district_number = dict_data.pop('sharawasti/Q1945458')
matched_districts[district_number] = 'shrawasti'+'/Q'+str(random.randint(400000, 500000))+'/UP'

district_number = dict_data.pop('shimoga/Q2981389')
matched_districts[district_number] = 'shivamogga'+'/Q'+str(random.randint(400000, 500000))+'/KA'

district_number = dict_data.pop('shopian/Q2073646')
matched_districts[district_number] = 'shopiyan'+'/Q'+str(random.randint(400000, 500000))+'/JK'

district_number = dict_data.pop('siddharth nagar/Q1815339')
matched_districts[district_number] = 'siddharthnagar'+'/Q'+str(random.randint(400000, 500000))+'/UP'

district_number = dict_data.pop('sivagangai/Q15195')
matched_districts[district_number] = 'sivaganga'+'/Q'+str(random.randint(400000, 500000))+'/TN'

district_number = dict_data.pop('sri ganganagar/Q1419696')
matched_districts[district_number] = 'ganganagar'+'/Q'+str(random.randint(400000, 500000))+'/RJ'

district_number = dict_data.pop('the dangs/Q1135616')
matched_districts[district_number] = 'dang'+'/Q'+str(random.randint(400000, 500000))+'/GJ'

district_number = dict_data.pop('the nilgiris/Q15188')
matched_districts[district_number] = 'nilgiris'+'/Q'+str(random.randint(400000, 500000))+'/TN'

district_number = dict_data.pop('thoothukudi/Q15198')
matched_districts[district_number] = 'thoothukkudi'+'/Q'+str(random.randint(400000, 500000))+'/TN'

district_number = dict_data.pop('tiruchchirappalli/Q15201')
matched_districts[district_number] = 'tiruchirappalli'+'/Q'+str(random.randint(400000, 500000))+'/TN'

district_number = dict_data.pop('tirunelveli kattabo/Q15200')
matched_districts[district_number] = 'tirunelveli'+'/Q'+str(random.randint(400000, 500000))+'/TN'

district_number = dict_data.pop('tiruvanamalai/Q15207')
matched_districts[district_number] = 'tiruvannamalai'+'/Q'+str(random.randint(400000, 500000))+'/TN'

district_number = dict_data.pop('tumkur/Q1301635')
matched_districts[district_number] = 'tumakuru'+'/Q'+str(random.randint(400000, 500000))+'/KA'

district_number = dict_data.pop('yadagiri/Q1786949')
matched_districts[district_number] = 'yadgir'+'/Q'+str(random.randint(400000, 500000))+'/KA'

district_number = dict_data.pop('ysr/Q15342')
matched_districts[district_number] = 'y.s.r. kadapa'+'/Q'+str(random.randint(400000, 500000))+'/AP'


district_number = dict_data.pop('adilabad/Q15211')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('bhadradri kothagudem/Q28169767')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('hyderabad/Q15340')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('jangaon/Q28170170')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('jogulamba gadwal/Q27897618')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('jayashankar bhupalapally/Q28169775')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('kamareddy/Q27956125')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('karimnagar/Q15373')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('khammam/Q15371')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('komram bheem/Q28170184')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('mahabubabad/Q28169761')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('mahabubnagar/Q15380')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('mancherial/Q28169747')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('medak/Q15386')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('medchal–malkajgiri/Q27614841')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('mulugu/Q61746006')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('nalgonda/Q15384')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('narayanpet/Q61746013')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('nirmal/Q28169750')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('nizamabad/Q15391')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('peddapalli/Q27614797')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('rajanna sircilla/Q28172781')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('rangareddy/Q15388')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('sangareddy/Q28169753')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('siddipet/Q28169756')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('suryapet/Q28169770')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('vikarabad/Q28170173')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('wanaparthy/Q28172504')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('warangal rural/Q28169759')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'
district_number = dict_data.pop('warangal urban/Q213077')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TG'

district_number = dict_data.pop('baksa/Q2360266')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('barpeta/Q41249')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('bishwanath/Q28110722')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('bongaigaon/Q42197')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('cachar/Q42209')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('charaideo/Q24039029')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('chirang/Q2574898')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('darrang/Q42461')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('dhubri/Q42485')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('dhemaji/Q42473')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('dibrugarh/Q42479')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('dima hasao/Q42774')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('east karbi anglong/Q42558')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('goalpara/Q42522')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('golaghat/Q42517')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('hailakandi/Q42505')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('kamrup/Q2247441')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('hojai/Q24699407')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('kamrup metropolitan/Q2464674')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('karimganj/Q42542')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('kokrajhar/Q42618')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('majuli/Q28110729')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('marigaon/Q42737')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('nagaon/Q42686')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('nalbari/Q42779')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('sivasagar/Q42768')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('sonapur/Q1473957')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('sonitpur/Q42765')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('south salmara-mankachar/Q24907599')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('tinsukia/Q42756')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('west karbi anglong/Q24949218')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'
district_number = dict_data.pop('jorhat/Q42611')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/AS'


district_number = dict_data.pop('chandel/Q2301769')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/MN'
district_number = dict_data.pop('churachandpur/Q2577281')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/MN'
district_number = dict_data.pop('imphal east/Q1916666')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/MN'
district_number = dict_data.pop('imphal west/Q1822188')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/MN'
district_number = dict_data.pop('jiribam/Q28419387')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/MN'
district_number = dict_data.pop('kakching/Q28173825')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/MN'
district_number = dict_data.pop('kamjong/Q28419390')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/MN'
district_number = dict_data.pop('kangpokpi/Q28419386')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/MN'
district_number = dict_data.pop('noney/Q28419389')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/MN'
district_number = dict_data.pop('pherzawl/Q28173809')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/MN'
district_number = dict_data.pop('senapati/Q2301706')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/MN'
district_number = dict_data.pop('tamenglong/Q2301717')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/MN'
district_number = dict_data.pop('tengnoupal/Q28419388')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/MN'
district_number = dict_data.pop('thoubal/Q2086198')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/MN'
district_number = dict_data.pop('ukhrul/Q735101')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/MN'


district_number = dict_data.pop('noklak/Q48731903')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/NL'

district_number = dict_data.pop('sepahijala/Q16086076')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/TR'

district_number = dict_data.pop('south sikkim/Q1805051')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/SK'
district_number = dict_data.pop('north sikkim/Q1784149')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/SK'
district_number = dict_data.pop('west sikkim/Q611357')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/SK'
district_number = dict_data.pop('east sikkim/Q1772832')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/SK'
district_number = dict_data.pop('north goa/Q108234')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/GA'
district_number = dict_data.pop('south goa/Q108244')
matched_districts[district_number] = 'unknown'+'/Q'+str(random.randint(400000, 500000))+'/GA'





neighbor_dis = data.copy()
for key, value in neighbor_dis.items():
    buff_val = key
    if "_" in key:
        buff_val = key.replace("_", " ")
    if " district" in buff_val:
        buff_val = buff_val.replace(" district", "")
    district_id = test.get(buff_val) 				
    district_name = matched_districts.get(district_id)
    if district_name:
        data[district_name] = data.pop(key)
    else:
        data.pop(key)

updated_neighbor_keys = data.copy()

for key, District_array in updated_neighbor_keys.items():
    array = []
    for district in District_array:
        buff_val = district
        if "_" in district:
            buff_val = district.replace("_", " ")
        if " district" in buff_val:
            buff_val = buff_val.replace(" district", "")
        district_id = test.get(buff_val) 		      
        district_name = matched_districts.get(district_id)
        if district_name:
            array.append(district_name)
    data[key] = array 

sample = matched_districts.copy()
for key, value in sample.items():
    district_name = matched_districts.pop(key)
    matched_districts[district_name] = key

# reverse_sample = data.copy()
# for key in reverse_sample.keys():
#     if len(key.split("/")) < 3:
#         data.pop(key)

sample1={}
sample_new=data.copy()
for key,district_list in sample_new.items():
    array_list= []
    for dis in district_list:
        if len(dis.split("/"))<3:
            district_list.remove(dis)
        elif (key.lower().split("/")[0])==(dis.lower().split("/")[0]) and (key.lower().split("/")[2]==dis.lower().split("/")[2]):
            district_list.remove(dis)
        else:
            array_list.append(dis)
    data[key]=array_list


data_copy_new=data.copy()
all_keys = data_copy_new.keys()
for key, district_array in data_copy_new.items():
    array=[]
    flag_to_add=False
    for inner_keys in all_keys:
        if inner_keys == key or (key not in data.keys()):
            continue
        if key.split("/")[0].lower()==inner_keys.split("/")[0].lower() and key.split("/")[2].lower()==inner_keys.split("/")[2].lower():
            list_dist=data.pop(inner_keys)
            flag_to_add=True
            if len(list_dist)>0:
                for dist in list_dist:
                    array.append(dist)
    if len(array)>0 and flag_to_add:
        data[key]=list(set(array))

some_copy_of_data=data.copy()
for key, district_arr in some_copy_of_data.items():
    array=[]
    flag_to_add=False
    for dist in district_arr:
        if dist in some_copy_of_data.keys():
            flag_to_add=True
            array.append(dist)
        else:
            for keys in some_copy_of_data.keys():
                if keys.split("/")[0].lower()==dist.split("/")[0].lower() and keys.split("/")[2].lower()==dist.split("/")[2].lower():
                    flag_to_add=True
                    array.append(keys)
                    break

    if len(array)>0 and flag_to_add:
        data[key]=list(set(array))


sample = dict(sorted(matched_districts.items()))

k=101
for key in sample.keys():
    matched_districts.pop(key)
    if key in data.keys():
        matched_districts[key] = k
        k = k+1

with open('output.json', 'w') as fp:
    json.dump(matched_districts, fp)

with open('neighbor-district-modified.json', 'w') as fp:
    json.dump(data, fp)




