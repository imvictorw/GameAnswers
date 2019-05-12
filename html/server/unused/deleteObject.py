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
    #urlString = "?username=pikachu&objectname=Theme&collectionname=Temp&newname=Theme&location=www.blah.com/pikachu/mp3"
    from urlparse import urlparse, parse_qs
    qs = urlparse(urlString).query
    dataJson = parse_qs(qs)
    userName = dataJson.get('username')[0]
    coll = dataJson.get('collectionname')[0]
    coll2 = "'" + coll + "'"
    objName = dataJson.get('objectname')[0]

    cursor = conn.cursor()
    # Finding ID
    cursor.execute("SELECT objectid_pk FROM objects WHERE collectname_fk = " + coll2 + " AND ownerId_fk = '" + userName + "' AND objectname = '" + objName + "'")
    idCol = cursor.fetchone()
    
    cursor.execute("DELETE FROM objectdescript WHERE objectid_fk = " + str(idCol[0]))
    cursor.execute("DELETE FROM objects WHERE collectname_fk = " + coll2 + " AND ownerId_fk = '" + userName + "' AND objectname = '" + objName + "'")
    
    conn.commit()
    print "success"
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
