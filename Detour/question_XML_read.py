'''
Created on May 25, 2013

@author: Deja-Vu
'''
#!/u    sr/bin/python
# -*- coding: iso-8859-1 -*-
import os, sys
import xml.etree.ElementTree as xml

class XML:
    def __init__(self):
        self.tree = ""

    
    def get_attributes(self,path):
        self.path = path
        tree = xml.parse(path)
        root = tree.getroot()
        
        flag = False #to check the occurrence of new modules
        
        run_count = 0 #checks the occurrences of "controls" tag
        run = [] #stores the values of run_count
        run.append(run_count)
        
        position = 1
        
        group_position = []
        matrix_position = []
        normal_position = []
        
        group_list = []
        matrix_list = []
        normal_list = []
        final_list = []
        
        for element in root.iter():
            if element.tag.startswith("module"):
                root0=element
                for element in root0.iter():
                    if element.tag.startswith("controls"):
                        run_count = run_count + 1 #run_count incremented if "controls" tag is encountered
                        if run_count != run[len(run)-1]: #to store only the distinct values of run_count
                            run.append(run_count)
                        root1=element
                        for element in root1.iter():
                            for name, value in element.items():
                                if value.startswith("QN"):
                                    if element.tag.startswith("group"):
                                        if flag == False: #upon encountring a new group questionnaire, "new group" is added in the group_list
                                            if run[len(run)-1] != run[len(run)-2]:
                                                group_list.append("new group")
                                                flag = True
                                        group_list.append(value+"group")
                                        root2=element
                                        for element in root2.iter():
                                            if element.tag.startswith("sub"):
                                                root3 = element
                                                for element in root3.iter():
                                                    for name,value in element.items():
                                                        if value.startswith("QN"):
                                                            group_list.append(value+"subgroup")
                                    elif element.tag.startswith("matrix"):
                                        if flag == False:
                                            if run[len(run)-1] != run[len(run)-2]:
                                                matrix_list.append("new matrix")
                                                flag = True
                                        matrix_list.append(value+"matrix")
                                        root2=element
                                        for element in root2.iter():
                                            if element.tag.startswith("matrixrow"):
                                                root3 = element
                                                for element in root3.iter():
                                                    for name,value in element.items():
                                                        if value.startswith("QN"):
                                                            matrix_list.append(value+"matrixrow")                        
                                    else:
                                        underscore_location = value.find("_") #get the position of 1st underscore(_) in the questionnaire code(QN_470_1))
                                        if value.find("_",underscore_location+1,7)!=-1: #check if the digit in the code(eg - 470) is three digits??)
                                            if len(value) > 9: #if it is fulfilled, the questionnnaire code is for group or matrix, not normal one. eg - QN_470_0_1. so skip it.
                                                print "skipped = "+value
                                                continue    #skip
                                            else:
                                                if flag == False:
                                                    if run[len(run)-1] != run[len(run)-2]:
                                                        normal_list.append("new list")
                                                        flag = True
                                                print "unskipped = " + value
                                                normal_list.append(value) #otherwise it is the normal questionnnaire so add it to the normal_list
                                        elif value.find("_",underscore_location+1,7)==-1: #check if the digit in the code(eg - 470) is four digits??)
                                            if len(value)>10:
                                                print "unskipped = " + value
                                                continue
                                            else:
                                                print value
                                                normal_list.append(value)
                    flag = False                    
        print normal_list
        print "\n"
        print group_list
        print "\n"
        print matrix_list                                    
        
        for element in root.iter():
            if element.tag.startswith("module"):
                root0 = element
                for element in root0.iter():
                    if element.tag.startswith("controls"):
                        root1 = element
                        #print root1
                        for element in root1:
                            #print element.tag
                            if element.tag.startswith("group"):
                                group_position.append(str(position)+"group")
                                position = position + 1
                            elif element.tag.startswith("matrix"):
                                matrix_position.append(str(position)+"matrix")
                                position = position + 1
                            else:
                                normal_position.append(str(position)+"normal")
                                position = position + 1
                                break
        
        final_position_list = group_position + matrix_position + normal_position
        final_position_list.sort()
        
        for item in final_position_list:
            if "normal" in item:
                print "normal"
                new_normal_list = []
                if normal_list[0] == "new list":
                    normal_list.pop(0)
                #print normal_list
                for item in normal_list:
                    if item != "new list":
                        new_normal_list.append(item)
                    else:
                        break
                for item in normal_list:
                    if item != "new list":
                        normal_list.pop(0)
                new_normal_list.reverse()
                final_list = final_list + new_normal_list
            elif "group" in item:
                print "group"
                new_group_list = []
                if group_list[0] == "new group":
                    group_list.pop(0)
                for item in group_list:
                    if item != "new group":
                        new_group_list.append(item)
                    else:
                        break
                for item in group_list:
                    if item != "new group":
                        group_list.pop(0)
                final_list.append(new_group_list.pop(0))
                new_group_list.reverse()
                final_list = final_list + new_group_list
            elif "matrix" in item:
                print "matrix"
                new_matrix_list = []
                if matrix_list[0] == "new matrix":
                    matrix_list.pop(0)
                for item in matrix_list:
                    if item != "new matrix":
                        new_matrix_list.append(item)
                    else:
                        break
                for item in matrix_list:
                    if item != "new matrix":
                        matrix_list.pop(0)
                final_list = final_list + new_matrix_list
            
        print final_list
        return final_list

