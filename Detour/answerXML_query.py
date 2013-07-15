'''
Created on May 27, 2013

@author: Deja-Vu
'''
from database.models import answer
from django.db import connection
import questionXML_query

class answerXML:
    def clear_answer_table(self):
        answer.objects.all().delete()
        
    def get_all_data(self):
        data_list = answer.objects.all()
        return data_list
    
    def get_id(self):
        cursor = connection.cursor()
        cursor.execute("""SELECT id FROM database_answer""")
        fetched_list  = cursor.fetchall()
        return fetched_list
        
        
    def fill_attributes(self, qn_attributes_list):
        data_attribute_list = ['dataID', 'date_of_visit', 'revision_no','field_monitor_id']
        respondent_attribute_list = ['wardno', 'address1', 'code', 'name', 'isnew', 'type', 'questionnairecode', 'monitoringplanid', 'sitecode', 'latitude', 'longitude', 'age', 'gender', 'parentid']
       
        for item in data_attribute_list:
            q1 = answer(question_number=item, received_answer = 'empty')
            q1.save()
        
        for item in qn_attributes_list:
            if 'group' in item:
                if 'subgroup' in item:
                    q1 = answer(question_number=item.rstrip('subgroup'), received_answer = 'hehe')
                else:
                    q1 = answer(question_number=item.rstrip('group'), received_answer = '-')
            elif 'matrix' in item:
                if 'matrixrow' in item:
                    q1 = answer(question_number=item.rstrip('matrixrow'), received_answer = 'hehe')
                else:
                    q1 = answer(question_number=item.rstrip('matrix'), received_answer = '-')
            else:
                q1 = answer(question_number=item, received_answer = 'hehe')
            q1.save()
        
        for item in respondent_attribute_list:
            q1 = answer(question_number=item, received_answer = 'hehe')
            q1.save()
            
    def fill_data(self, SMS_member_list,id_list):
        count = 0
        print SMS_member_list
        for item in id_list:
            record = answer.objects.get(id = item[0])
            if str(record.received_answer).startswith("-"):
                print "=============================="
                continue
            else:
                if count < len(SMS_member_list):
                    print "----------------------------------------------"
                    print "count= "
                    print len(SMS_member_list)
                    print count
                    print "----------------------------------------------"
                    print SMS_member_list[count]
                    record.received_answer = SMS_member_list[count]
                    record.save()
                    count = count + 1
            