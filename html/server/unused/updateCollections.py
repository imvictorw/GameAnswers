import psycopg2
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
    #urlString = "?username=pikachu&collectionname=Trash&newname=More+Trash&descript=Soo+Many+Trash"
    from urlparse import urlparse, parse_qs
    qs = urlparse(urlString).query
    dataJson = parse_qs(qs)
    userName = dataJson.get('username')[0]
    coll = dataJson.get('collectionname')[0]
    #print dataJson

    cursor = conn.cursor()
    if 'newname' in dataJson:
        folName = dataJson.get('newname')[0]
        cursor.execute("UPDATE collection SET collectionName = '" + folName + "' WHERE collectionName = '" + coll + "' AND ownerId_fk = '" + userName + "'")
        coll = folName
        conn.commit()
    # Finding ID
    cursor.execute("SELECT collectionId_pk FROM collection WHERE collectionName = '" + coll + "' AND ownerId_fk = '" + userName + "'")
    idCol = cursor.fetchone()
    #print idCol

    #cursor.execute("DELETE FROM objects WHERE collectionname_fk = '" + coll + "' AND ownerId_fk = '" + userName + "'")
    #cursor.execute("DELETE FROM collectDescript WHERE collectionId_fk = " + str(records[i][0]))
    #cursor.execute("DELETE FROM collection WHERE collectionName = " + coll + " AND ownerId_fk = " + userName)

    # OTHER VALUES
    dictionary = dict(dataJson)
    for key in dictionary:
        if key != 'username':
            if key != 'collectionname':
                if key != 'newname':
                    if (len(dictionary[key])) == 1:
                        cursor.execute("UPDATE collectDescript SET val = '" + dictionary[key][0] + "' WHERE collectionid_fk = " + str(idCol[0]) + " AND field = '" + key + "'")
                    else:  
                        cursor.execute("UPDATE collectDescript SET val = '" + dictionary[key] + "' WHERE collectionid_fk = " + str(idCol[0]) + " AND field = '" + key + "'")
    conn.commit()
    print "success"
except:
    # Get the most recent exception
    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
    # Exit the script and print an error telling what happened.
    sys.exit("Database connection failed!\n ->%s" % (exceptionValue))
