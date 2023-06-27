from config.__db import configure_mysql


class Insert:
    def __init__(self, mysql):
        self.mysql = mysql
        
    def post_task(self, value):
        cursor = self.mysql.get_db().cursor()
        query = "INSERT INTO tasks (task_content) VALUES (%s)"
        cursor.execute(query, (value,))
        self.mysql.get_db().commit()
        cursor.close()
        