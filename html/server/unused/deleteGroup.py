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
    #urlString = "?groupname=humansRule&descript=Humans+Only!"
    from urlparse import urlparse, parse_qs
    qs = urlparse(urlString).query
    dataJson = parse_qs(qs)
               
    groupName = "'" + dataJson.get('groupname')[0] + "'"
    
    cursor = conn.cursor()
    
    # DELETING GROUP
    cursor.execute("DELETE FROM groupProfile WHERE groupName_fk = " + groupName)
    cursor.execute("DELETE FROM membership WHERE groupName_fk = " + groupName)
    cursor.execute("DELETE FROM groups WHERE groupName = " + groupName)
    conn.commit()
    print "success"
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
