import csv, sys

def read_csv_noheader(filename):
    rdr = csv.reader(
        open(filename, encoding='cp1252'), 
        delimiter=';', 
        quotechar='"')

    for id, firstname, lastname, birth in rdr:
        yield {
            'id': int(id),
            'firstname': firstname,
            'lastname': lastname,
            'birth': birth,
        }

for record in read_csv_noheader(sys.argv[1]):
    print(f'ID:{record["id"]}, Firstname:{record["firstname"]}, Lastname:{record["lastname"]}, Date of birth: {record["birth"]}')

