from dateutil import parser
import json, sys, pdb


DF_HEADER = 'title,subtitle,author,date,section,text,url'
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
  

def scrap_to_csv(item):
    line = "{0},{1},{2},{3},{4},{5},{6}" \
            .format(del_junk_chars(item["title"]),
                    del_junk_chars(item["subtitle"]),
                    del_junk_chars(item["author"]),
                    conform_date(item["date"]),
                    del_junk_chars(item["section"]),
                    del_junk_chars(conform_text(item["text"])),
                    item["url"])
    return line

def json_to_csv(orig, dest):
   data = unpack_json(orig)

   with open(dest, 'w', encoding=ENCODING) as f:

       f.write("{}\n".format(DF_HEADER))
    
       for scrap in data:
           f.write("{}\n".format(scrap_to_csv(scrap)))



# script arguments
data_source = sys.argv[1]
data_dest = sys.argv[2]

if len(sys.argv) < 3:
    print("Please provide a source and and destination file")

else:
    json_to_csv(data_source, data_dest)

