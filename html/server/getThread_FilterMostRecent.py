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

    # RETRIEVE gameID from php
    argFilter = dataJson.get('filter')[0]

    # RETRIEVE game name with corresponding id
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name
        FROM ga_games
        WHERE id_pk='""" + argFilter + "'")
    game = cursor.fetchall()
    game = game[0][0]

    # RETRIEVE newest 25 questions
    cursor2 = conn.cursor()
    cursor2.execute("""
        SELECT id_pk, username_fk, game_fk, timestamp, title, score, answercount
        FROM ga_questions
        WHERE game_fk='""" + game + """'
        ORDER BY timestamp DESC
        LIMIT 25""")
    records = cursor2.fetchall()
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
