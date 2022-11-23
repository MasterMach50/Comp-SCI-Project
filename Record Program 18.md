# 18. ILLUSTRATION OF CONNECTIVITY PROGRAMMING-II
Integrate SQL with python by importing the MYSQL module and to implement
the DML commands(INSERT and SELECT).
Populate the STUDENT(Roll, Name, Stream, Section) table
with 4 records of your choice using INSERT query and display
all the records by using the appropriate Query

## Source Code
```py
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
        [1] Insert new record
        [2] Display the table
        [3] Exit
        """)

        ch = input("Enter your choice[1/2/3]: ")

        if ch == "1":
            roll = input("Enter roll no of student: ")
            name = input("Enter name of student: ")
            stream = input("Enter stream of student: ")
            section = input("Enter section of student: ")

            cur.execute("insert into student values({}, '{}', '{}', '{}')".format(roll, name, stream, section))

            conn.commit()
            print("New record inserted into table")

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
```

## OUTPUT
```
Connected
=============================================
What would you like to do?

        [1] Insert new record
        [2] Display the table
        [3] Exit
        
Enter your choice[1/2/3]: 2
Data from the student table is as follows:

1      Alice      COMPUTER SCIENCE      A
2      Bob      COMMERCE      B
3      Charlie      HUMANITIES      C
4      David      COMPUTER SCIENCE      D
=============================================
What would you like to do?

        [1] Insert new record
        [2] Display the table
        [3] Exit

Enter your choice[1/2/3]: 1
Enter roll no of student: 5
Enter name of student: Ellie
Enter stream of student: COMMERCE 
Enter section of student: C
New record inserted into table
=============================================
What would you like to do?

        [1] Insert new record
        [2] Display the table
        [3] Exit

Enter your choice[1/2/3]: 2
Data from the student table is as follows:

1      Alice      COMPUTER SCIENCE      A
2      Bob      COMMERCE      B
3      Charlie      HUMANITIES      C
4      David      COMPUTER SCIENCE      D
5      Ellie      COMMERCE      C
=============================================
What would you like to do?

        [1] Insert new record
        [2] Display the table
        [3] Exit

Enter your choice[1/2/3]: 3
[ Exiting ]
```
