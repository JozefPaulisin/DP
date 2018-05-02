from datetime import datetime
from elasticsearch import Elasticsearch
import json

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
data = json.load(open('test21.json'))
counter = 1
fmt = '%Y-%m-%d %H:%M:%S'

def resolveStateName(stateId):
    if (stateId == 410):
        return "Absencia"
    elif (stateId == 411):
        return "Prebudenie"
    elif (stateId == 412):
        return "Neurcity stav"
    elif (stateId == 413):
        return "Spanok"
    elif (stateId == 414):
        return "Prerusenie spanku"
    elif (stateId == 415):
        return "Predsien - aktivita"
    elif (stateId == 416):
        return "Kuchyna - aktivita"
    elif (stateId == 417):
        return "Obyvacia izba - aktivita"
    elif (stateId == 418):
        return "Prechodna chodba - aktivita"
    elif (stateId == 419):
        return "Zachod - aktivita"
    elif (stateId == 420):
        return "Kupelna - aktivita"
    elif (stateId == 421):
        return "Spalna - aktivita"
    elif (stateId == 422):
        return "Predsien - pasivita"
    elif (stateId == 423):
        return "Kuchyna - pasivita"
    elif (stateId == 424):
        return "Obyvacia izba - pasivita"
    elif (stateId == 425):
        return "Prechodna chodba - pasivita"
    elif (stateId == 426):
        return "Zachod - pasivita"
    elif (stateId == 427):
        return "Kupelna - pasivita"
    elif (stateId == 428):
        return "Spalna - pasivita"
    else:
        return"UNKNOWN"


for item in data:

    begin_value = item["begin"]
    end_value = item["end"]
    id_value = item["id"]

    if (begin_value is None or end_value is None):
        continue

    begin = datetime.strptime(begin_value, fmt)
    end = datetime.strptime(end_value, fmt)

    time_difference = end - begin
    time_difference_minutes = int(round(time_difference.total_seconds()/60))

    pair = {'duration': time_difference_minutes}
    item.update(pair)

    state_id_value = item["state_id"]
    pair = {'state_name': resolveStateName(state_id_value)}
    item.update(pair)

    pair = {'record_name': str(id_value) + ' ' + resolveStateName(state_id_value)}
    item.update(pair)

    print("after", item)

    es.index(index="test99", doc_type="test-type", id=counter, body=item)
    counter+=1
pprint(data)
