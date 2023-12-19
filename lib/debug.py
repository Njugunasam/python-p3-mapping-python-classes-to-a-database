#!/usr/bin/env python3

from config import CONN, CURSOR
from song import Song
Song.create_table()





CURSOR.execute("PRAGMA table_info(songs)")
table_info = CURSOR.fetchall()
print("Table Info:", table_info)


if __name__ == '__main__':
    import ipdb
    ipdb.set_trace()
