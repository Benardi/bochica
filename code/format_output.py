"""
.. module:: format_output
   :synopsis: Conform scrap results to csv format (in utf-8).
.. moduleauthor:: Benardi <github.com/Benardi>
"""

import json, sys

from chronological import conform_date

HEADER = 'title,subtitle,author,date,section,text,url'
ENCODING = 'utf8'


def unpack_file(path, encoding):

    """ Extract json data from file.

    Extract json list from file.

    :param str path: source file path.
    :param str encoding: source file enconding.

    :return: list of json objects (dict) 

    :rtype: list
    """
    data = None
    with open(path, encoding=encoding) as f:
        data = json.load(f)
    
    return data


def del_junk_chars(excerpt):

   """ Remove unwanted chars from excerpt.

   Remove delimiters and special codes from excerpts.

   :param str excerpt: text to be stripped.

   :return: stripped text

   :rtype: str
   """
   if excerpt:
       excerpt = excerpt.replace(',',' ')
       excerpt = ''.join(c for c in excerpt if c not in '\r\t\n')
   return excerpt
  

def format_item_as_csv(item):

    """ Format scrap item into csv row.

    Format scrap item into clean and conforming csv row

    :param dict item: scrap item.

    :return: line in csv format

    :rtype: str
    """
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

   """ Convert json list to csv file.

   Format and export list of json as csv file

   :param str source: path to source file.
   :param str dest: path to destination file.

   :return: no return

   :rtype: None
   """
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

