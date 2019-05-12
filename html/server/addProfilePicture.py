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
        #dictionary = dict(dataJson)

        print dataJson

        # RETRIEVING username and password from form

        #avatar does not exist if user does not put stuff into prompt box like I was doing... it will therefore crash
        argPic = dataJson.get('avatar')[0]
        argUser = dataJson.get('username')[0]


        blah = "UPDATE ga_users SET avatar='%s' WHERE username = '%s'" % (argPic, argUser)

        #print blah
        # UPDATE user table
        cursor = conn.cursor()
        cursor.execute(blah)
        conn.commit()

        print "success"
    except:
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        sys.exit("Database connection failed!\n ->%s" % (exceptionValue))

Code();
