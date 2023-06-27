from config.__db import configure_mysql


class Update:
    def __init__(self,mysql):
        self.mysql = mysql
        
    def update(self, id, new_description):
        cursor = self.mysql.get_db().cursor()
        query = "UPDATE tasks SET task_content = %s WHERE id_task = %s"
        cursor.execute(query, (new_description, id))
        self.mysql.get_db().commit()
        cursor.close()
