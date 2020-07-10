# Sorting-hat: a seat assigning randomly considering social distance

there are 4 interfaces to deal with seat-assignment information.   
Please refer some websites about sqlite and python.
Start from here [https://www.sqlitetutorial.net/sqlite-sample-database/]

## Environment
- python 3.6 (recommended)
- sqlite3 (default included python)
- linux ubuntu 18.04 (please update your test log)

## dbsetup.py
Create "users", "cluster", and "seat" table (used only once)

### register.py
Insert rows into tables through csv files(1) or manual input(2)
To insert from csv, use "usertable.csv", "clustertable.csv", or "seattable.csv"
Ex. to insert "usertable.csv" to "users" table
csv(1) or command(2)? -> 1
enter the file path? -> usertable.csv
what table? user(1), cluster(2), seat(3) -> 1

### assign_seat.py
Randomly assign seats in a bulk(1) or one-by-one(2)
the algorithm
 i) evenly places students in each cluster, and thus,
ii) considers social distance between each student

### search.py
Give the list all of the students(1), or all of the seats(2), or students and their seats(3)

### update_info.py
Removes specific student from seat(1), or
assign specific seat to student(2), or
remove student permanently(3)


