#!flask/bin/python
from flask import Flask, render_template, request, url_for, redirect
from time import strftime
import micawber
from micawber.providers import bootstrap_basic
from micawber.contrib.mcflask import add_oembed_filters
import sqlite3 as lite
import sys

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
	#import shit
	providers = micawber.bootstrap_basic()
	add_oembed_filters(app, providers)
	#connect to db
	db_obj = connect_db('data.db')
	#assign cursor and connection to variables
	cur = db_obj[0]
	con = db_obj[1]
	
	#get list of all threads		
	cur.execute('SELECT * FROM thread;')
	threads = cur.fetchall()
	#get original post belonging to each thread
	cur.execute('SELECT * FROM post WHERE id = 1 ;')
	posts = cur.fetchall()

	if request.method == 'POST':
		
		#grab form data
		subject = request.form['subjectLine']
		comment = request.form['comment']
		embed = request.form['embed']

		if subject == "" or comment == "" or embed =="":
			return "need javascript"
		
		#get highest threadID
		cur.execute('SELECT MAX(id) FROM thread;')
		#current post is 1 higher
		threadID = cur.fetchone()[0] + 1
		thread = [threadID, subject]
		#adds thread to the database by passing it the item
		cur.execute('insert into thread values(?,?)',thread)

		#create original post
		post = [1, threadID, strftime("%I:%M %B %d, %Y"), comment, embed] 
		cur.execute('insert into post values(?,?,?,?,?)',post)

		#save the changes
		con.commit()
		con.close()
		
		return redirect(url_for('index'))

	con.close()
	
	return render_template('listthreads.html', threads=reversed(threads), posts=posts) 

@app.route('/thread/<threadID>',methods = ['GET', 'POST'])
def viewThread(threadID):
	#import shit
	providers = micawber.bootstrap_basic()
	add_oembed_filters(app, providers)
	#database shit
	db_obj = connect_db('data.db')
	cur = db_obj[0]
	con = db_obj[1]	

	#get information about this thread
	cur.execute('SELECT * FROM thread WHERE id ='+threadID+';')
	threadInfo = cur.fetchall()

	title = threadInfo[0][1]

	#get original post belonging to each thread
	cur.execute('SELECT * FROM post WHERE threadID ='+threadID+';')
	posts = cur.fetchall()

	return render_template('viewthread.html',title=title, posts=posts) 

#connect to database, return cursor and connection
def connect_db(db):
	con = None
	try:
		con = lite.connect(db)
		cur = con.cursor()
		return cur,con
	except lite.Error, e:
		print "Error %s:" %e.args[0]
		return

if __name__ == '__main__':
    app.run(debug = True)
