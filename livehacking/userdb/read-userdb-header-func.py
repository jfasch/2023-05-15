import csv, sys

def read_csv_header(filename):
    rdr = csv.DictReader(
        open(filename, encoding='cp1252'), 
        delimiter=';', 
        quotechar='"')

    for record in rdr:
        yield {
            'id': int(record['ID']),
            'firstname': record['First name'],
            'lastname': record['Last name'],
            'birth': record['Date of Birth'],
        }

for record in read_csv_header(sys.argv[1]):
    print(f'ID:{record["id"]}, Firstname:{record["firstname"]}, Lastname:{record["lastname"]}, Date of birth: {record["birth"]}')
