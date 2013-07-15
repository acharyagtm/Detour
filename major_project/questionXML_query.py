'''
Created on May 27, 2013

@author: Deja-Vu
'''

from database.models import questionnaire

class questionXML:
    #module to clear the questionnaire table and prepare it for new questionnnaire
    def clear_question_table(self):
        questionnaire.objects.all().delete()
    
    #module to insert the attributes of new quesionnnaire into the questionnaire table
    def insert_attributes(self,attributes_list):
        for item in attributes_list:
            #check if 'group' is attached to the attribute
            if 'group' in item :
                #check if 'subgroup' is attached to the attribute
                if 'subgroup' in item:
                    #store type as 'subgroup' and store the attribute value into the question_number after removing the attached 'subgorup'
                    q1 = questionnaire(type="subgroup",question_number=item.rstrip('subgroup'))
                else:
                    #store type as 'group' and store the attribute value into the question_number after removing the attached 'group'
                    q1 = questionnaire(type="group",question_number=item.rstrip('group'))
            elif 'matrix' in item:
                if 'matrixrow' in item:
                    #store type as 'matrixrow' and store the attribute value into the question_number after removing the attached 'matrixrow'
                    q1 = questionnaire(type="matrixrow",question_number=item.rstrip('matrixrow'))
                else:
                    #store type as 'matrix' and store the attribute value into the question_number after removing the attached 'matrix'
                    q1 = questionnaire(type="matrix",question_number=item.rstrip('matrix'))
            else:
                #store type as 'xx'->normal and store the attribute value into the question_number
                q1 = questionnaire(type="xx",question_number=item)
            q1.save()
    
                
        