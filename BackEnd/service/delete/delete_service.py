from config.__db import configure_mysql

class Delete:
    def __init__(self,mysql):
        self.mysql = mysql
        
    def delete(self, id):
        cursor = self.mysql.get_db().cursor()
        query = "DELETE FROM tasks WHERE id_task = %s"
        cursor.execute(query, (id,))
        self.mysql.get_db().commit()
        cursor.close()