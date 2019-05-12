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
    #urlString = "?username=pikachu&collectionname=Trash"
    from urlparse import urlparse, parse_qs
    qs = urlparse(urlString).query
    dataJson = parse_qs(qs)
    #print dataJson
    # INSERTING collection name
    userName = dataJson.get('username')[0]
    colName = dataJson.get('collectionname')[0]

    import datetime
    sentTime = datetime.datetime.now()
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO collection(ownerId_fk, collectionName) VALUES (%s,%s)", (userName, colName))

    # Fetch unique key
    cursor.execute("SELECT collectionId_pk FROM collection WHERE ownerId_fk = '" + userName + "' AND collectionName = '" + colName + "'")
    colId = cursor.fetchone()
    #print colId[0]
    
    # INSERTING other field/values into collectiondescript table
    dictionary = dict(dataJson)
    for key in dictionary:
        if key != 'username':
            if key != 'collectionname':
                if (len(dictionary[key])) == 1:
                    cursor.execute("INSERT INTO collectDescript(collectionId_fk, field, val) VALUES (%s, %s, %s)", (colId, key, dictionary[key][0]))
                else:  
                    cursor.execute("INSERT INTO collectDescript(collectionId_fk, field, val) VALUES (%s, %s, %s)", (colId, key, dictionary[key]))

    # INSERT into feed
    cursor.execute("""
    INSERT INTO feed(userFrom_fk, ownerId_fk, activityType, verb, action, createdAt)
    VALUES (%s, %s, %s, %s, %s, %s)""",
    (userName, userName, 'collection', 'created a collection: ', colName, sentTime))
    
    print "success"
    conn.commit()  
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))

