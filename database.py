# Ce fichier constitue le fichier de création de la base de donnée.

import sqlite3

connection = sqlite3.connect("data.db")
c = connection.cursor()
user_creation = """
        CREATE TABLE users
        (ID         INTEGER         PRIMARY KEY,
        USERNAME    CHAR(20)        NOT NULL,
        EMAIL       CHAR(100)       NOT NULL,
        PASSWORD    CHAR(20)        NOT NULL,
        ROLE        TEXT            NOT NULL)


"""

SELECT_USER = """
    SELECT * FROM users WHERE EMAIL = 'TEST@GMAIL.COM'
"""

res = c.execute(SELECT_USER)
print(res.fetchall())
# FOREIGN KEY(COMMANDE_ID) REFERENCES COMMANDE(ID)  


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
