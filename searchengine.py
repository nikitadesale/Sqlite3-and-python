import pandas as pd
import sqlite3
import timeit

conn = sqlite3.connect("c://sqlite3//company.db")
cur = conn.cursor()
cur.execute("select * from table1 limit 5;")
results = cur.fetchall()
print(results)

df = pd.read_sql_query("SELECT * FROM table1", conn)
df
cur.execute("SELECT * FROM table1 WHERE name LIKE '%tcs%';")

#solution 1
start_time = timeit.default_timer()
df = pd.read_sql_query("SELECT name FROM table1 WHERE name LIKE '%tcs%' LIMIT 10", conn)
elapsed = timeit.default_timer() - start_time
print(df,elapsed)
#elapsed

#solution 2
t = ('%info%',)
start_time = timeit.default_timer()
cur.execute('SELECT name FROM table1 WHERE name LIKE ? LIMIT 10', t)
#print(cur.fetchone())
results = cur.fetchall()
elapsed = timeit.default_timer() - start_time
print(results,elapsed )

#solution 3
a=input("Which company you looking for:")
b='%'
c=b+a+b
data=(c,)
start_time = timeit.default_timer()
cur.execute('SELECT name FROM table1 WHERE name LIKE ? LIMIT 10', data)
results = cur.fetchall()
elapsed = timeit.default_timer() - start_time
print(results,elapsed )

#solution 4
a=input("Which company you looking for:")
b='%'+a+'%'
data=(b,)
start_time = timeit.default_timer()
cur.execute('SELECT name FROM table1 WHERE name LIKE ? LIMIT 10', data)
results = cur.fetchall()
elapsed = timeit.default_timer() - start_time
print(results,elapsed )

results

