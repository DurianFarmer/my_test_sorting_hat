# update_info.py
# update registered data on the DB table
import sqlite3
DB = 'seat_2021_1.db'

conn = sqlite3.connect(DB)
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

def remove_student_from_seat():
    # A. 학생의 지정된 자리를 삭제하기
    # 1. 좌석이 지정된 학생들의 pid를 획득
    # 2. 획득된 pid 중에서 하나를 선택하도록 입력 대기
    # 3. 선택된 pid의 학생의 자리를 제거 (cluster: owned -= 1, seat: owner_id 제거)

    pid_list = []
    for row in c.execute('''SELECT users.pid FROM users LEFT JOIN seat ON users.pid = seat.owner_id WHERE \
                     seat.owner_id is not null'''):
        pid_list.append(*row)
    print('students that have a seat:', pid_list)

    if pid_list:
        print('please type pid')
        mm = input()
        if mm == 'q':
            print('goodbye')
            flag = False            
            return flag
        elif mm not in pid_list:
            print('select a pid in the list!!')
            flag = True
            return flag
        
        for row in c.execute('''SELECT cluster_id FROM seat WHERE owner_id=?''', (str(mm),) ):
            cluster_id = row[0]
        c.execute('''UPDATE seat SET owner_id=NULL WHERE owner_id=?''', (str(mm),) )
        c.execute('''UPDATE cluster SET number_owned=number_owned-1 WHERE cid=?''', (cluster_id,) )    
        conn.commit()
        print('removing student from seat done')

        pid_list.remove(mm)
        if not pid_list:
            print('No student has a seat. Goodbye.')
            flag = False
            return flag    
                
        return ask_to_end()
    else:
        print('No student has a seat. Goodbye.')
        flag = False
        return flag

def assign_specific_seat_to_student():
    # B. 학생의 지정된 자리를 강제로 변경하거나, 자리가 미배정된 학생의 자리를 강제로 설정하기
    # 1. 전체 pid를 획득
    # 2. 획득된 pid 중에서 하나를 선택하도록 입력 대기
    # 3. 자리가 지정된 pid인 경우, A.를 실행
    # 4. 선택된 pid의 학생의 자리를 강제 배정 (cluster: owned += 1, seat: owner_id 추가)
    pid_list = []
    for row in c.execute('''SELECT users.pid FROM users'''):
        pid_list.append(*row)
    print('all students:', pid_list)
    
    if pid_list:
        print('please type pid')
        mm = input()
        if mm == 'q':
            print('goodbye')
            flag = False            
            return flag
        elif mm not in pid_list:
            print('select a pid in the list!!')
            flag = True
            return flag

        cluster_id = -1
        # 학생에게 자리가 배정되어 있었는지를 확인
        for row in c.execute('''SELECT cluster_id FROM seat WHERE owner_id=?''', (str(mm),) ):            
            cluster_id = row[0]            
        
        # 학생의 자리가 배정되어 있었던 경우, 학생의 자리를 없앤다.
        if cluster_id != -1:
            c.execute('''UPDATE seat SET owner_id=NULL WHERE owner_id=?''', (str(mm),) )
            c.execute('''UPDATE cluster SET number_owned=number_owned-1 WHERE cid=?''', (cluster_id,) )
            conn.commit()
        
        # 학생에게 새로운 자리를 배치
        sid_list = []
        for row in c.execute('''SELECT seat.sid FROM seat WHERE seat.owner_id IS NULL'''):
            sid_list.append(*row)
        print('empty seats:', sid_list)

        if sid_list:
            print('please type new sid for student(pid):', mm)
            tmp = input()

            if tmp == 'q':
                print('goodbye')
                flag = False
                return flag
            try:
                sid = int(tmp)
                if sid not in sid_list:
                    print('select an sid in the list!!')
                    flag = True
                    return flag
                else:
                    c.execute('''UPDATE seat SET owner_id =? WHERE sid=?''', (str(mm), sid))
                    conn.commit()
                    print('update done')
                    return ask_to_end()
                         
            except ValueError as e:            
                print('### ERROR!! ###')
                print(e)
                print('sid must be an INTEGER\n')
                flag = True
                return flag
                
        else:
            print('No left seat. Goodbye.')
            flag = False
            return flag

        
        conn.commit()

        pid_list.remove(mm)
        if not pid_list:
            print('No student. Goodbye.')
            flag = False
            return flag    
        
        return ask_to_end()
    else:
        print('No student. Goodbye.')
        flag = False
        return flag    

def remove_every_student_from_seat():
    # C. 모든 학생의 자리를 지움 (테스트할 때 편리하기 위한 용도의 함수)        
    pid_list = []
    for row in c.execute('''SELECT users.pid FROM users LEFT JOIN seat ON users.pid = seat.owner_id WHERE \
                     seat.owner_id is not null'''):
        pid_list.append(*row)    
    
    if pid_list:
        for mm in pid_list:                                    
            for row in c.execute('''SELECT cluster_id FROM seat WHERE owner_id=?''', (str(mm),) ):
                cluster_id = row[0]
            c.execute('''UPDATE seat SET owner_id=NULL WHERE owner_id=?''', (str(mm),) )
            c.execute('''UPDATE cluster SET number_owned=number_owned-1 WHERE cid=?''', (cluster_id,) )    
            conn.commit()
            
        print('Removing every student from seat done. Goodbye')
        return False
    else:
        print('No student has a seat. Goodbye.')
        flag = False
        return flag

while flag:
    print('what do you want to update? remove student from seat(1), assign specific seat to student(2), remove every student from seat(3)')
    print("(cf. type 'q' to exit!!)")
    mode = input()
    if mode == '1':
        flag = remove_student_from_seat()
    elif mode == '2':
        flag = assign_specific_seat_to_student()
    elif mode == '3':
        flag = remove_every_student_from_seat()
    elif mode == 'q':
        print('goodbye')
        flag = False
        break
    else:
        print('error', ' ', 'please type 1 or 2 or 3' )
        flag = True
