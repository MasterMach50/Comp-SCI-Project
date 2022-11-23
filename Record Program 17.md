# 17. ILLUSTRATION OF CONNECTIVITY PROGRAMMING-I
Integrate SQL with Python by importing the MYSQL module and to implement
the DML command (SELECT).
Create a table STUDENT (Roll, Name, Stream, Section).
Populate the table with 4 records of your choice.
Display all the records of student table.

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

    cur.execute('select * from student')
    rows = cur.fetchall() #retrieving data from the result set
    
    print('Data from the student table is as follows:\n')

    for i in rows: #displaying the table
        print(i[0],'    ',i[1],'    ',i[2],'    ',i[3])

    cur.close()
    conn.close()

except Exception as e:
    print(e)
```

## OUTPUT
```
Connected
Data from the student table is as follows:

1      Alice      COMPUTER SCIENCE      A
2      Bob      COMMERCE      B
3      Charlie      HUMANITIES      C
4      David      COMPUTER SCIENCE      D
```
