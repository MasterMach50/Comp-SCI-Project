# 20. ILLUSTRATION OF CONNECTIVITY PROGRAMMING-IV
# Integrate SQL with python by importing the MYSQL module and to implement the DML commands(DELETE and SELECT).
# Populate the STUDENT(Roll, Name, Stream, Section)table with 4 records of your choice and do the following tasks:
#     - Accept the roll no: of the student to be deleted.
#     - Delete the Record
#     - Display all the records (After deletion)

import mysql.connector as msc

try: # Using a try block to catch errors
    conn = msc.connect(host='localhost',user='root',password='password',database='recordwork1')

    if (conn.is_connected()): #checking if the connection is established
        print('Connected')
    else:
        print('Connection not established')

    cur = conn.cursor()

    while True:
        print("=============================================")
        print("What would you like to do?")
        print("""
        [1] Delete a record
        [2] Display the table
        [3] Exit
        """)

        ch = input("Enter your choice[1/2/3]: ")

        if ch == "1":
            roll = input("Enter roll no of student to delete: ")

            cur.execute("delete from student where roll={}".format(roll))

            conn.commit()
            print("Record has been deleted")

        elif ch == "2":
            cur.execute('select * from student')
            rows = cur.fetchall() #retrieving data from the result set
    
            print('Data from the student table is as follows:\n')

            for i in rows: #displaying the table
                print(i[0],'    ',i[1],'    ',i[2],'    ',i[3])

        elif ch == "3":
            print("[ Exiting ]") # Break from the loop to exit
            break

        else:
            print("[ Invalid Choice ]") # In case user inputs a choice that was not defined

    cur.close()
    conn.close()

except Exception as e:
    print(e)