import psycopg2
import psycopg2.extras
import sys
import cgi
import cgitb
import os
import json

cgitb.enable()
#print "Content-type:text/html\r\n\r\n"
print 'Content-Type: text/plain\r\n\r'

try:
    conn = psycopg2.connect("dbname='info1003_project' user='info1003user' host='postgres.it.usyd.edu.au' password='userpj1003'")
    # Parsing input data
    urlString = "?" + os.environ['QUERY_STRING']
    #urlString = "http://www.ug.it.usyd.edu.au/~lcha1115/testserver/register.cgi?username=snowwhite&passd=yoshi&age=7"
    from urlparse import urlparse, parse_qs
    qs = urlparse(urlString).query
    dataJson = parse_qs(qs)
    userName = dataJson.get('username')[0]
    userName = "'" + userName + "'"
    cursor = conn.cursor()
            
    # execute Query
    cursor.execute("SELECT field, val FROM profile WHERE username_fk = " + userName)
    # retrieve the records from the database
    records = cursor.fetchall()

    #datalist = []
    #for i in len(records):
    #    datalist.append([])
    #    for j in xrange(2):
    #        data[i].append(i+j)
    #    rowarray_list.append(row)

    colName = ['field', 'val']
    
    out = []
    for row in range(len(records)):
        out.append({})
        for j in range(len(records[row])):
            out[row][colName[j]] = records[row][j]
    jsonData = json.dumps(out)
    print jsonData

    # SAMPLE DATA
    # [[1, "firstName", "Pikachu"], [2, "lastName", "Ketchum"],
    # [3, "profilePhoto", "http://www.ug.it.usyd.edu.au/~info1003/project/default.png"],
    # [4, "email", "pikachu@pokemon.com"], [5, "aboutMe", "Cute little yellow monster"]]
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
