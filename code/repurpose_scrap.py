from dateutil import parser
import json


DF_HEADER = 'title,subtitle,author,time,section,text,url'
ENCODING = 'utf8'


def unpack_json(path):

    data = None
    with open(path, encoding=ENCODING) as json_file:
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


def del_junk_chars(excerpt):
   if excerpt:
       excerpt = excerpt.replace(',',' ')
       excerpt = ''.join(c for c in excerpt if c not in '\r\t\n')
   return excerpt
  

def scrap_to_csv(scrap):
    for k,v in scrap.items():
        line = "{0},{1},{2},{3},{4},{5},{6}" \
                .format(del_junk_chars(v["title"]),
                        del_junk_chars(v["subtitle"]),
                        del_junk_chars(v["author"]),
                        conform_date(v["time"]),
                        del_junk_chars(v["section"]),
                        del_junk_chars(conform_text(v["text"])), k)
        return line


data = unpack_json('../output/elpais.json')

with open('../output/results.csv', 'w', encoding=ENCODING) as f:

    f.write("{}\n".format(DF_HEADER))
    
    for scrap in data:
        f.write("{}\n".format(scrap_to_csv(scrap)))

