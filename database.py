# Ce fichier constitue le fichier de création de la base de donnée.

import sqlite3

connection = sqlite3.connect("data.db")
c = connection.cursor()
user_creation = """
        CREATE TABLE users
        (ID         INTEGER         PRIMARY KEY     AUTOINCREMENT,
        USERNAME    CHAR(20)        NOT NULL,
        EMAIL       CHAR(100)       NOT NULL,
        PASSWORD    CHAR(20)        NOT NULL,
        ROLE        TEXT            NOT NULL)


"""

# SELECT_USER = """
#     SELECT * FROM users WHERE EMAIL = 'TEST@GMAIL.COM'
# """

c.execute(user_creation)
connection.commit()



# Création d'un item dans la base de données.
# item = """
#         CREATE TABLE item
#         (ID             INTEGER           PRIMARY KEY,
#         NAME            TEXT              NOT NULL,
#         PRIX            FLOAT             NOT NULL,
#         DISPONIBLE      BOOL              NOT NULL,
#         LOCATIONS       TEXT              NOT NULL
           
        
        
#         )
# """

# Création d'une commande dans la base de données.
# commande = """
#         CREATE table commande
#         (ID             INTEGER             PRIMARY KEY,
#         TOTAL           FLOAT               NOT NULL,
#         ITEMS           TEXT                NOT NULL,
#         DATE            TEXT                NOT NULL,
#         FOREIGN KEY(USER_ID) REFERENCES users(ID),
#         FOREIGN KEY(ITEMS) REFERENCES item(ID)
#         )



# """

# c.execute(commande)
# connection.commit()
