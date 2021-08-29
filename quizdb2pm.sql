create table user_profile (uid int PRIMARY KEY AUTO_INCREMENT, username 
varchar(50) UNIQUE, password varchar(50), name varchar(50), role varchar(50));


create table technology(tid int PRIMARY KEY AUTO_INCREMENT, tname varchar(70) UNIQUE);


create table questions(qid int PRIMARY KEY AUTO_INCREMENT, question varchar(200) UNIQUE,
opta varchar(100), optb varchar(100),optc varchar(100),optd varchar(100),
correct varchar(10), tech_id int, FOREIGN KEY(tech_id) REFERENCES technology(tid));


create table results (rid int primary key AUTO_INCREMENT, user_id int, tech_id int, 
marks float, resdate date, FOREIGN KEY(user_id) REFERENCES user_profile(uid), 
FOREIGN KEY(tech_id) REFERENCES technology(tid));


insert into user_profile(username, password,name,role) values ('admin123','1234',
'Rakesh Sharma', 'admin');2pmquizappquestionsquestions