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
    #urlString = "http://www.ug.it.usyd.edu.au/~lcha1115/testserver/sendMessage.cgi?wallUserId_fk=pikachu&senderId_fk=yoshi&messageSubject=hiiii&messageBody=weep+weep"
    from urlparse import urlparse, parse_qs
    qs = urlparse(urlString).query
    dataJson = parse_qs(qs)
    dictionary = dict(dataJson)
    
    # Extract Message Data
    wallUser = dataJson.get('wallUserId_fk')[0]
    senderUser = dataJson.get('senderId_fk')[0]
    messSub = dataJson.get('messageSubject')[0]
    messBody = dataJson.get('messageBody')[0]
    
    #from time import gmtime, strftime
    #sentTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    import datetime
    sentTime = datetime.datetime.now()
    #print sentTime
    #colName = ['messageId_pk', 'wallUserId_fk', 'senderId_fk', 'messageSubject', 'messageBody', 'sentTimestamp', 'field', 'val']
    
    cursor = conn.cursor()
    
    # MessageType option
    if 'messageType' in dataJson:
        messT = dataJson.get('messageType')[0]
        cursor.execute("""
        INSERT INTO messages(wallUserId_fk, senderId_fk, messageSubject, messageBody, sentTimestamp, messageType)
        VALUES (%s, %s, %s, %s, %s, %s)""", (wallUser, senderUser, messSub, messBody, sentTime, messT))
    else:
        cursor.execute("""
        INSERT INTO messages(wallUserId_fk, senderId_fk, messageSubject, messageBody, sentTimestamp)
        VALUES (%s, %s, %s, %s, %s)""", (wallUser, senderUser, messSub, messBody, sentTime))

    # Insert into news feed	
    if wallUser != senderUser:
        cursor.execute("""
        INSERT INTO feed(userFrom_fk, ownerId_fk, activityType, verb, action, createdAt)
        VALUES (%s, %s, %s, %s, %s, %s)""", (senderUser, wallUser, 'message', 'sent a message: ', messSub, sentTime))
    conn.commit()
    print "success"
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
