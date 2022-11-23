import mysql.connector as msc

conn = msc.connect(host='localhost',user='root',password='password',database='recordwork1')

cur = conn.cursor()

cur.execute("truncate student")

cur.execute('insert into student values(1, "Alice", "COMPUTER SCIENCE", "A")')
cur.execute('insert into student values(2, "Bob", "COMMERCE", "B")')
cur.execute('insert into student values(3, "Charlie", "HUMANITIES", "C")')
cur.execute('insert into student values(4, "David", "COMPUTER SCIENCE", "D")')

conn.commit()
conn.close()