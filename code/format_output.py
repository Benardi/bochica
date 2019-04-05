import json, sys

from chronological import conform_date

HEADER = 'title,subtitle,author,date,section,text,url'
ENCODING = 'utf8'


def unpack_file(path, encoding):

    data = None
    with open(path, encoding=encoding) as f:
        data = json.load(f)
    
    return data


def del_junk_chars(excerpt):

   if excerpt:
       excerpt = excerpt.replace(',',' ')
       excerpt = ''.join(c for c in excerpt if c not in '\r\t\n')
   return excerpt
  

def format_item_as_csv(item):

    line = "{0},{1},{2},{3},{4},{5},{6}" \
            .format(del_junk_chars(item["title"]),
                    del_junk_chars(item["subtitle"]),
                    del_junk_chars(item["author"]),
                    conform_date(item["date"]),
                    del_junk_chars(item["section"]),
                    del_junk_chars((''.join(item["text"]))),
                    item["url"])
    return line


def export_json_as_csv(source, dest):

   data = unpack_file(source, ENCODING)

   with open(dest, 'w', encoding=ENCODING) as f:

       f.write("{}\n".format(HEADER))
    
       for item in data:
           f.write("{}\n".format(format_item_as_csv(item)))


if len(sys.argv) < 3:
   print("Please provide a source and destination file")

else:
   # script arguments
   data_source = sys.argv[1]
   data_dest = sys.argv[2]
   
   export_json_as_csv(data_source, data_dest)

