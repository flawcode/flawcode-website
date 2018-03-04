"""
This will show the registered users.

Usage:
    move to the correct directory and then run the below command.

    python showdb.py

"""
import sqlite3

from settings import DB_FILENAME

conn = sqlite3.connect(DB_FILENAME+'.db')

cursor = conn.execute('SELECT * FROM user')

for row in cursor:
	print('------------------------------------------------------')
	print('id:\t\t\t', row[0])
	print('email:\t\t\t', row[1])
	print('confirmation_sent_on:\t', row[2])
	print('confirmed:\t\t', row[3])
	print('confirmed_on:\t\t', row[4])
	print('------------------------------------------------------')
