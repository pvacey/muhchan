#!flask/bin/python
from flask import Flask, render_template, request
import sqlite3 as lite
import sys

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
	if request.method == 'POST':
		#subject = str(request.form['sujectLine'])
		#item = [123,'test']
		#cur.execute('insert into thread values(?,?)',item)
		return 'bewbs'

	
	cur = connect_db()

	#list of all threads		
	cur.execute('SELECT * FROM thread;')
	threads = cur.fetchall()
	#list posts
	cur.execute('SELECT * FROM post;')
	posts = cur.fetchall()

	return render_template('listthreads.html', threads=threads, posts=posts)	
	

def connect_db():
	con = None
	try:
		con = lite.connect('data.db')
		cur = con.cursor()
		return cur
	except lite.Error, e:
		print "Error %s:" %e.args[0]
		return

if __name__ == '__main__':
    app.run(debug = False)
