from dateutil import parser
import json


DF_HEADER = 'title,subtitle,author,time,section,text,url'

def unpack_json(path):

    data = None
    with open(path) as json_file:
        data = json.load(json_file)
    
    return data

def conform_date(date):
   time = parser.parse(date)
   formatted = time.strftime('%d/%m/%Y %H:%M:%S')
   return formatted

def scrap_to_csv(scrap):
    for k,v in scrap.items():
        line = "{},{},{},{},{},{},{}" \
                .format(v["title"], v["subtitle"], v["author"],
                        conform_date(v["time"]), v["section"],
                        v["text"], k)
        return line


data = unpack_json('../output/elpais.json')

with open('../output/results.csv', 'w') as f:

    f.write("{}\n".format(DF_HEADER))
    
    for scrap in data:
        f.write("{}\n".format(scrap_to_csv(scrap)))

