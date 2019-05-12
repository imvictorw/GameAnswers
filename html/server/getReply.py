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
    
    # RETRIEVE threadID from php
    argId = dataJson.get('id_pk')[0]
    
    # RETRIEVE question with matching threadID
    cursor = conn.cursor()
    cursor.execute("""
        SELECT ga_replies.id_pk, questionid_fk, username_fk, body, timestamp, score, avatar
        FROM ga_replies
        INNER JOIN ga_users ON ga_users.username = ga_replies.username_fk
        WHERE questionid_fk=%s
        ORDER BY timestamp DESC""" % (argId))

    records = cursor.fetchall()

    colName = ['id_pk', 'questionid_fk', 'username_fk', 'body', 'timestamp', 'score', 'avatar']

    # TRANSLATE data to proper format/type
    out = []
    for row in range(len(records)):
        out.append({})
        for j in range(len(records[row])):
            out[row][colName[j]] = records[row][j]

    jsonData = json.dumps(out)
    print jsonData
    
except:
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))