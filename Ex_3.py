import mysql.connector

user = 'root'
password = 'root'
host = '127.0.0.1'
database = 'discografia'

#cursor.execute("CREATE DATABASE discografia") #cerco di creare il database

def connection_database (user, password, host, database):
    try:
        conn = mysql.connector.connect(user=user, password=password, host=host, database=database)
        return conn
    except  mysql.connector.errors.DatabaseError as db_error:
        print(db_error.msg)
        return None

conn = connection_database(user, password, host, database)
cursor = conn.cursor()

select = 'NomeCantante'
frm = 'canzone'
join1 = 'esecuzione on canzone.CodiceReg=esecuzione.CodiceReg'
join2 = 'autore on esecuzione.TitoloCanzone=autore.TitoloCanzone'
where = 'nome=NomeCantante and nome like ‘D%’'


def query(select, frm, join1=None, join2=None, where=None, groupby=None, orderby=None ):
    stmt = 'select %s from %s ' % (select,frm)
    if join1 is not None:
        stmt = stmt + 'join %s ' % join1
    if join2 is not None:
        stmt = stmt + 'join %s ' % join2
    if where is not None:
        stmt = stmt + 'where %s ' % where
    if groupby is not None:
        stmt = stmt + 'group by %s ' % groupby
    if orderby is not None:
        stmt = stmt + 'order by %s' % orderby
    stmt = stmt + ';'
    return stmt

ex_1 = query(select,frm,join1,join2,where)
print(ex_1)

select = 'TitoloAlbum'
frm = 'disco'
join1 = 'contiene on disco.NroSerie=contiene.NroSerieDisco'
join2 = 'esecuzione on contiene.CodiceReg=esecuzione.CodiceReg'
where = 'esecuzione.Anno is NULL'

ex_2 = query(select,frm,join1,join2,where)
print(ex_2)

select = 'distinct NomeCantante'
frm = 'cantante'
join1 = None
join2 = None
select2 = 'S1.NomeCantante'
frm2 = 'cantante as S1'
select3 = 'CodiceReg'
frm3 = 'cantante as S2'
where3 = 'S2.NomeCantante <> S1.NomeCantante'
where2 = 'CodiceReg not in' + query(select3,frm3,where3)
where = 'NomeCantante not in' + query(select2,frm2,where2)

esercizio3 = query(select,frm,join1,join2,where)
print(esercizio3)

select = 'NomeCantante'
frm = 'cantante'
join1 = None
join2 = None
select2 = 'S1.NomeCantante'
frm2 = 'cantante as S1'
join3 = 'esecuzione on CodiceReg=S1.CodiceReg'
join4 = 'cantante as S2 on CodiceReg=S2.CodiceReg'
where2 = 'S1.NomeCantante <> S2.NomeCantante'
where = 'NomeCantante not in' + query(select2, frm2, join3, join2, where2)

ex_4 = query(select,frm,join1,join2,where)
print(ex_4)


cursor.execute(ex_1)
conn.commit()

insert = ''
list1 = []
list2 = []

def inserimento(insert,list1,list2):
    stm = 'insert into %s ' % (insert)
    stm + '('
    for i in range(len(list1)):
        stm = stm + list1[i] + ' '
    stm = stm + ') values ('
    for k in range(len(list2)):
        stm = stm + list2[k] + ' '
    stm = stm + ')'
    return stm

inserimento1 = inserimento(insert,list1,list2)
print(inserimento1)

delete = ''
d_where = ''

def eliminazione(delete,d_where):
    stm = 'delete from %s ' % (delete)
    stm = stm + d_where
    return stm

eliminazione1 = eliminazione(delete,d_where)
print(eliminazione1)




def close_connection(connection):
    connection.close()