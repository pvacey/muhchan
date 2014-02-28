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
	id		integer	CONSTRAINT p_id_pk ,
	threadID		CONSTRAINT p_threadID_fk REFERENCES thread(id)
					ON DELETE CASCADE,
	content	varchar(160) CONSTRAINT p_content_nn NOT NULL,
	PRIMARY KEY(id,threadID)
);


--insert some stuff
insert into thread(id,title)
	values (1,'This was here first');

insert into post(id,threadID,content)
	values (1,1,'original post goes here');
insert into post(id,threadID,content)
	values (2,1,'this should not be visible');
