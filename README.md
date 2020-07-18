# Sorting-hat: a seat assigning randomly considering social distance

there are 4 interfaces to deal with seat-assignment information.   
Please refer some websites about sqlite and python.
Start from here [https://www.sqlitetutorial.net/sqlite-sample-database/]

## Environment
- python 3.6 (recommended)
- sqlite3 (default included python)
- linux ubuntu 18.04 (please update your test log)


## dbsetup.py
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
Randomly assign seats in a bulk(1) or assign a seat for one student(2) <br/>
to consider both i) social distance and ii) interaction between students from different labs, <br/>
- the algorithm randomly places students in clusters <br/>
- each cluster gets almost same number of students <br/>
- as much as possible, students are not assigned adjacent seats that do not have a partition between them <br/>

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
Search the list all of the students(1), or all of the seats(2), or students and their seats(3) <br/>

Ex 1) How to search all of the students<br/>
- execute code<br/>
- what do you want to see? -> 1 <br/>

Ex 2) How to search all of the seats<br/>
- execute code<br/>
- what do you want to see? -> 2 <br/>

Ex 3) How to search the seats that are assigned to students<br/>
- execute code<br/>
- what do you want to see? -> 3 <br/>


### update_info.py
Removes specific student from seat(1), or <br/>
assign specific seat to student(2), or <br/>
remove student permanently(3) <br/>

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

Ex 3) How to remove specific student permanently (for example, graduation) <br/>
- execute code<br/>
- what do you want to update? -> 3 <br/>
- the program shows a list of all students<br/>
- please type pid -> (ex) 2020-20001<br/>
- the program removes student permanently<br/>


