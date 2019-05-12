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
    #urlString = "http://www.ug.it.usyd.edu.au/~lcha1115/testserver/requestFriendship.cgi?username=yoshi&friendname=dk"
    from urlparse import urlparse, parse_qs
    qs = urlparse(urlString).query
    dataJson = parse_qs(qs)
    dictionary = dict(dataJson)
    
    # Extract Message Data
    userRequester = dataJson.get('username')[0]
    friendUser = dataJson.get('friendname')[0]
    requestMess = userRequester + " is requesting your friendship"
    
    #from time import gmtime, strftime
    #sentTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    import datetime
    sentTime = datetime.datetime.now()
    
    #colName = ['messageId_pk', 'wallUserId_fk', 'senderId_fk', 'messageSubject', 'messageBody', 'sentTimestamp', 'field', 'val']
    
    cursor = conn.cursor()
    
    # Store friendship relation
    cursor.execute("INSERT INTO friendship(userId_fk, friendUserId, status) VALUES (%s, %s, %s)", (userRequester, friendUser, 'request'))
	
    # Friendship notification 
    cursor.execute("""
    INSERT INTO messages(wallUserId_fk, senderId_fk, messageSubject, messageBody, sentTimestamp, messageType)
    VALUES (%s, %s, %s, %s, %s, %s)""", (friendUser, userRequester, 'Friendship Request', requestMess, sentTime, 'friendNotification'))
    
    # Feed update
    cursor.execute("""
    INSERT INTO feed(userFrom_fk, ownerId_fk, activityType, verb, action, createdAt)
    VALUES (%s, %s, %s, %s, %s, %s)""",
    (userRequester, friendUser, 'friendship', 'request', 'your friendship', sentTime))
	
    print "success"
    conn.commit()
    
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
