import sqlite3

class Database:
    def __init__(self, db_name="people_info.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            relationship TEXT,
            image_path TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_person(self, name, age, relationship, image_path):
        query = "INSERT INTO people (name, age, relationship, image_path) VALUES (?, ?, ?, ?)"
        self.conn.execute(query, (name, age, relationship, image_path))
        self.conn.commit()

    def find_person_by_face(self, face_embedding):
        # Placeholder for actual face embedding matching
        # Simulated match lookup in the database
        query = "SELECT * FROM people"
        cursor = self.conn.execute(query)
        for row in cursor:
            # In real implementation, compare embeddings (e.g., cosine similarity)
            if row[1] in face_embedding:  # Simulated match logic
                return {"name": row[1], "age": row[2], "relationship": row[3]}
        return None

    def close(self):
        self.conn.close()
