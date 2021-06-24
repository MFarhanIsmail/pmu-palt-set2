#palt python set 2
#question3
#Mohamad farhan bin ismail (20ddt19f1085)
def Question3():
    content = open('emailaddress.txt','r')
    contentcopy = open('emailaddress_copy.txt','w')
    editcontent = ""
    attemp = 1
    for eachline in content.readlines():
        remove_newline = eachline.rstrip("\n")
        if attemp == 1:
            editcontent += remove_newline
        else:
            editcontent += ";" + remove_newline
        attemp += 1

    print(editcontent)
    contentcopy.write(editcontent)
    contentcopy.close()
    content.close()
Question3()