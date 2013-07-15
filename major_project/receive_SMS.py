'''
Created on May 28, 2013

@author: Deja-Vu
'''

class SMS:
    def return_SMS(self):
        SMS_from_tablet = "1604204000 4/25/2013 1 333 X 4/9/2013#12:00:00#AM 1$2 1 1 X PulchowkLalitpur IOE1 3 father 40|50|1 22|33|2 55|55|1 55|55|1 X X 1669004051 IOE1 Y X 268 X 1169 X X X X X"
        SMS_from_public = "Disaster"
        SMS_member_list = SMS_from_tablet.split(" ")
        return SMS_member_list
