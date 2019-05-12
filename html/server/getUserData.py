import psycopg2
import psycopg2.extras
import sys
import os
import cgi
import cgitb
import hashlib
import json

cgitb.enable()
print 'Content-Type: text/plain\r\n\r'

try:
    conn = psycopg2.connect("dbname='info1003gp' user='info1003gp' host='postgres.it.usyd.edu.au' password='Wed23sYT'")
    urlString = "?" + os.environ['QUERY_STRING']
    from urlparse import urlparse, parse_qs
    qs = urlparse(urlString).query
    dataJson = parse_qs(qs)
    
    # RETRIEVING username from sessionStorage
    argUser = dataJson.get('username')[0]

    out = []
    out.append({})

    # RETRIEVING userData from server
    cursor = conn.cursor()

    cursor.execute("""
        SELECT avatar
        FROM ga_users
        WHERE username = '""" + argUser + """'""")
    records = cursor.fetchall()
    out[0]['avatar'] = records[0][0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM ga_questions
        WHERE username_fk='%s'""" % (argUser));
    records = cursor.fetchall()
    out[0]['questionCount'] = records[0][0]

    #print records;

    cursor.execute("""
        SELECT COUNT(*)
        FROM ga_replies
        WHERE username_fk='%s'""" % (argUser));
    records = cursor.fetchall()
    out[0]['answerCount'] = records[0][0]

    # CONVERT userData to proper format
    # TODO Decide what userData to give back

    #print records;

    #records = cursor.fetchall()
    #out[0]['answerCount'] = records[0][2]

    jsonData = json.dumps(out)
    print jsonData

except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
