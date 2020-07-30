# search.py
# search registered information from DB tables
import sqlite3
import time

conn = sqlite3.connect('test.db')
c= conn.cursor()
flag = True

def ask_to_end():
    print('Do you want to quit? (y/n)')
    answer = input()
    if answer =='y':
        print('goodbye')
        conn.commit()
        conn.close()
        flag = False
    else:
        flag = True
    return flag
                
while flag:
    print('what do you want to see? all student table(1), all seat table(2), student with seat(3)')
    print("(cf. type 'q' to exit!!)")
    query = input()
    if query =='1':
        for row in c.execute('''SELECT * FROM users'''):
            print(row[0][0:7] + '***', row[1])
        flag = ask_to_end()
    elif query =='2':
        print('SEAT | STUDENT | CLUSTER')
        for row in c.execute('''SELECT * FROM seat'''):
            print(row[0], row[1] if row[1] is None else row[1][0:7] + '***', row[2])
        flag = ask_to_end()
    elif query =='3':
        for row in c.execute('''SELECT users.pid, users.full_name, seat.sid FROM users LEFT JOIN seat ON users.pid = seat.owner_id'''):
            if row[2] is not None:
                print(row[0][0:7] + '***', row[1], '|', row[2])
                # time.sleep(1)
        flag = ask_to_end()            
    elif query == 'q':
        print('goodbye')
        flag = False
    else:
        print('error', ' ', 'please type 1 or 2 or 3' )
        flag = True 


