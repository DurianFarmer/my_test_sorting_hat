# search.py
# search registered information from DB tables
import sqlite3
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
    query = input()
    if query =='1':
        for row in c.execute('''SELECT * FROM users'''):
            print(row)
        flag = ask_to_end()
    elif query =='2':
        for row in c.execute('''SELECT * FROM seat'''):
            print(row)
        flag = ask_to_end()
    elif query =='3':
        for row in c.execute('''SELECT * FROM users LEFT JOIN seat ON users.pid = seat.owner_id'''):
            print(row)
        flag = ask_to_end()            
    else:
        print('error', ' ', 'please type 1 or 2 or 3' )
        flag = True 


