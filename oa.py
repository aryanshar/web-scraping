import urllib
import urllib2
import sys
import re

if(len(sys.argv) != 3):
    print ("Please run this as: python oa.py <initial> <final>")
    print ("Use python2")
    exit()

try:
    initial = int(sys.argv[1])
    final = int(sys.argv[2])+1
    assert initial < final

except:
    print ("Enter valid roll numbers")

for i in range(initial,final):
    # Sending a get request to the URL
        html=urllib2.urlopen('http://oa.cc.iitk.ac.in/Oa/Jsp/OAServices/IITk_SrchRes.jsp?typ=stud&numtxt=%d&sbm=Y' %i)
        # Reading the response
        html=html.read()
        # Finding the name for a roll number
        beg=html.find('<b>Name: </b>')+len("<b>Name: </b>")
        # If no result found
        if(beg==len("<b>Name: </b>")-1):
            print ("Something went wrong for roll No %d " %i)
            print ("\n\n")
            continue
        end=html.find('</p>',beg)

        print ("Roll No :" + str(i))
        print ("Name : "+html[beg:end].strip())

        beg=html.find('<b>Program: </b>')+len("<b>Program: </b>")
        if(beg==len("<b>Program: </b>")-1):
            print ("Roll No %d invalid" %i)
            print ("\n\n")
            continue
        end=html.find('</p>',beg)
        print ("Program: "+html[beg:end].strip())

        beg=html.find('<b>Department: </b>')+len("<b>Department: </b>")
        if(beg==len("<b>Department: </b>")-1):
            print ("Roll No %d invalid" %i)
            print ("\n\n")
            continue
        end=html.find('</p>',beg)
        print ("Dept: "+html[beg:end].strip())

        # Find the hostel info for the current roll number
        beg=html.find('<b>Hostel Info: </b>')+len("<b>Hostel Info: </b>")
        if(beg==len("<b>Hostel Info: </b>")-1):
            print ("Roll No %d invalid" %i)
            print ("\n\n")
            continue
        end=html.find('<br>',beg)
        print ("Address : "+html[beg:end].strip())

        beg=html.find('<b> E-Mail: </b>')+len("<b> E-Mail: </b>")
        if(beg==len("<b> E-Mail: </b>")-1):
            print ("Roll No %d invalid" %i)
            print ("\n\n")
            continue
        end=html.find('</a>',beg)
        email = re.search('>(.*)', html[beg:end].strip()).group(1)
        print ("Email: " + email)

        print ("")
