import csv, sys

rdr = csv.DictReader(
    open(sys.argv[1], encoding='cp1252'), 
    delimiter=';', 
    quotechar='"')

for record in rdr:
    print(f'ID:{record["ID"]}, Firstname:{record["First name"]}, Lastname:{record["Last name"]}, Date of birth: {record["Date of Birth"]}')
