import csv
from json import dumps


def main(filedir: str, outputfiledir: str):
    """Function used to convert the first positions obtained
    to a json file. The original file was manualy converted
    to a csv file before applying this function."""
    outdict = {}
    with open(filedir, 'r') as file:
        lines = csv.reader(file, delimiter=';')
        for line in lines:
            key, typepos, values = line
            outdict.setdefault(key, {})
            outdict[key][typepos] = values
    jsonstr = dumps(outdict, indent=4, sort_keys=True)
    with open(outputfiledir, 'w') as outfile:
        outfile.write(jsonstr)
