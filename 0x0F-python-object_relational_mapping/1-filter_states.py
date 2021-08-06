#!/usr/bin/python3
"""
Script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM `states` WHERE `states`.`name` \
        RLIKE '^[N]' ORDER BY `states`.`id` ASC")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
