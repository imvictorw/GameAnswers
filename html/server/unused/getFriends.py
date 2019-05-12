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
    #urlString = "?username=yoshi"
    from urlparse import urlparse, parse_qs
    qs = urlparse(urlString).query
    dataJson = parse_qs(qs)
    userName = dataJson.get('username')[0]
    userName = "'" + userName + "'"
    cursor = conn.cursor()
            
    # execute Query
    cursor.execute("SELECT frienduserid FROM friendship WHERE userid_fk = " + userName + "AND status = 'accept'")
    # retrieve the records from the database
    records = cursor.fetchall()
    #print records
    colName = ['friend']
    
    out = []
    for row in range(len(records)):
        out.append({})
        for j in range(len(records[row])):
            out[row][colName[j]] = records[row][j]

    jsonData = json.dumps(out)
    
    # Friend 2
    cur2 = conn.cursor()
    cur2.execute("SELECT userId_fk FROM friendship WHERE friendUserId = " + userName + "AND status = 'accept'")
    records2 = cur2.fetchall()
    
    out2 = []
    for row in range(len(records2)):
        out2.append({})
        for j in range(len(records2[row])):
            out2[row][colName[j]] = records2[row][j]

    jsonData2 = json.dumps(out2)
    
    for value in out:
       out2.append(value)

    jsonData3 = json.dumps(out2)
    print jsonData3
    
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
