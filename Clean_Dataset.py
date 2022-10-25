import csv

#Converter string para XML
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

def mainXML(fich):
    print(fich)
    # Abrir CVS e ler dados
    f = open(fich)
    f_csv = csv.reader(f)
    data = []


    # Substituir caracteres invalidos por algo valido
    for row in f_csv:
        tags = row

        for i in range(len(tags)):
            row[i] = row[i].replace('&', "and")
        data.append(row)

    f.close()
    # Test only
    #print('\n'.join([convert_row(row) for row in data[1:]]))

    # Escreve o XML num ficheiro
    with open('output.xml', 'w') as f: f.write(
        '<xml>\n' + '\n'.join([convert_row(row) for row in data[1:]]) + '\n</xml>\n')  # abrir ficheiro xml
# Ao abrir tem que verificar se o "no" principal esta aberto e fechado.

if __name__ == '__main__':
    try:
        mainXML("./Clean_Dataset.csv")
    # Catch exceptions
    except (Exception, ArithmeticError) as e:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(e).__name__, e.args)
        print(message)

