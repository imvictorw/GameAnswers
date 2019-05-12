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
    #urlString = "http://www.ug.it.usyd.edu.au/~lcha1115/testserver/register.cgi?username=snowwhite&relationship=single"
    from urlparse import urlparse, parse_qs
    qs = urlparse(urlString).query
    dataJson = parse_qs(qs)

    # INSERTING username and password into users table
    userName = dataJson.get('username')[0]
    
    cursor = conn.cursor()
    # INSERTING other field/values into profile table
    dictionary = dict(dataJson)
    for key in dictionary:
        if key != 'username':
            if key != 'passd':
                if (len(dictionary[key])) == 1:
                    cursor.execute("INSERT INTO profile(username_fk, field, val) VALUES (%s, %s, %s)", (userName, key, dictionary[key][0]))
                else:  
                    cursor.execute("INSERT INTO profile(username_fk, field, val) VALUES (%s, %s, %s)", (userName, key, dictionary[key]))

    conn.commit()
    print "success"
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
