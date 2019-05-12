import psycopg2
import sys
import cgi
import cgitb
import os

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
    cursor = conn.cursor()
    
    # Group name
    groupName = dataJson.get('groupname')[0]
    
    # INSERTING other field/values into profile table
    dictionary = dict(dataJson)
    for key in dictionary:
        if key != 'groupname':
            if (len(dictionary[key])) == 1:
                cursor.execute("INSERT INTO groupProfile(groupName_fk, field, val) VALUES (%s, %s, %s)", (groupName, key, dictionary[key][0]))
            else:  
                cursor.execute("INSERT INTO groupProfile(groupName_fk, field, val) VALUES (%s, %s, %s)", (groupName, key, dictionary[key]))
    
    print "success"
    conn.commit()  
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
