import psycopg2
import sys
import cgi
import cgitb
import os
import json

cgitb.enable()
print 'Content-Type: text/plain\r\n\r'

def Code():
    try:
        conn = psycopg2.connect("dbname='info1003gp' user='info1003gp' host='postgres.it.usyd.edu.au' password='Wed23sYT'")
        urlString = "?" + os.environ['QUERY_STRING']
        from urlparse import urlparse, parse_qs
        qs = urlparse(urlString).query
        dataJson = parse_qs(qs)
        dictionary = dict(dataJson)

        # RETRIEVE new question data from form
        argUsername = dictionary.get('username')[0]
        argGame = dictionary.get('game')[0]
        argTitle = dictionary.get('title')[0]
        argBody = dictionary.get('body')[0]

        # CHECK for hacking question data
        if "<script>" in argTitle or "<script>" in argBody or "<script>" in argGame:
            print "hackattempt"
            return

        # GET current time
        import datetime
        argTime = datetime.datetime.now()

        # INSERT question data into question table
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO ga_questions(username_fk, game_fk, timestamp, title, body)
        VALUES (%s, %s, %s, %s, %s)""", (argUsername, argGame, argTime, argTitle, argBody))
        #conn.commit();

        t = """
        UPDATE ga_games
        SET questioncount = questioncount + 1
        WHERE name = '%s'
        """ % argGame

        #print t

        cursor.execute(t);

        #cursor.execute("""
        #UPDATE ga_games
        #SET questioncount = questioncount + 1
        #WHERE name = '%s'
        #""", argGame);

        conn.commit();

        print "success"
        
    except:
        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
        sys.exit("Database connection failed!\n ->%s" % (exceptionValue))

Code();