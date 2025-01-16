Creo els arxius (hi haurán canvis tant al codi com el nom dels arxius ja que els adaptaré a com m'agrada estructurar i nombrar el meu codi, ús de PascalCase i altres coses menys importants)
![1](../Captures/1.png)

Creo la mini llibreria (realment sól és 1 funció) per connectar-nos a la base de dades a través de la llibreria de psycopg2 (la funció retorna un objecte de connexió per interactuar amb la database amb el que podem utilitzar en altres scripts)
![2](../Captures/2.png)

També m'aseguro de que el docker-compose.yml tingui totes les dades correctes i que siguin les mateixes que les de connect.py
![3](../Captures/3.png)

Creo les mini llibreries que necessitem (CreateTableToDictionary, CSVToDictionary, DictionaryToDatabase), CreateTableToDictionary creará la taula a la base de dades, CSVToDictionary pasa un CSV a la estructura de dades d'un diccionari, DictionaryToDatabase transforma un dictionari a la comanda SQL per insertar dades a la base de dades
![4](../Captures/4.png)

Creo CreateTableToDictionary que simplement crea la taula de clients a la base de dades
![5](../Captures/5.png)

Creo CSVToDictionary llegeix el CSV amb Pandas y el transforma a un dicionari, passant la informació a DictionaryToDatabase per enviar-ho tot a la base de dades
![6](../Captures/6.png)

(També he creat la carpeta i descarregat l'arxiu Clientes.csv)
![9](../Captures/9.png)

Creo DictionaryToDatabase que transforma el diccionari a una comanda SQL per enviar a la base de dades, indexa a cada client a la taula amb el index que s'envia a través de la funció i inserta tots els valors per el client indicat a la instrucció SQL
![7](../Captures/7.png)

(He corregit l'estructura dels arxius)
![8](../Captures/8.png)