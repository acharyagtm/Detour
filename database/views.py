 """
 
 tree = xml.parse("E:/hawa Backup/python test code/Question_XML.xml")

    root = tree.getroot()

    list = []
    for element in root.iter():
        for name,value in (element.items()):
            check = value.startswith("QN")
            if value.startswith("QN"):
                print ("%s = %r" % (name,value))
                list.append(value)
# Create your views here.
"""