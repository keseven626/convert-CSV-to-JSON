import csv
import json

def buildJSON(csvPath, jsonPath):
    obj = {}
    with open(csvPath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        
    with open(jsonPath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(obj, indent=4))
    
csvFilePath = r'Names.csv'
jsonFilePath = r'Names.json'

# Call the make_json function
buildJSON(csvFilePath, jsonFilePath)