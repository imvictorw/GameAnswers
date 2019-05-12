import psycopg2
import psycopg2.extras
import sys
import cgi
import cgitb
import os
import json
import collections

cgitb.enable()
#print 'Content-Type: application/json\n'
print 'Content-Type: text/plain\r\n\r'

try:
    conn = psycopg2.connect("dbname='info1003_project' user='info1003user' host='postgres.it.usyd.edu.au' password='userpj1003'")
    # Parsing input data
    urlString = "?" + os.environ['QUERY_STRING']
    #urlString = "?username=pikachu"
    from urlparse import urlparse, parse_qs
    qs = urlparse(urlString).query
    dataJson = parse_qs(qs)
    userName = dataJson.get('username')[0]
    userName = "'" + userName + "'"
    # Display column names
    cursor = conn.cursor()
            
    # execute Query
    #cursor.execute("""
    #SELECT messages.*, field, val
    #FROM messages INNER JOIN profile ON username_fk = senderId_fk WHERE walluserid_fk = """ + userName + """
    #ORDER BY sentTimestamp ASC""")
    cursor.execute("""
    SELECT *
    FROM messages WHERE walluserid_fk = """ + userName + """
    ORDER BY sentTimestamp ASC""")
    # retrieve the records from the database
    records = cursor.fetchall()
    colName = ['messageId_pk', 'wallUserId_fk', 'senderId_fk', 'messageSubject', 'messageBody', 'sentTimestamp', 'messageType']
    
    out = []
    for row in range(len(records)):
        out.append({})
        for j in range(len(records[row])):
            out[row][colName[j]] = records[row][j]

    #for row in range(len(records)):
    #    a.append({})
	#for j in range(len(records[row])):
            #a[row][colName[j]] = records[row][j]
            
            #a[row].append(colName[j])
            #a[row].append(records[row][j])
    	
    #for row in records:
    #    for col in xrange(10):
    #        print colName[col], row[col]
    jsonData = json.dumps(out)
    print jsonData
    
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
