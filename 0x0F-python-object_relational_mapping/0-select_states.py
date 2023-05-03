#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    
    # Create a cursor object to execute queries
    cur = db.cursor()
    
    # Execute the query to retrieve all the states and order by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all the rows and display them
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    # Close all database connections
    cur.close()
    db.close()
