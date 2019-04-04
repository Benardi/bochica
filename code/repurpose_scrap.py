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


def conform_text(text):
    delimiter = ''
    joined = delimiter.join(text)
    return joined


def del_commas(excerpt):
   if excerpt is not None:
    excerpt = excerpt.replace(',',' ')

   return excerpt
  

def scrap_to_csv(scrap):
    for k,v in scrap.items():
        line = "{0},{1},{2},{3},{4},{5},{6}" \
                .format(del_commas(v["title"]),
                        del_commas(v["subtitle"]),
                        del_commas(v["author"]),
                        conform_date(v["time"]),
                        del_commas(v["section"]),
                        del_commas(conform_text(v["text"])), k)
        return line


data = unpack_json('../output/elpais.json')

with open('../output/results.csv', 'w') as f:

    f.write("{}\n".format(DF_HEADER))
    
    for scrap in data:
        f.write("{}\n".format(scrap_to_csv(scrap)))

