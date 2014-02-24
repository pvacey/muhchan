--!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
--tables for a basic message board
--!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
DROP TABLE thread;
CREATE TABLE thread
(
	id integer CONSTRAINT t_id_pk PRIMARY KEY,
	title varchar(50) CONSTRAINT t_title_nn NOT NULL
);

DROP TABLE post;
CREATE TABLE post
(
	id		integer	CONSTRAINT p_id_pk PRIMARY KEY,
	threadID		CONSTRAINT p_threadID_fk REFERENCES thread(id)
					ON DELETE CASCADE,
	content	varchar(160) CONSTRAINT p_content_nn NOT NULL
);


--insert some stuff
insert into thread(id,title)
	values (1,'first title');
insert into thread(id,title)
	values (2,'so i heard u liek dogs');
insert into thread(id,title)
	values (3,'cats are ghey tho');

insert into post(id,threadID,content)
	values (11231,1,'test the post?');
insert into post(id,threadID,content)
	values (11221,1,'different words');
insert into post(id,threadID,content)
	values (31431,2,'this should be different tew');	
insert into post(id,threadID,content)
	values (11434,3,'oh wow such posts');
insert into post(id,threadID,content)
	values (31421,2,'so many kinds of posts available here');
insert into thread (id, title)
	values (4, 'kayt is sooo pretyy');
