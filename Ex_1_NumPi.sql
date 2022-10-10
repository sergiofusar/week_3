SELECT Citta FROM AEREOPORTO WHERE NumPiste IS Null;
SELECT TipoAereo FROM VOLO WHERE CittaPart= 'Torino';
SELECT CittaPart FROM VOLO WHERE CittaArr= 'Bologna';
SELECT CittaPart,CittaArr FROM VOLO WHERE IdVolo= 'AZ274';
SELECT TipoAereo, GiornoSett,OraPart FROM VOLO WHERE CittaPart LIKE 'B%O%' AND CittaArr LIKE '%E%A';