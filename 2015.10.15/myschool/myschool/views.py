from django.shortcuts import render_to_response

import MySQLdb

def users(request):
    content = MySQLdb.connect(
        host = 'localhost',
        user = 'root',
        passwd = '123456',
        db = 'db_name'
    )
    cur = content.cursor()
    cur.execute('select * from user;')
    con = cur.fetchall()
    cur.close()
    content.commit()
    content.close()
    return render_to_response('mydbs.html',locals())