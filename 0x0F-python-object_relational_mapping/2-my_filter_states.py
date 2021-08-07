#!/usr/bin/python3
"""
Script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM `states` WHERE `states`.`name` = '{:s}' \
        ORDER BY `states`.`id` ASC".format(argv[4]))
    results = cursor.fetchall()
    for row in results:
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db.close()
