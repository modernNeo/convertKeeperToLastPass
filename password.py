# name,username,password,url,notes

import csv

f= open("/path/to/output/csv/for/lastpass","w+")

f.write("url,username,password,extra,name,grouping,fav\n")
#f.write("http://url,username,password,notes,name,folder,0")
with open('/path/to/exported/csv/from/keeper', 'r',encoding='utf-8-sig') as csvFile:
  reader = csv.reader(csvFile)
  for row in reader:
      folder = row[0].strip()
      name = row[1].strip()
      username = row[2].strip()
      password = row[3].strip()
      url = row[4].strip()
      notes = row[5].strip()

      line = url+',' if url is not None else ','
      line += username+',' if username is not None else ','
      line += password+',' if password is not None else ','
      line += notes+',' if notes is not None else ','
      line += name+',' if name is not None else ','
      line += folder+'\n' if folder is not None else '\n'
      f.write(line)

csvFile.close()
f.close()
