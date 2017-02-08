from mysql.connector import MySQLConnection, Error

def insert_values(year, injuries, fatal_injuries, total_fatalities):
    query = "INSERT INTO oh_ohs(year, injuries, fatal_injuries, total_fatalities) " \
            "VALUES(%s, %s, %s, %s)"
    args = (year, injuries, fatal_injuries, total_fatalities)

    try:
        config = {
        'user': 'root',
        'password': 'admin',
        'host': 'localhost',
        'database': 'Jesse'
        }
        conn = MySQLConnection(**config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        # Commit changes to the db
        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()
        print("I finished succesfully")

def main():
   # execute one
   insert_values('2017','11111', 2, 4)

if __name__ == '__main__':
    main()
