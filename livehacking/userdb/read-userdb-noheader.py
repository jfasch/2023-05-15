import csv, sys

rdr = csv.reader(
    open(sys.argv[1], encoding='cp1252'), 
    delimiter=';', 
    quotechar='"')

for id, firstname, lastname, birth in rdr:
    print(f'ID:{id}, Firstname:{firstname}, Lastname:{lastname}, Date of birth: {birth}')
