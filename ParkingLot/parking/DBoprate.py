import psycopg2

def DBInsert(TBName,val):
    conn = psycopg2.connect(database="parkinglot", user="postgres", password="123456", host="localhost", port="5432")
    print("Opened database successfully")

    cur = conn.cursor()
    str = "INSERT INTO " + TBName + " VALUES " + val + ";"
    cur.execute(str)

    conn.commit()
    print("Records created successfully")
    conn.close()

# DBInsert("parking_info.car_info","(2,'B','Tom')")
def DBDelete(TBName,exp):
    conn = psycopg2.connect(database="parkinglot", user="postgres", password="123456", host="localhost", port="5432")
    print("Opened database successfully")

    cur = conn.cursor()
    str = "DELETE from " + TBName + " where " + exp + ";"
    cur.execute(str)

    conn.commit()
    print("Total number of rows deleted :", cur.rowcount)
    conn.close()

# DBDelete("parking_info.car_info","id='2'")

def DBUpdate(TBName,exp1,exp2):
    conn = psycopg2.connect(database="parkinglot", user="postgres", password="123456", host="localhost", port="5432")
    print("Opened database successfully")

    cur = conn.cursor()
    str = "UPDATE " + TBName + " set " + exp1 + " where " + exp2 + ";"
    cur.execute(str)

    conn.commit()
    print("Total number of rows updated :", cur.rowcount)
    conn.close()

# DBUpdate("parking_info.car_info","type = 'C'","id='1'")

def DBSelect(TBName,exp1,exp2):
    conn = psycopg2.connect(database="parkinglot", user="postgres", password="123456", host="localhost", port="5432")
    print("Opened database successfully")

    cur = conn.cursor()
    str = "SELECT " + exp1 + " from " + TBName + " " + exp2 + ";"
    cur.execute(str)
    rows = cur.fetchall()
    conn.commit()
    print("Operation done successfully")
    conn.close()
    return rows

# rows = DBSelect("parking_info.car_info","*","")
# print(rows)
def DBTruncate(TBName):
    conn = psycopg2.connect(database="parkinglot", user="postgres", password="123456", host="localhost", port="5432")
    print("Opened database successfully")

    cur = conn.cursor()
    str = "TRUNCATE " + TBName + " ;"
    cur.execute(str)

    conn.commit()
    conn.close()
