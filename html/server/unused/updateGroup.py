import psycopg2
import psycopg2.extras
import sys
import cgi
import cgitb
import os
import json

cgitb.enable()
#print "Content-type:text/html\r\n\r\n"
print 'Content-Type: text/plain\r\n\r'

try:
    conn = psycopg2.connect("dbname='info1003_project' user='info1003user' host='postgres.it.usyd.edu.au' password='userpj1003'")
    # Parsing input data
    urlString = "?" + os.environ['QUERY_STRING']
    #urlString = "?groupname=pokemon&newname=marioRules&descript=pokemon+dudes"
    from urlparse import urlparse, parse_qs
    qs = urlparse(urlString).query
    dataJson = parse_qs(qs)
    groupName = dataJson.get('groupname')[0]
    cursor = conn.cursor()

    # New Name
    if 'newname' in dataJson:
        folName = dataJson.get('newname')[0]
        folName2 = "'" + folName + "'"
        
        #cursor.execute("DELETE FROM groups WHERE groupName = '" + groupName + "'")
        cursor.execute("INSERT INTO groups(groupname) VALUES ('" + folName +"')")
        cursor.execute("UPDATE membership SET groupname_fk = '" + folName + "' WHERE groupName_fk = '" + groupName + "'")
        cursor.execute("UPDATE groupprofile SET groupname_fk = '" + folName + "' WHERE groupName_fk = '" + groupName + "'")
        #cursor.execute("UPDATE groups SET groupName = '" + folName + "' WHERE groupName = '" + groupName + "'")
        cursor.execute("DELETE FROM groups WHERE groupName = '" + groupName + "'")
        conn.commit()
        groupName = folName
    
    # OTHER VALUES
    dictionary = dict(dataJson)
    for key in dictionary:
        if key != 'groupname':
            if key != 'newname':
                if (len(dictionary[key])) == 1:
                    cursor.execute("UPDATE groupProfile SET val = '" + dictionary[key][0] + "' WHERE groupName_fk = '" + groupName + "' AND field = '" + key + "'")
                else:  
                    cursor.execute("UPDATE groupProfile SET val = " + dictionary[key] + " WHERE groupName_fk = '" + groupName + "' AND field = '" + key + "'")

    conn.commit()
    print "success"
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
