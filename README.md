# Sorting-hat: a seat assigning randomly considering social distance

Please refer some websites about sqlite and python.
Start from here [https://www.sqlitetutorial.net/sqlite-sample-database/]

## Environment
- python 3.6 (recommended)
- sqlite3 (default included python)
- linux ubuntu 18.04 (please update your test log)


## dbsetup.py
**Important!** First and foremost, change `DB` variable to the database name. <br/>
- ex) DB = 'seat_2020_1.db'
Create "users", "cluster", and "seat" table (used only once for creating table)<br/>
Three tables are created by simply executing the code.<br/>

"users" table <br/>
- pid (VARCHAR): student ID<br/>
- full_name (VARCHAR): student name<br/>

"cluster" table <br/>
- cid (INT): cluster ID<br/>
- number_of_seat (INT): number of seats in cluster (3 or 6)<br/>
- number_owned (INT): number of occupied seats in cluster<br/>

"seat" table<br/>
- sid (INT): seat id<br/>
- owner_id (VARCHAR): corresponds to users.pid<br/>
- cluster_id (INT): corresponds to cluster.cid<br/>


### register.py
**Important!** First and foremost, change `DB` variable to the database name. <br/>
- ex) DB = 'seat_2020_1.db'
Insert rows into tables. Can insert from <b>csv files(1)</b> or insert by <b>manual input(2)</b>.<br/>
csv files: "usertable.csv", "clustertable.csv", or "seattable.csv" <br/>

Ex1) How to insert rows in "usertable.csv" to "users" table<br/>
- execute code<br/>
- csv(1) or command(2)? -> 1<br/>
- enter the file path? -> usertable.csv<br/>
- what table? user(1), cluster(2), seat(3) -> 1<br/>

Ex2) How to insert rows in "clustertable.csv" to "cluster" table<br/>
- execute code<br/>
- csv(1) or command(2)? -> 1<br/>
- enter the file path? -> clustertable.csv<br/>
- what table? user(1), cluster(2), seat(3) -> 2<br/>

Ex3) How to insert rows in "seattable.csv" to "seat" table<br/>
- execute code<br/>
- csv(1) or command(2)? -> 1<br/>
- enter the file path? -> seattable.csv<br/>
- what table? user(1), cluster(2), seat(3) -> 3<br/>

Ex4) How to insert new student manually<br/>
- execute code<br/>
- csv(1) or command(2)? -> 2<br/>
- what table? user(1), cluster(2), seat(3) -> 1<br/>
- please type user pid -> (ex) 2020-20001 <br/>
- please type user full name -> (ex) DurianFarmer <br/>


### assign_seat.py
**Important!** First and foremost, change `DB` variable to the database name. <br/>
- ex) DB = 'seat_2020_1.db'
Randomly assign seats in a bulk(1) or assign a seat for one student(2) <br/>
to consider both i) social distance and ii) interaction between students from different labs, <br/>
- (A) for each cluster, randomly assign one seat to one student <br/>
- (B) if every cluster is visited, repeat (A)
- through (A) and (B) students are almost equally distributed <br/>

Ex 1) How to assign seats to many students at once<br/>
- execute code<br/>
- what do you want to do? bulk insert(1), individual insert(2) -> 1 <br/>

Ex 2) How to assign seats to specific student<br/>
- execute code<br/>
- what do you want to do? bulk insert(1), individual insert(2) -> 2 <br/>
- the program shows a list of students that do not have a seat<br/>
- please type pid -> (ex) 2020-20001<br/>
- the program assigns a random seat to (ex) 2020-20001<br/>
 
### search.py
**Important!** First and foremost, change `DB` variable to the database name. <br/>
- ex) DB = 'seat_2020_1.db'
Search the list every student(1), or every seat(2), or students and their seats(3) <br/>

Ex 1) How to search every student<br/>
- execute code<br/>
- what do you want to see? -> 1 <br/>

Ex 2) How to search every seat<br/>
- execute code<br/>
- what do you want to see? -> 2 <br/>

Ex 3) How to search the seats that are assigned to students<br/>
- execute code<br/>
- what do you want to see? -> 3 <br/>


### update_info.py
**Important!** First and foremost, change `DB` variable to the database name. <br/>
- ex) DB = 'seat_2020_1.db'
Removes specific student from seat(1), or <br/>
assign specific seat to student(2), or <br/>
remove_every_student_from_seat(3) <br/>

Ex 1) How to remove specific student from seat (for example, leave of absence) <br/>
- execute code<br/>
- what do you want to update? -> 1 <br/>
- the program shows a list of students that have a seat<br/>
- please type pid -> (ex) 2020-20001<br/>
- the program detaches students from seat<br/>

Ex 2) How to assign specific seat to student<br/>
- execute code<br/>
- what do you want to update? -> 2 <br/>
- the program shows a list of all students<br/>
- please type pid -> (ex) 2020-20001<br/>
- the program shows a list of empty seats<br/>
- please type new sid for student(pid) -> (ex) 1<br/>
- update complete<br/>

Ex 3) How to remove every student from seat <br/>
- execute code<br/>
- what do you want to update? -> 3 <br/>
- the program removes every student from seat <br/>


