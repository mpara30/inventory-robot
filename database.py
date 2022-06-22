def inserare_produs(database, cursor, product):
    cursor.execute("INSERT INTO produse (produs) VALUES (%s)", (product,))
    database.commit()
    print(cursor.rowcount, "PRODUS ADAUGAT CU SUCCES!")


def creare_tabel(cursor):
    cursor.execute("CREATE TABLE produse (id INT AUTO_INCREMENT PRIMARY KEY, produs VARCHAR(255))")


def stergere_tabel(cursor):
    cursor.execute("DROP TABLE produse")
