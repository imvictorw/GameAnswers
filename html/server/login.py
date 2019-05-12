import psycopg2
import psycopg2.extras
import sys
import os
import cgi
import cgitb
import hashlib

cgitb.enable()
print 'Content-Type: text/plain\r\n\r'

try:
    conn = psycopg2.connect("dbname='info1003gp' user='info1003gp' host='postgres.it.usyd.edu.au' password='Wed23sYT'")
    urlString = "?" + os.environ['QUERY_STRING']
    from urlparse import urlparse, parse_qs
    qs = urlparse(urlString).query
    dataJson = parse_qs(qs)
    
    # RETRIEVING username and password from form
    argUser = dataJson.get('username')[0]
    argPass = hashlib.sha256(dataJson.get('passd')[0]).hexdigest()

    # RETRIEVING username and password from 
    cursor = conn.cursor()
    cursor.execute("""
        SELECT passwd FROM ga_users WHERE username = '""" + argUser + """'""")
    records = cursor.fetchall()

    # CHECKS if username and password match with database
    if len(records) == 1:
        if records[0][0] == argPass:
            print "success"
        else:
            print "invalid"
    else:
        print "invalid"
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
