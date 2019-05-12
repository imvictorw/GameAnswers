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
    coll = dataJson.get('collectionname')[0]
    objName = dataJson.get('objectname')[0]

    #from time import gmtime, strftime
    #sentTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    import datetime
    sentTime = datetime.datetime.now()
    #print sentTime
    #colName = ['messageId_pk', 'wallUserId_fk', 'senderId_fk', 'messageSubject', 'messageBody', 'sentTimestamp', 'field', 'val']
    
    cursor = conn.cursor()
    # Insert object
    cursor.execute("INSERT INTO objects(ownerId_fk, collectName_fk, objectName) VALUES (%s, %s, %s)", (userName, coll, objName))
    conn.commit()
    # Get id
    cursor = conn.cursor()
    cursor.execute("SELECT objectId_pk FROM objects WHERE ownerId_fk = '" + userName + "' AND objectName = '" + objName + "'")
    colId = cursor.fetchone()
    #print colId[0]
    
    dictionary = dict(dataJson)
    for key in dictionary:
        if key != 'username':
            if key != 'collectionname':
                if key != 'objectname':
                    if (len(dictionary[key])) == 1:
                        cursor.execute("INSERT INTO objectDescript(objectId_fk, field, val) VALUES (%s, %s, %s)", (colId, key, dictionary[key][0]))
                    else:  
                        cursor.execute("INSERT INTO objectDescript(objectId_fk, field, val) VALUES (%s, %s, %s)", (colId, key, dictionary[key]))

    # Insert into news feed	
    cursor.execute("""
    INSERT INTO feed(userfrom_fk, ownerid_fk, activityType, verb, action, createdat)
    VALUES (%s, %s, %s, %s, %s, %s)""", (userName, userName, 'object', 'created an object: ', objName, sentTime))

    conn.commit()
    print "success"
     
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
