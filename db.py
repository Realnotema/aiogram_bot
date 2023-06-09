import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchmany(1)
            return bool(len(result))

    def add_user(self, user_id, user_name):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (user_id, user_name) VALUES (?, ?)", (user_id, user_name,))

    def set_active(self, user_id, active):
        with self.connection:
            return self.cursor.execute("UPDATE users SET active = ? WHERE user_id = ?", (active, user_id,))

    def get_users(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id, active FROM users").fetchall()

    def plus_point(self, user_name, point):
        with self.connection:
            return self.cursor.execute("UPDATE users SET point = point + ? WHERE user_name = ?", (point, user_name,))

    def minus_point(self, user_name, point):
        with self.connection:
            return self.cursor.execute("UPDATE users SET point = point - ? WHERE user_name = ?", (point, user_name,))

    def get_point(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT point FROM users WHERE user_id = ?", (user_id,)).fetchone()

    def get_sorted(self):
        with self.connection:
            return self.cursor.execute("SELECT user_name, point FROM users ORDER BY point DESC").fetchall()
