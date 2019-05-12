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
    #urlString = "?username=pikachu&collectionname=Temp&objectname=My+New+Theme&location=www.ug.it.usyd.edu.au/~info1003/pikachu.mp3"
    from urlparse import urlparse, parse_qs
    qs = urlparse(urlString).query
    dataJson = parse_qs(qs)
    
    # Extract Message Data
    userName = dataJson.get('username')[0]
    objName = dataJson.get('objectname')[0]
    
    colName = ['objectId_pk', 'ownerId_fk', 'collectName_fk', 'objectName', 'field', 'val']
    
    cursor = conn.cursor()
    # Retrieve data object
    cursor.execute("SELECT objects.*, field, val FROM objects INNER JOIN objectdescript ON objectid_pk = objectid_fk WHERE ownerid_fk = '" + userName + "'")
    records = cursor.fetchall()
    
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
