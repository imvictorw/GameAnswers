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
    #urlString = "?username=pikachu&objectname=My+New+Theme&collectionname=Temp&newname=Theme&location=www.blah.com/pikachu/mp3"
    from urlparse import urlparse, parse_qs
    qs = urlparse(urlString).query
    dataJson = parse_qs(qs)
    userName = dataJson.get('username')[0]
    coll = dataJson.get('collectionname')[0]
    coll2 = "'" + coll + "'"
    objName = dataJson.get('objectname')[0]
    
    cursor = conn.cursor()
    if 'newname' in dataJson:
        folName = dataJson.get('newname')[0]
        cursor.execute("UPDATE objects SET objectname = '" + folName + "' WHERE collectname_fk = " + coll2 + " AND ownerid_fk = '" + userName + "' AND objectname = '" + objName + "'")
        conn.commit()
        objName = folName
    
    # Finding ID
    cursor.execute("SELECT objectid_pk FROM objects WHERE collectname_fk = " + coll2 + " AND ownerId_fk = '" + userName + "' AND objectname = '" + objName + "'")
    idCol = cursor.fetchone()
    #print idCol
    
    # OTHER VALUES
    dictionary = dict(dataJson)
    for key in dictionary:
        if key != 'username':
            if key != 'collectionname':
                if key != 'objectname':
                    if key != 'newname':
                        if (len(dictionary[key])) == 1:
                            #print key, dictionary[key][0], idCol[0]
                            cursor.execute("UPDATE objectdescript SET val = '" + dictionary[key][0] + "' WHERE objectid_fk = " + str(idCol[0]) + " AND field = '" + key + "'")
                        else:  
                            cursor.execute("UPDATE objectdescript SET val = '" + dictionary[key] + "' WHERE objectid_fk = " + str(idCol[0]) + " AND field = '" + key + "'")
    conn.commit()
    print "success"
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
