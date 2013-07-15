from database.models import public_sms, data_from_public

class public_sms:
    def __init__(self):
        complete_sms = " "
        
    def insert_sms_data(self, sms):
        description = ""
        sms_list = sms.split(" ", 4)
        description = sms_list[len(sms_list)-1]
        print description
        q1 = data_from_public(address = sms_list[2], disaster = sms_list[3], description = description)
        q1.save()
        
