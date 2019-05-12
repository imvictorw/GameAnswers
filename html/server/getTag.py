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

    # RETRIEVE tagID from php
    argId = dataJson.get('id_pk')[0]
    
    # RETRIEVE tag with matching tagID
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id_pk, name, img_link
        FROM ga_games
        WHERE id_pk=%s""" % (argId))
    records = cursor.fetchall()

    colName = ['id_pk', 'name', 'img_link']

    # TRANSLATE data to proper format/type
    out = [{}]
    for j in range(len(colName)):
        out[0][colName[j]] = records[0][j];

    jsonData = json.dumps(out)
    print jsonData
    
except:
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
