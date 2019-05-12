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
    #urlString = "http://www.ug.it.usyd.edu.au/~lcha1115/testserver/acceptFriendship.cgi?username=dk&friendname=yoshi"
    #urlString = "?username=yoshi&friendname=dk"
    from urlparse import urlparse, parse_qs
    qs = urlparse(urlString).query
    dataJson = parse_qs(qs)
    dictionary = dict(dataJson)
    
    # INSERTING username and password into users table
    userAccepter = dataJson.get('username')[0]
    friendUser = dataJson.get('friendname')[0]
    acceptMess = userAccepter + " has accepted your friendship request"
	
    #from time import gmtime, strftime
    #sentTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    import datetime
    sentTime = datetime.datetime.now()
    
    #colName = ['messageId_pk', 'wallUserId_fk', 'senderId_fk', 'messageSubject', 'messageBody', 'sentTimestamp', 'field', 'val']
    
    cursor = conn.cursor()
    
    # Store friendship relation
    cursor.execute("UPDATE friendship SET status = 'accept' WHERE userId_fk = '" + friendUser + "' AND friendUserId = '" + userAccepter + "'")
	
    # Friendship notification 
    cursor.execute("""
    INSERT INTO messages(wallUserId_fk, senderId_fk, messageSubject, messageBody, sentTimestamp, messageType)
    VALUES (%s, %s, %s, %s, %s, %s)""", (friendUser, userAccepter, 'Friendship Accepted', acceptMess, sentTime, 'friendNotification'))
    
    #friend1 = "You are friends with " + wallUser
    #friend2 = "You are friends with " + senderUser
	
    # Feed update
    cursor.execute("""
    INSERT INTO feed(userFrom_fk, ownerId_fk, activityType, verb, action, createdAt)
    VALUES (%s, %s, %s, %s, %s, %s)""",
    (friendUser, userAccepter, 'friendship', 'are', 'friends with', sentTime))
	
    cursor.execute("""
    INSERT INTO feed(userFrom_fk, ownerId_fk, activityType, verb, action, createdAt)
    VALUES (%s, %s, %s, %s, %s, %s)""",
    (userAccepter, friendUser, 'friendship', 'are', 'friends with', sentTime))
	
    print "sucess"
    conn.commit()
    
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
