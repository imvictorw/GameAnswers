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
    UPDATE ga_questions
    SET score = score + 1
    WHERE id_pk='""" + argId + """'""")

    cursor.execute("""
        SELECT ga_questions.id_pk, username_fk, game_fk, timestamp, title, body, score, answercount, avatar
        FROM ga_questions
        INNER JOIN ga_users ON ga_users.username = ga_questions.username_fk
        WHERE ga_questions.id_pk=%s""" % (argId))
    records = cursor.fetchall()
    conn.commit()
    colName = ['id_pk', 'username_fk', 'game_fk', 'timestamp', 'title', 'body', 'score', 'answercount', 'avatar']

    # TRANSLATE data to proper format/type
    out = [{}]
    for j in range(len(colName)):
        out[0][colName[j]] = records[0][j]

    jsonData = json.dumps(out)
    print jsonData
    
except:
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))