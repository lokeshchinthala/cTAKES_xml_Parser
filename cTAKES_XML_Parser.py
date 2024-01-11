#!/usr/bin/env python
# coding: utf-8

import xml.etree.ElementTree as ET
import csv
import os

def parseXML(xmlfile):
    
    #Create element tree object
    tree = ET.parse(xmlfile)
    
    #Get root element
    root = tree.getroot()
    
    #Create empty list
    csvItems = []
    
    for doc_id in root.findall('.//uima.cas.Sofa'):
        x = doc_id.get('sofaString')
        y = x.split(",", 1)
        docId = y[0]
        
    
    for type_tag in root.findall('.//org.apache.ctakes.typesystem.type.refsem.UmlsConcept'):
        items = {'DOC_ID':docId,'SCHEMA':type_tag.get('codingScheme'),'DRUG_NAME':type_tag.get('preferredText'),'CODE':type_tag.get('code'),'CUI':type_tag.get('cui')}
        
        csvItems.append(items)
    
    return csvItems

def savetoCSV(csvitems, filename):
    
    #Fields for csv file
    fields = ['DOC_ID', 'SCHEMA', 'CODE', 'DRUG_NAME', 'CUI']
    
    file_exists = os.path.isfile(filename)
    
    #Write to csv file
    with open(filename, 'a+') as csvfile:
        
        #Creating a CSV dict writer object
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        
        # writing headers (field names)
        if not file_exists:
            writer.writeheader()  # file doesn't exist yet, write a header
       
        # writing data rows
        writer.writerows(csvitems)


def main():
    
    directory = r'/path_to_xml_files/'
    
    for file in os.listdir(directory):
        if file.endswith(".xml"):
            
            #Parse XML
            csvitems = parseXML(os.path.join(directory,file))
            
            # store news items in a csv file
            savetoCSV(csvitems, '/Concepts.csv')
        
        else:
            continue

if __name__ == "__main__":
    
    # calling main function
    main()




