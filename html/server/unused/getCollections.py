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
    #urlString = "?username=pikachu&collectionname=Trash&descript=Trash+Docs"
    from urlparse import urlparse, parse_qs
    qs = urlparse(urlString).query
    dataJson = parse_qs(qs)
    
    # INSERTING collection name
    userName = dataJson.get('username')[0]
    
    cursor = conn.cursor()

    # Fetch unique key
    cursor.execute("""
    SELECT collection.*, field, val FROM collection INNER JOIN collectdescript
    ON collectionId_pk = collectionId_fk
    WHERE ownerid_fk = '""" + userName + "'")

    records = cursor.fetchall()

    colName = ['collectionId_pk', 'ownerId_fk', 'collectionName', 'field', 'val']
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

