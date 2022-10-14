import mysql.connector

from sqlalchemy import create_engine

import pandas as pd

db_connection_str = 'mysql+pymysql://root:rootpass@localhost/ecommerce'

db_connection = create_engine(db_connection_str)
# Connetto il database al progetto

#parametri per programma SQL
user = 'root'
password = 'rootpass'
host = '127.0.0.1'
database = 'ecommerce'

def connection_database (user, password, host, database):
    try:
        conn = mysql.connector.connect(user=user, password=password, host=host, database=database)
        return conn
    except  mysql.connector.errors.DatabaseError as db_error:
        print(db_error.msg)
        return None

conn = connection_database(user, password, host, database)
cursor = conn.cursor()

# Definisco una funzione che permette di cambiare solamente i parametri della query

def query(select, frm, join_1=None, join_2=None, where=None, groupby=None, orderby=None):
    stmt = 'select %s from %s ' % (select,frm)
    if join_1 is not None:
        stmt = stmt + 'join %s ' % join_1
    if join_2 is not None:
        stmt = stmt + 'join %s ' % join_2
    if where is not None:
        stmt = stmt + 'where %s ' % where
    if groupby is not None:
        stmt = stmt + 'group by %s ' % groupby
    if orderby is not None:
        stmt = stmt + 'order by %s' % orderby
    stmt = stmt + ';'
    return stmt



select = 'citta'
frm = 'indirizzo' 
join_1 = 'utente on utente.uid=indirizzo.uid'
join_2 = None
where = 'rag_soc is not null'
groupby = None
orderby = None

domanda_1 = query(select,frm,join_1,join_2,where,groupby,orderby)

cursor.execute(domanda_1)
q1 = cursor.fetchmany()
print('La risposta alla tua query in SQL:', q1)



# Definisco una funzione su Pandas per eseguire query SQL

def il_panda (tab):
    tabella = pd.read_sql(tab,db_connection)
    return tabella

tab = 'select citta from indirizzo join utente on utente.uid=indirizzo.uid where rag_soc is not null'
tab_1 = il_panda(tab)
print('La risposta alla tua query in PANDAS:',tab_1)

conn.close()