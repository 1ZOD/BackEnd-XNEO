from config.__db import configure_mysql


class Insert:
    def __init__(self,mysql):
        self.mysql = mysql
        
    def post_task(self,value):
        cursor = self.mysql.get_db().cursor()
        cursor.execute(f"INSERT INTO tasks(task_content)VALUES({value})")
        data = cursor.fetchall()
        cursor.close()

        return data