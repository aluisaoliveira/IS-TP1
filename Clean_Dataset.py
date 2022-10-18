import csv

f = open('Clean_Dataset.csv')

csv_f = csv.reader(f)

data=[]

for row in csv_f:
    data.append(row)

f.close()

print(data[1:])

def convert_row(row):
    return  """<Plane>
<airline>%s</airline>
<flight>%s</flight>
<source_city>%s</source_city>
<departure_time>%s</departure_time>
<stops>%s</stops>
<arrival_time>%s</arrival_time>
<destination_city>%s</destination_city>
<class>%s</class>
<duration>%s</duration>
<days_left>%s</days_left>
<price>%s</price>
</Plane>""" % (row[0], row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])

with open('output.xml', 'w') as f:
    f.write('\n'.join([convert_row(row) for row in data]))