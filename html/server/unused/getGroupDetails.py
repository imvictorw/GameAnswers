import psycopg2
import sys
import cgi
import cgitb
import os
import json

cgitb.enable()
print 'Content-Type: text/plain\r\n\r'

try:
    conn = psycopg2.connect("dbname='info1003_project' user='info1003user' host='postgres.it.usyd.edu.au' password='userpj1003'")
    # Parsing form data
    urlString = "?" + os.environ['QUERY_STRING']
    #urlString = "?groupname=humansRule&descript=Humans+Only!"
    from urlparse import urlparse, parse_qs
    qs = urlparse(urlString).query
    dataJson = parse_qs(qs)
    
    # INSERTING group name
    groupName = dataJson.get('groupname')[0]
          
    cursor = conn.cursor()
    cursor.execute("SELECT field, val FROM groupProfile WHERE groupName_fk = '" + groupName + "'")  
    records = cursor.fetchall()

    colName = ['field', 'val']
    
    out = []
    for row in range(len(records)):
        out.append({})
        for j in range(len(records[row])):
            out[row][colName[j]] = records[row][j]

    jsonData = json.dumps(out)
    print jsonData
    
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
