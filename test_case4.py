import sqlite3
from random import randrange

conn = sqlite3.connect('TestCase4.db')
c = conn.cursor()

c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='STORE_BOOK' ''')
if c.fetchone()[0]==1 :
    print('Table STORE_BOOK exists.')
else:
    conn.execute('''
            CREATE TABLE STORE_BOOK(
                ID_BOOK             INT PRIMARY KEY NOT NULL,
                NAME_BOOK           TEXT    NOT NULL,
                DESCRIPTION_BOOK    TEXT    NOT NULL,
                AUTHOR_BOOK         TEXT    NOT NULL,
                LIMIT_BOOK          INT
            );
    ''')
    print('Created Table STORE_BOOK.')

c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='USERS' ''')
if c.fetchone()[0]==1 :
    print('Table USERS exists.')
else:
    conn.execute('''
            CREATE TABLE USERS(
                ID_USER           INT PRIMARY KEY NOT NULL,
                NAME_USER         TEXT    NOT NULL,
                ADDRESS_USER      TEXT    NOT NULL
            );
    ''')
    print('Created Table USERS.')

c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='PEMINJAMAN' ''')
if c.fetchone()[0]==1 :
    print('Table PEMINJAMAN exists.')
else:
    conn.execute('''
            CREATE TABLE PEMINJAMAN(
                ID_PEMINJAMAN     INTEGER PRIMARY KEY AUTOINCREMENT,
                ID_USER_PEMINJAM  INT    NOT NULL,
                ID_BOOK           INT    NOT NULL,
                STATUS_PINJAMAN   TEXT   NOT NULL,
                Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            );
    ''')
    print('Created Table PEMINJAMAN.')

SESSION_ID_USER = 0
SESSION_NAME_USER = ""

while True:
    print("System Start... Welcome to Perpustakaan")
    print("Pilih Masukkan Perpustakaan")
    print("1. Login")
    print("2. Register")
    print("3. Lihat Buku")
    print("4. Peminjaman")
    pilihan = int(input())
    
    print()
    if pilihan == 0:
        print("Insert Seluruh Buku .. hanya untuk admin")
        conn.execute("INSERT INTO STORE_BOOK (ID_BOOK,NAME_BOOK,DESCRIPTION_BOOK,AUTHOR_BOOK,LIMIT_BOOK) VALUES (111, 'Harry Potter (Cursed of Black)', 'Bla bla bla...', 'Bla bla bla...', 2)")
        conn.execute("INSERT INTO STORE_BOOK (ID_BOOK,NAME_BOOK,DESCRIPTION_BOOK,AUTHOR_BOOK,LIMIT_BOOK) VALUES (222, 'Learning Programming', 'Bla bla bla...', 'Bla bla bla...', 1)")
        conn.execute("INSERT INTO STORE_BOOK (ID_BOOK,NAME_BOOK,DESCRIPTION_BOOK,AUTHOR_BOOK,LIMIT_BOOK) VALUES (333, 'Hand Writing Book', 'Bla bla bla...', 'Bla bla bla...', 3)")
        conn.commit()
    elif pilihan == 1:
        print("=== Login Data ===")
        print("Masukkan ID User : ")
        id_user = int(input())
        cursor = conn.execute("SELECT NAME_USER FROM USERS WHERE ID_USER = {}".format(id_user))
        for row in cursor.fetchall():
            SESSION_ID_USER = id_user
            SESSION_NAME_USER = row[0]
            print("Welcome ",row[0])
    elif pilihan == 2:
        print("=== Register Data ===")
        generated_id = randrange(100000, 1000000)
        print("Masukkan Nama : ")
        nama = input()
        print("Masukkan Alamat : ")
        alamat = input()
        print("Save your ID here... ",generated_id)
        script = "INSERT INTO USERS (ID_USER, NAME_USER, ADDRESS_USER) VALUES (?,?,?)"
        conn.execute(script, (generated_id, nama, alamat))
        conn.commit()
    elif pilihan == 3:
        print("Buku Perpustakaan yang tersediaa...")
        cursor = conn.execute("SELECT * FROM STORE_BOOK")
        for row in cursor.fetchall():
            print(f"ID BUKU : {row[0]} -- NAME : {row[1]} -- DESKRIPSI : {row[2]} -- BUKU TERSISA : {row[4]}")
    elif pilihan == 4:
        print("Masukkan ID Buku yang akan dipinjam")
        id_buku = int(input())
        nama_buku = ""
        sisa_buku = 0
        cursor = conn.execute("SELECT ID_BOOK, NAME_BOOK ,LIMIT_BOOK FROM STORE_BOOK WHERE ID_BOOK = {}".format(id_buku))
        for row in cursor.fetchall():
            print(f"Buku yang anda pilih : {row[1]} -- SISA : {row[2]}")
            nama_buku = row[1]
            sisa_buku = row[2]
        print("Anda yakin akan meminjam ? YES/NO ")
        persetujuan = str(input())
        if persetujuan == 'YES':
#             if SESSION_ID_USER == 0:
#                 print("Anda guest, mohon login")
#             else:
            sisa_buku -= 1
            cursor = conn.execute("UPDATE STORE_BOOK set LIMIT_BOOK = {} WHERE ID_BOOK = {}".format(sisa_buku, id_buku))
            
            script_peminjam = "INSERT INTO PEMINJAMAN (ID_USER_PEMINJAM, ID_BOOK, STATUS_PINJAMAN) VALUES (?,?,?)"
            conn.execute(script_peminjam, (SESSION_ID_USER, id_buku, "PINJAM"))
            print("Anda telah meminjam")
    
    print()

conn.close()
