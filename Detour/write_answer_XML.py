'''
Created on May 29, 2013

@author: Deja-Vu
'''
import xml.etree.ElementTree as xml
from xml import etree
from lxml import etree
import shutil
import os
from pprint import PrettyPrinter

class XML:
    def __init__(self):
        self.tree = ""
        
    def write_XML(self, data_list):
        print data_list
        #data_list contains id, question_number and received_answer
        id_list=[]
        
        for item in data_list:
            #add all the IDs from the data_list inro id_list
            id_list.append(item.id)
                  
        #a skeleton of answer XML is already created containg tags and attribute names
        #the XML skeleton is copied into another file with name "XML'id_list[0]" in which the answers will be filled
        current_path = os.path.dirname(__file__)
        parent_folder = os.path.abspath(os.path.join(current_path, os.pardir))
        xml_folder = os.path.normpath(os.path.join(parent_folder, "XML_files"))
        shutil.copy2(os.path.join(xml_folder, "Answer_XML_skeleton.xml"), os.path.join(xml_folder,"XML%s.xml"%id_list[0]))
        
        path = os.path.join(xml_folder,"XML%s.xml"%id_list[0])
        print "11231239123123981209381092380192830912830812938102938"
        print path
        print "11231239123123981209381092380192830912830812938102938"
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(path,parser)
        root = tree.getroot()
        #first filling the value of tag attributes(eg <data id="value">) from the received answer SMS
        for element in root.iter():
            attribute = element.attrib
            for item in attribute:
                for item1 in data_list:
                        #print "item ="+item, "question_number="+str(item1.question_number)
                        
                        #to avoid conflict, the attribute "id" of "data" tag is stored as "dataID"
                        #check if "dataID" is encountered in the data list
                        if item == "id" and item1.question_number == "dataID":
                            #if encountered, add the value of received answer to the value of "id" attribute
                            element.attrib[item] = item1.received_answer
                        if item == str(item1.question_number):
                            #check if the attribute name from the answer XML skeleton matches the item from the data_list
                            if item1.received_answer == "X":
                                #if received answer contains "X" then nothing is stored as the value of attribute
                                continue
                            #otherwise the the received answer is stored as the value of the attribute
                            element.attrib[item] = item1.received_answer 
        
        #filling the data items(eg <QN_470_0>data</QN_470-0>
        for element in root:
            root1 = element
            #counter to make sure that data is inserted one after another rather than one before another
            count = 0
            for item in data_list:
                if item.question_number.startswith("QN"):
                    #check if the received_answer is "-", if true it confirms the presence of tags of group or matrix 
                    if item.received_answer == "-":
                        #no need to add the data to the XML, so SKIP
                        continue
                    #if received answer contains data, then make the corresponding question_number a tag
                    elem = etree.Element(str(item.question_number))
                    #and store the received_answer as the text of the same tag
                    elem.text = str(item.received_answer)
                    #insert the tag into the XML file one after another
                    #count defines where to insert in the XML file
                    root1.insert(count,elem)
                    count=count+1
        
        #finally write the data into the XML file
        tree.write(path,pretty_print=True)
        return id_list[0]
        
                        