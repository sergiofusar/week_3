--1 prodotti con quantita > 10
select nome from prodotto where quantita < 11;

--2 selezionare le città con rivenditori
select citta from indirizzo join utente on utente.uid=indirizzo.uid where rag_soc is not null;

--3 Descrizione dei prodotti 
select marca.nome,prodotto.descr_lunga from marca join prodotto on prodotto.mid=marca.mid where descr_lunga is not Null ;

--4 utenti che sono iscritti alla newsletter
select nome from utente where email = 1;

--5 rimanenze magazzino 
select marca.nome,prodotto.quantita from marca join prodotto on prodotto.mid=marca.mid where prodotto.quantita >1;

--6 Mostrami gli amministratori del sito
select utente.nome from utente join livello on livello.uid=utente.uid where livello.uid = "admin" ;

--7 prodotti terminati
select marca.nome, prodotto.quantita from marca join prodotto on prodotto.mid=marca.mid where prodotto.quantita =0;

--8 Selezione dei nomi utente che hanno effettuato più di 10 ordini
select utente.nome,orpr01.quantita from utente join listino on listino.Isid=utente.Isid join orpr01 on orpr01.Isid=listino.Isid where orpr01 >10; 

--9 Prodotti in arrivo con descrizione
select marca.nome,prodotto.descr_lunga,prodotto.arrivo from marca join prodotto on prodotto.mid=marca.mid where arrivo >= 1;

--10 Totale utenti con partita iva
select utente.piva, COUNT(utente.piva) from utente where utente.piva >0 group by "piva"