import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host = host, 
        port = 3306,
        user = user,
        password = password,
        database = db_name,
        cursorclass = pymysql.cursors.DictCursor

        )
    print("Successfully connected")

    try:
        cursor = connection.cursor()

        create_query =  "CREATE TABLE IF NOT EXISTS connect(" \
                        "id INT PRIMARY KEY AUTO_INCREMENT," \
                        "firstname VARCHAR(45));"
        cursor.execute(create_query)

        insert_query = "INSERT connect (firstname)"\
                        "VALUES ('Антон'),('Alex');"
        cursor.execute(insert_query)
        connection.commit()
        

        update_query = "UPDATE connect SET firstname = 'Mike' WHERE id = 1;"
        cursor.execute(update_query)
        connection.commit()

        delete_query = "DELETE FROM connect WHERE id = 1;"
        cursor.execute(delete_query)
        connection.commit()

        select_query = "SELECT * from connect"
        cursor.execute(select_query)

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    finally:

        connection.close()

   


except Exception as ex:
    print("disconnected")
    print(ex)