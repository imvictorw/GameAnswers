import psycopg2
import sys
import cgi
import cgitb
import os

cgitb.enable()
print 'Content-Type: text/plain\r\n\r'

try:
    conn = psycopg2.connect("dbname='info1003_project' user='info1003user' host='postgres.it.usyd.edu.au' password='userpj1003'")
    # Parsing form data
    urlString = "?" + os.environ['QUERY_STRING']
    #urlString = "?groupname=humansRule&member=mario"
    from urlparse import urlparse, parse_qs
    qs = urlparse(urlString).query
    dataJson = parse_qs(qs)
    
    # INSERTING group name
    groupName = dataJson.get('groupname')[0]
    member = dataJson.get('member')[0]
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO membership(groupName_fk, member) VALUES (%s, %s)", (groupName, member))
    conn.commit()
                   
    print "success"
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
