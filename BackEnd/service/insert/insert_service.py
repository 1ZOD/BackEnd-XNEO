from config.__db import configure_mysql


class Insert:
    def __init__(self,mysql):
        self.mysql = mysql
        
    def get_All(self):
        cursor = self.mysql.get_db().cursor()
        cursor.execute("SELECT * FROM tasks")
        data = cursor.fetchall()
        cursor.close()

        return data