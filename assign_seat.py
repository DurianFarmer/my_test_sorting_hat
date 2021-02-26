# assign_seat.py
# (A) for each cluster, randomly assign one seat to one student
# (B) if every cluster is visited, repeat (A)
import sqlite3
import csv
import random
DB = 'seat_2021_1.db'

conn = sqlite3.connect(DB)
c = conn.cursor()

# for bulk assign(1)
user_list = []
for row in c.execute('SELECT users.pid, users.full_name, seat.owner_id FROM users LEFT JOIN seat ON users.pid = seat.owner_id WHERE \
                     seat.owner_id is null'):
    user_list.append(row)
# shuffle user_list
random.shuffle(user_list)
print('Randomly shuffled students!!')

# for individual assign(2)
pid_list = []
for row in c.execute('SELECT users.pid FROM users LEFT JOIN seat ON users.pid = seat.owner_id WHERE \
                     seat.owner_id is null'):
    pid_list.append(*row)

# for both
cluster_pool = []
for row in c.execute('SELECT distinct cid FROM cluster WHERE number_of_seat-number_owned >0'):    
    cluster_pool.append(*row)

print('what do you want to do? bulk assign(1), individual assign(2)')
print("(cf. type 'q' to exit!!)")
users_reaction = input()

if users_reaction =='1':    
    cluster_pool_length = len(cluster_pool)
    period = 0

    while user_list:
        a= user_list.pop() #a[0] user pid, a[1] user name
        b= cluster_pool[period]
        period = (period + 1) % cluster_pool_length # for each cluster, assign one seat to one student, repeat this if all clusters are visited
        
        #a[0],b 활용해서 seat update
        seat_pool = []
        for row in c.execute('''SELECT * from seat where cluster_id = ? and owner_id is null''', (b,) ):
            # print('left seats:', row)
            seat_pool.append(row[0])        

        # choose a seat if a seat is left in the cluster
        # else, put back the student in user_list, and continue
        if seat_pool:
            selected_seat = random.choice(seat_pool)
        else:
            user_list.append(a)
            continue            

        c.execute('''UPDATE seat SET owner_id =? WHERE sid=?''', (str(a[0]),selected_seat) )
        # print(f'assign {a[1]} to seat {selected_seat}')

        c.execute('''UPDATE cluster SET number_owned =number_owned +1 WHERE cid =?''', (b,) )
        
    print('done')
    conn.commit()
    conn.close()
    
elif users_reaction=='2':
    cluster_pool = []
    for row in c.execute('SELECT distinct cid from cluster where number_of_seat-number_owned >0'):
        cluster_pool.append(*row)

    while True:
        print('students that do not have a seat:', pid_list)
        
        if pid_list:            
            print('please type pid')
            mm = input()
            if mm == 'q':
                print('goodbye')
                break            
            elif mm not in pid_list:
                print('select a pid in the list!!')
                continue
                        
            b= random.choice(cluster_pool)
            cluster_pool.remove(b)
            seat_pool = []
            for row in c.execute('''SELECT * from seat WHERE cluster_id = ? AND owner_id IS NULL''', (b,) ):
                seat_pool.append(row[0])
            occupied_seat =[]
            for row in c.execute('''SELECT * from seat WHERE cluster_id = ? AND owner_id is not NULL''',(b,)):
                occupied_seat.append(row[0])
            sd_pool =[]
            for xx in occupied_seat:
                for row in c.execute('''SELECT * from seat WHERE cluster_id = ? AND near = ?''',(b,xx)):
                    sd_pool.append(row[0])
            mmm_test = set(seat_pool) - set(sd_pool)
            mmm_test = list(mmm_test)
            if len(occupied_seat) <=4:
                selected_seat = random.choice(mmm_test)
            else:
                selected_seat = random.choice(seat_pool)

            c.execute('''UPDATE seat SET owner_id =? WHERE sid=?''', (str(mm), selected_seat))
            print(f'assign {mm} to seat {selected_seat}')
            c.execute('''UPDATE cluster SET number_owned =number_owned +1 WHERE cid =?''', (b,) )
            conn.commit()
            if not cluster_pool:
                cluster_pool = []
                for row in c.execute('SELECT distinct cid from cluster where number_of_seat-number_owned >0'):
                    cluster_pool.append(*row)

            pid_list.remove(mm)
            if not pid_list:
                print('Every student has a seat. Goodbye.')
                break    

            print('assign done, do you want to quit? (y/n)')
            mmm = input()
            if mmm == 'y':
                print('goodbye')
                break
        else:
            print('Every student has a seat. Goodbye.')
            break
    conn.close()

elif users_reaction == 'q':
    print('goodbye')
