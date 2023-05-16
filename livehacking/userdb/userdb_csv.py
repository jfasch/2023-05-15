import csv


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

