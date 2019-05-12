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
    #urlString = "?username=mario&aboutMe=loves+red+hats"
    from urlparse import urlparse, parse_qs
    qs = urlparse(urlString).query
    dataJson = parse_qs(qs)
    userName = dataJson.get('username')[0]
    cursor = conn.cursor()

    # OTHER VALUES
    dictionary = dict(dataJson)
    for key in dictionary:
        if key != 'username':
            if (len(dictionary[key])) == 1:
                cursor.execute("UPDATE profile SET val = '" + dictionary[key][0] + "' WHERE username_fk = '" + userName + "' AND field = '" + key + "'")
            else:  
                cursor.execute("UPDATE profile SET val = " + dictionary[key] + " WHERE username_fk = " + userName + " AND field = " + key)

    conn.commit()
    print "success"
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
