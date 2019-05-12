import psycopg2
import psycopg2.extras
import sys
import cgi
import cgitb
import os
import json
import collections

cgitb.enable()
print 'Content-Type: text/plain\r\n\r'

try:
    conn = psycopg2.connect("dbname='info1003gp' user='info1003gp' host='postgres.it.usyd.edu.au' password='Wed23sYT'")
    urlString = "?" + os.environ['QUERY_STRING']
    from urlparse import urlparse, parse_qs
    qs = urlparse(urlString).query
    dataJson = parse_qs(qs)

    argQuestionID = dataJson.get('questionid')[0]
    argUser = dataJson.get('username')[0]
    argBody = dataJson.get('body')[0]

    # CHECK for hacking question data
    if "<script>" in argBody:
        print "hackattempt"

    # GET current time
    import datetime
    argTime = datetime.datetime.now()
    
    # connect to pgDatabase
    cursor = conn.cursor()

    # execute Query
    cursor.execute("""
    INSERT INTO ga_replies(questionid_fk, username_fk, body, timestamp)
    VALUES(%s, %s, %s, %s)
    """, (argQuestionID, argUser, argBody, argTime))

    cursor.execute("""
    UPDATE ga_questions
    SET answercount = answercount + 1
    WHERE id_pk='""" + argQuestionID + """'
    """)

    conn.commit();
    print "success"
    
except:
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
