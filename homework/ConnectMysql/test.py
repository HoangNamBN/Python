from mysql.connector import MySQLConnection, Error


def connect():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'passwd': '',
        'database': 'UserAccount'
    }

    # Biến lưu trữ kết nối
    conn = None

    try:
        conn = MySQLConnection(**db_config)
        if conn.is_connected():
            print("Kết nối thành công")
            return conn
    except Error as error:
        print(error)

    return conn


# Test thử
conn = connect()
print(conn)
