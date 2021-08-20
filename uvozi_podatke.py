import sqlite3
import csv

baza_datoteka = 'eksoticni_resort.db'

def uvoziSQL(cur, datoteka):
    with open(datoteka) as f:
        koda = f.read()
        cur.executescript(koda)


def uvoziCSV(cur, tabela):
    with open('podatki/{0}.csv'.format(tabela)) as csvfile:
        podatki = csv.reader(csvfile)
        vsiPodatki = [vrstica for vrstica in podatki]
        glava = vsiPodatki[0]
        vrstice = vsiPodatki[1:]
        cur.executemany("INSERT INTO {0} ({1}) VALUES ({2})".format(
            tabela, ",".join(glava), ",".join(['?']*len(glava))), vrstice)


with sqlite3.connect(baza_datoteka) as baza:
    cur = baza.cursor()
    uvoziSQL(cur, 'eksoticni_resort.sql')
    uvoziSQL(cur, 'podatki\gost.sql')
    uvoziSQL(cur, 'podatki\zaposleni.sql')
    uvoziSQL(cur, 'podatki\sobe.sql')
    uvoziSQL(cur, 'podatki\\nastanitve.sql')
    uvoziSQL(cur, 'podatki\hrana.sql')