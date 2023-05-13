# Ce fichier constitue le fichier de création de la base de donnée.

import sqlite3

connection = sqlite3.connect("data.db")
c = connection.cursor()
# user_creation = """
#         CREATE TABLE users
#         (ID         INTEGER         PRIMARY KEY,
#         USERNAME    CHAR(20)        NOT NULL,
#         EMAIL       CHAR(100)       NOT NULL,
#         PASSWORD    CHAR(20)        NOT NULL,
#         ROLE        TEXT            NOT NULL)


# """


# FOREIGN KEY(COMMANDE_ID) REFERENCES COMMANDE(ID)  

item = """
        CREATE TABLE item
        (ID             INTEGER           PRIMARY KEY,
        
        
        
        
        )
"""


c.execute(user_creation)
connection.commit()
