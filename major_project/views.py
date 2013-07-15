from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
import xml.etree.ElementTree as xml
import question_XML_read
import questionXML_query
import answerXML_query
import receive_SMS
import write_answer_XML
import add_public_sms
import os, sys
from django.core.context_processors import request
from major_project.add_public_sms import public_sms

def index(request):
    #t = get_template("template1.html")
    #html = t.render(Context({'aalu_mula': 'khoi aalu ho ki mula ho :P'}))
    return render(request, 'template1.html', {'aalu_mula': "heheheheheheheheheheeheh"})

def hello(request):
    return HttpResponse("Hello world")

def sms_submit(request):
    return render(request, 'sms_submit.html')

def search(request):
    send_sms = add_public_sms.public_sms()
    if 'sms_box' in request.GET and request.GET['sms_box']:
        sms = request.GET['sms_box']
        send_sms.insert_sms_data(sms)
        message = "aalu mula"
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

#module to obtain all the attributes list from the questionnaire XML

def process_questionnaire_xml(request):
    current_path = os.path.dirname(__file__)
    parent_folder = os.path.abspath(os.path.join(current_path, os.pardir))
    xml_folder = os.path.normpath(os.path.join(parent_folder, "XML_files"))
    print "--------------"
    print xml_folder
    attribute_reader = question_XML_read.XML() 
    attributes_list = attribute_reader.get_attributes(os.path.join(xml_folder, "Question_XML.xml")) #get attributes from the Question_XML.xml
   
   #fill the questionnaire table 
    prepare_questionnaire_table = questionXML_query.questionXML()
   #prepare the questionnaire table for a new questionnaire
    prepare_questionnaire_table.clear_question_table()
   #populate the questionnaire table with the attributes list
    prepare_questionnaire_table.insert_attributes(attributes_list)
   
   #fill the answer table
    fill_answer_table = answerXML_query.answerXML()
   #prepare the answer table for a new answer retrieval
    fill_answer_table.clear_answer_table()
   #populate the answer table with the attributes list
    fill_answer_table.fill_attributes(attributes_list)
   
    return render(request, 'template1.html', {'qncode_list': attributes_list})
#module to receive the answer SMS and read the member lists in it 
def process_SMS(request):
    SMS_receiver = receive_SMS.SMS()
    received_SMS_member_list = SMS_receiver.return_SMS() #store each member list from the received SMS in received_SMS_member_list
    
    #get corresponding ID of the stored records from the answer table
    get_id_list = answerXML_query.answerXML()
    id_list = get_id_list.get_id()
    
    fill_answer_table = answerXML_query.answerXML()
    #call the fill_data module with parameters received_SMS_member_list and id_list to store the received SMS into the answer table.
    fill_answer_table.fill_data(received_SMS_member_list,id_list)
    
    return render(request, 'template2.html', {'SMS': received_SMS_member_list})

#module to write the data from the answer table into the answer XML
def write_XML(request):
    #get the stored data from the answer table
    get_data_list = answerXML_query.answerXML()
    data_list = get_data_list.get_all_data()
    
    xml_writer = write_answer_XML.XML()
    #call the write_XML module to write the data_list to corresponding XML
    #to create the XML file with a random name everytime, 
    #the ID corresponding to first data item from answer table is extracted and XML is named as "XML'id_list[0]'"
    answer_xml_number = xml_writer.write_XML(data_list) 
    #return render(request, 'template3.html', {'message': answer_xml})
    
    #trying to display the contents of answer XML in the browser itself
    xml_filename = "XML%s.xml"%answer_xml_number
    current_path = os.path.dirname(__file__)
    parent_folder = os.path.abspath(os.path.join(current_path, os.pardir))
    xml_folder = os.path.normpath(os.path.join(parent_folder, "XML_files"))
    fo = open(os.path.join(xml_folder, "%s"%xml_filename),"r")
    return render(request, 'template3.html', {'message': fo.read()})
    #contents of XML file is displayed, but not pretty printed
    #return HttpResponse(open("E:/aptana workspace/test_server/XML_files/%s"%xml_filename).read())

        
