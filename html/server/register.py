import psycopg2
import psycopg2.extras
import sys
import cgi
import cgitb
import os
import hashlib 

cgitb.enable()
print 'Content-Type: text/plain\r\n\r'

# METHOD to get whether hacked or not
def Code():
    try:
        conn = psycopg2.connect("dbname='info1003gp' user='info1003gp' host='postgres.it.usyd.edu.au' password='Wed23sYT'")
        urlString = "?" + os.environ['QUERY_STRING']
        from urlparse import urlparse, parse_qs
        qs = urlparse(urlString).query
        dataJson = parse_qs(qs)
        dictionary = dict(dataJson)

        # RETRIEVING username and password from form
        argUsername = dataJson.get('username')[0]
        argPassword = hashlib.sha256(dataJson.get('passwd')[0]).hexdigest()
        argEmail = dataJson.get('email')[0]

        # CHECKS for hacking strings
        hacked = False;

        if ">" in argUsername:
            hacked = True
        elif "<" in argUsername:
            hacked = True
        elif "'" in argUsername:
            hacked = True
        elif '"' in argUsername:
            hacked = True

        if ">" in argPassword:
            hacked = True
        elif "<" in argPassword:
            hacked = True
        elif "'" in argPassword:
            hacked = True
        elif '"' in argPassword:
            hacked = True
            
        if (hacked == True):
            print "hackattempt"
            return;

        # INSERTING username and password into users table
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ga_users(username, passwd, email) VALUES (%s, %s, %s)""", (argUsername, argPassword, argEmail))
        print "Attempting to commit"
        conn.commit()

        print "success"
    except:
        # Get the most recent exception
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        # Exit the script and print an error telling what happened.
        sys.exit("Database connection failed!\n ->%s" % (exceptionValue))

Code();
