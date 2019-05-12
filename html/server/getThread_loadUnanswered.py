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

    # RETRIEVE newest 25 questions
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id_pk, username_fk, game_fk, timestamp, title, score, answercount
        FROM ga_questions
        WHERE answercount = '0'
        LIMIT 25""")
    records = cursor.fetchall()
    colName = ['id_pk', 'username_fk', 'game_fk', 'timestamp', 'title', 'score', 'answercount']

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
