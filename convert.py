import json
import csv 
import hashlib


def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf) 

        filename = csvFilePath
        sha256_hash = hashlib.sha256()
        with open(filename,"rb") as f:
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)

        # Do this to each row
        for row in csvReader:   
            # Checking each row to remove empty row
            if row['Filename'] != '' or row['Series Number'] != '':
                row.update({'sha256' : sha256_hash.hexdigest()})
                jsonArray.append(row)
  
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


fileInput = input('Enter Your CSV Flie name with (.csv):')
files = fileInput.split('.')
if files[1] != 'csv':
    print('==========================')
    print('==========================')
    print('This is not a Valid csv file!')
    print('==========================')
    print('==========================')
else:
    name = f'./{files[0]}'      
    csvFilePath = r"" f'{name}.csv' ""
    jsonFilePath = r"" f'{name}.json'""

    csv_to_json(csvFilePath, jsonFilePath)


