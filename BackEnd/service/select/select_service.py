from config.__db import configure_mysql


class Select:
    def __init__(self,mysql):
        self.mysql = mysql
        
    def get_All(self):
        cursor = self.mysql.get_db().cursor()
        cursor.execute("SELECT * FROM tasks")
        data = cursor.fetchall()
        cursor.close()

        tasks = []
        for row in data:
            task = {
                'id': row[0],
                'description': row[1]
            }
            tasks.append(task)

        return tasks