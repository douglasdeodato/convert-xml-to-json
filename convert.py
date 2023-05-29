import xmltodict
import json

def xml_to_json(xml_file, json_file):
    with open(xml_file, 'r', encoding='utf-8') as file:
        xml_data = file.read()

    xml_dict = xmltodict.parse(xml_data)
    json_data = json.dumps(xml_dict, indent=4)

    with open(json_file, 'w') as outfile:
        outfile.write(json_data)

# Example XML and JSON file paths
xml_file = 'file.xml'
json_file = 'file.json'

xml_to_json(xml_file, json_file)
