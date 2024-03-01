import psycopg2

conn = psycopg2.connect(dbname="hw", user="marina", password="123")
cursor = conn.cursor()

# Create table:

# cursor.execute("""
#     CREATE TABLE orders (
#         ord_no SERIAL PRIMARY KEY,
#         purch_amt NUMERIC,
#         ord_date DATE,
#         customer_id INT,
#         salesman_id INT
#     );
# """)
# conn.commit()

# Insert data:

# insert_query = """
#     INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id)
#     VALUES (%s, %s, %s, %s, %s);
# """
#
# data = [
#     (70001, 150.5, '2012-10-05', 3005, 5002),
#     (70009, 270.65, '2012-09-10', 3001, 5005),
#     (70002, 65.26, '2012-10-05', 3002, 5001),
#     (70004, 110.5, '2012-08-17', 3009, 5003),
#     (70007, 948.5, '2012-09-10', 3005, 5002),
#     (70005, 2400.6, '2012-07-27', 3007, 5001),
#     (70008, 5760, '2012-09-10', 3002, 5001),
#     (70010, 1983.43, '2012-10-10', 3004, 5006),
#     (70003, 2480.4, '2012-10-10', 3009, 5003),
#     (70012, 250.45, '2012-06-27', 3008, 5002)
# ]
#
# cursor.executemany(insert_query, data)
# conn.commit()

# 1 query:
#
# select1_query = """
#     SELECT ord_no, ord_date, purch_amt
#     FROM orders
#     WHERE salesman_id = 5002;
# """
#
# cursor.execute(select1_query)
# results = cursor.fetchall()
#
# for row in results:
#     print(row)

#  2 query:

# select_distinct_query = """
#     SELECT DISTINCT salesman_id
#     FROM orders;
#     """
#
# cursor.execute(select_distinct_query)
# results = cursor.fetchall()
#
# for row in results:
#     print(row)

#  3 query:

# select_ordered_query = """
#     SELECT ord_date, salesman_id, ord_no, purch_amt
#     FROM orders
#     ORDER BY ord_date, salesman_id, ord_no, purch_amt;
# """
#
# cursor.execute(select_ordered_query)
# results = cursor.fetchall()
#
# for row in results:
#     print(row)

#  4 query:

select_between_query = """
    SELECT ord_no, ord_date, purch_amt
    FROM orders
    WHERE ord_no BETWEEN 70001 AND 70007;
"""

cursor.execute(select_between_query)
results = cursor.fetchall()

for row in results:
    print(row)


cursor.close()
conn.close()

#  comment to create PR