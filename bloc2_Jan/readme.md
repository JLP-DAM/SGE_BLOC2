Creo els arxius (hi haurán canvis tant al codi com el nom dels arxius ja que els adaptaré a com m'agrada estructurar i nombrar el meu codi, ús de PascalCase i altres coses menys importants)

![1](Captures/1.png)

Creo la mini llibreria (realment sól és 1 funció) per connectar-nos a la base de dades a través de la llibreria de psycopg2 (la funció retorna un objecte de connexió per interactuar amb la database amb el que podem utilitzar en altres scripts)

![2](Captures/2.png)

També m'aseguro de que el docker-compose.yml tingui totes les dades correctes i que siguin les mateixes que les de connect.py

![3](Captures/3.png)

Creo les mini llibreries que necessitem (CreateTableToDictionary, CSVToDictionary, DictionaryToDatabase), CreateTableToDictionary creará la taula a la base de dades, CSVToDictionary pasa un CSV a la estructura de dades d'un diccionari, DictionaryToDatabase transforma un dictionari a la comanda SQL per insertar dades a la base de dades

![4](Captures/4.png)

Creo CreateTableToDatabase que simplement crea la taula de clients a la base de dades

![5](Captures/5.png)

Creo CSVToDictionary llegeix el CSV amb Pandas y el transforma a un dicionari, passant la informació a DictionaryToDatabase per enviar-ho tot a la base de dades

![6](Captures/6.png)

(També he creat la carpeta i descarregat l'arxiu Clientes.csv)

![9](Captures/9.png)

Creo DictionaryToDatabase que transforma el diccionari a una comanda SQL per enviar a la base de dades, indexa a cada client a la taula amb el index que s'envia a través de la funció i inserta tots els valors per el client indicat a la instrucció SQL

![7](Captures/7.png)

(He corregit l'estructura dels arxius)

![8](Captures/8.png)

He creat les taules a través del script

![10](Captures/10.png)
![11](Captures/11.png)

I les he populat

![12](Captures/12.png)
![13](Captures/13.png)

Creo el CreateRegister i modifico Main per probar que funcioni CreateRegister, l'executo i comprovo que s'hagi creat el registre. (podem veure que apareix com l'ultim de la taula)

![14](Captures/14.png)
![15](Captures/15.png)
![16](Captures/16.png)
![17](Captures/17.png)

Fico el codi a ReadRegister per llegir tota la taula de Clientes, i he modificat register per que pugui mostrar de forma llegible els resultats.

![18](Captures/18.png)
![19](Captures/19.png)
![20](Captures/20.png)

Creo el UpdateRegister per actualitzar la base de dades a través de l'script i utilitzo el Main creat abans per llegir els canvis (hem vist que les captures anteriors han mostrat la informació previa a ser editada, podem veure les diferencies)
(* a partir d'aqui, m'he adonat que la a la taula li falta la id_cliente, he fet les modificacions necesaries, he canviat els scripts i he renovat algunes captures de pantalla per mantenir coherencia)

![21](Captures/21.png)
![22](Captures/22.png)
![23](Captures/23.png)
![24](Captures/24.png)
![25](Captures/25.png)

Creo el DeleteRegister per borrar clients de la base de dades i utilitzo el Main creat previament per veure que ja no existeixen els 3 Clients que he canviat amb UpdateRegister

![26](Captures/26.png)
![27](Captures/27.png)
![28](Captures/28.png)
![29](Captures/29.png)
![30](Captures/30.png)