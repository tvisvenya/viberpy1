import sqlite3

#DB = '/home/rosto/.ViberPC/380938481360/viber.db'
DB = "C:/Users/rosto/AppData/Roaming/ViberPC/380938481360/viber.db"

conn = sqlite3.connect(DB)
conn.isolation_level = None


def clearEvents(id):
    db_write = conn.cursor()
    db_write.execute('Delete FROM Events where EventID = ' + str(id) + ';')


def writeToEventsBack(sql):
    db_write = conn.cursor()
    q_to_back = 'INSERT INTO EventsBack values (NULL,' + str(sql[1]) + ', ' + str(sql[2]) + ', ' + str(sql[3]) + ', ' + \
                str(sql[4]) + ', ' + str(sql[5]) + ', ' + str(sql[6]) + ', ' + str(sql[7]) + ', ' + str(sql[8]) + ', ' + \
                str(sql[9]) + ', ' + str(sql[10]) + ',255);'
    db_write.execute(q_to_back)


def readForEvBack(num, typ):
    db_read = conn.cursor()
    db_read.execute('select * from Events where direction = 0 and number = "' + num + '" and type=' + typ + ';')
    return db_read.fetchall()


def loadNum():
    db_read = conn.cursor()
    db_read.execute('SELECT DISTINCT(Number) FROM Events WHERE Direction = 0;')
    return db_read.fetchall()


def checkCall():
    db_read = conn.cursor()
    db_read.execute('SELECT DISTINCT(Number) FROM Events WHERE Direction = 0 AND type = 1;')
    return db_read.fetchall()


def checkSms():
    db_read = conn.cursor()
    db_read.execute('SELECT DISTINCT(Number) FROM Events WHERE Direction = 0 AND type = 0;')
    return db_read.fetchall()
