import  sqlite3

# sql datatypes:
# BULL
# INTEGER
# REAL
# TEXT
# BLOB

# conn = sqlite3.connect(":memory:")
conn = sqlite3.connect("customer.db")

curr = conn.cursor()



#create table
# curr.execute("""
#     CREATE TABLE IF NOT EXISTS products(
#         name text,
#         price real
#     )
# """)



# Insert
# curr.execute("INSERT INTO products VALUES ('coca cola', 1.2)")

# products=[
#     ('pepsi', 1),
#     ('fanta', 1.3),
# ]
# curr.executemany("INSERT INTO products VALUES (?,?)", products)



# bazadan olish
#curr.fetchone()
#curr.fetchmany(3)
#curr.fatchall()

#rowid - id larni korsatadi
curr.execute("SELECT rowid, * FROM products")
print(curr.fetchall())
# print(curr.fetchone())
# print(curr.fetchone()[0])




# WHERE
# curr.execute("SELECT * FROM products WHERE rowid=2")
# print(curr.fetchone())



# UPDATE
# curr.execute(
#     "UPDATE products SET price=1.1 WHERE rowid=2"
# )



# DELETE
# curr.execute("DELETE FROM products WHERE price>=1.3")



# ORDER BY
curr.execute("SELECT * FROM products ORDER BY price")
print(curr.fetchall())






conn.commit()
conn.close()