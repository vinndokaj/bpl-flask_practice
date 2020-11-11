import sqlite3

class Schema:
    def __init__ (self):
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_to_do_table()
    
    def create_to_do_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "todo" (
            id INTEGER PRIMARY KEY,
            Title TEXT,
            Description TEXT,
            _is_done INTEGER DEFAULT 0,
            _is_deleted INTEGER DEFAULT 0,
            CreatedOn Date DEFAULT CURRENT_DATE,
            DueDate Date,
            UserId INTEGER FOREIGNKEY REFERENCES User(_id)
        );"""

        self.conn.execute(query)
    
    def create_user_table(self):
        pass

class ToDoModel:
    TABLE_NAME = 'todo'

    def __init__ (self):
        self.conn = sqlite3.connect('todo.db')
        self.conn.row_factory = sqlite3.Row
    
    def create(self, params):
        query = f"INSERT INTO {self.TABLE_NAME} " \
                f"(Title, Description, DueDate, UserId) " \
                f'values ("{params.get("Title")}", "{params.get("Description")}", "{params.get("DueDate")}", "{params.get("UserId")}");'
        print(query)
        result = self.conn.execute(query)
        return result

    def list_items(self, where_clause=""):
        query = f"SELECT id, Title, Description, DueDate, _is_done " \
                f"from {self.TABLE_NAME} WHERE _is_deleted != {1} " + where_clause
        print (query)
        result_set = self.conn.execute(query).fetchall()
        print(result_set)
        result = [{column: row[i]
                  for i, column in enumerate(result_set[0].keys())}
                  for row in result_set]
        return result