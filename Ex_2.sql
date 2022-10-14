
select NomeCantante
from CANTANTE join ESECUZIONE on CANTANTE.CodiceReg=ESECUZIONE.CodiceReg
join AUTORE on ESECUZIONE.TitoloCanz=AUTORE.TitoloCanzone
where Nome=NomeCantante and Nome like ‘d%’


select TitoloAlbum
from DISCO join CONTIENE on DISCO.NroSerie=CONTIENE.NroSerieDisco
join ESECUZIONE on CONTIENE.CodiceReg=ESECUZIONE.CodiceReg
where ESECUZIONE.anno is NULL


select distinct NomeCantante from CANTANTE
where NomeC not in
      ( select S1.NomeCantante
        from CANTANTE as S1
        where CodiceReg not in
           ( select CodiceReg
             from CANTANTE S2
             where S2.NomeCantante <> S1.NomeCantante ) )


select NomeCantante
from CANTANTE
where NomeCantante not in ( select S1.NomeCantante
       from CANTANTE as S1 join ESECUZIONE on CodiceReg=S1.CodiceReg
            join CANTANTE as S2 on CodiceReg=S2.CodiceReg )
       where S1.NomeCantante<> S2.NomeCantante
