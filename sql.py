import mysql.connector
cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    port='3306',
    database='bizcard'
)
cursor = cnx.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS biz_card_data 
                    (id INTEGER PRIMARY KEY AUTO_INCREMENT,
                    name TEXT,
                    designation TEXT,
                    area TEXT,
                    city TEXT,
                    state TEXT,
                    pin_code VARCHAR(10),
                    Contact_no VARCHAR(50),
                    email_id TEXT,
                    website TEXT,
                    company_name TEXT,
                    image LONGBLOB )''')


