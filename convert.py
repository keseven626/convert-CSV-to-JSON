import csv
import json

def buildJSON(csvPath, jsonPath):
    obj = {}
    with open(csvPath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        
    with open(jsonPath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(obj, indent=4))
    
csvPath = r'csvFile.csv'
jsonPath = r'JsonFile.json'

# Call the make_json function
buildJSON(csvPath, jsonPath)
