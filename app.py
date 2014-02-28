#!flask/bin/python
from flask import Flask, render_template, request, url_for, redirect
import sqlite3 as lite
import sys

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
	#connect to db
	db_obj = connect_db()
	#assign cursor and connection to variables
	cur = db_obj[0]
	con = db_obj[1]
	
	#get list of all threads		
	cur.execute('SELECT * FROM thread;')
	threads = cur.fetchall()
	#get  posts belonging to each thread
	cur.execute('SELECT * FROM post;')
	posts = cur.fetchall()


	#cur = connect_db()
	if request.method == 'POST':
		
		#grab form data
		subject = request.form['subjectLine']
		comment = request.form['comment']
		
		#get highest thread post number
		cur.execute('SELECT MAX(id) FROM thread;')
		#current post is 1 higher
		postnum = cur.fetchone()[0] + 1
		item = [postnum, subject]
		#adds thread to the database by passing it the item
		cur.execute('insert into thread values(?,?)',item)

		#save the changes
		con.commit()
		con.close()
		
		return redirect(url_for('index'))

		#return render_template('listthreads.html', threads=threads, posts=posts)	

	con.close()
	
	return render_template('listthreads.html', threads=threads, posts=posts)	

#connect to database, return cursor and connection
def connect_db():
	con = None
	try:
		con = lite.connect('data.db')
		cur = con.cursor()
		return cur,con
	except lite.Error, e:
		print "Error %s:" %e.args[0]
		return

if __name__ == '__main__':
    app.run(debug = True)
