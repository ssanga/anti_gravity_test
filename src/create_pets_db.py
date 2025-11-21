import sqlite3

def create_database():
    db_path = 'pets.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create table with English column names
    # id (autoincremental), name, color, birth_year, species, breed
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            color TEXT,
            birth_year INTEGER,
            species TEXT,
            breed TEXT
        )
    ''')

    # 10 animals to insert
    pets_data = [
        ('Bella', 'Brown', 2020, 'Dog', 'Labrador'),
        ('Luna', 'White', 2019, 'Cat', 'Siamese'),
        ('Charlie', 'Golden', 2021, 'Dog', 'Golden Retriever'),
        ('Lucy', 'Black', 2018, 'Cat', 'Bombay'),
        ('Max', 'Spotted', 2022, 'Dog', 'Dalmatian'),
        ('Cooper', 'Red', 2020, 'Dog', 'Irish Setter'),
        ('Milo', 'Orange', 2021, 'Cat', 'Tabby'),
        ('Rocky', 'Grey', 2019, 'Dog', 'Bulldog'),
        ('Daisy', 'White/Brown', 2023, 'Rabbit', 'Holland Lop'),
        ('Coco', 'Brown', 2017, 'Dog', 'Poodle')
    ]

    # Insert data
    cursor.executemany('''
        INSERT INTO pets (name, color, birth_year, species, breed)
        VALUES (?, ?, ?, ?, ?)
    ''', pets_data)

    conn.commit()
    
    print(f"Database '{db_path}' created and 10 pets inserted successfully.")
    print("-" * 50)
    print(f"{'ID':<5} {'Name':<10} {'Color':<15} {'Year':<6} {'Species':<10} {'Breed'}")
    print("-" * 50)
    
    # Verify and display
    cursor.execute('SELECT * FROM pets')
    rows = cursor.fetchall()
    for row in rows:
        # row is a tuple: (id, name, color, birth_year, species, breed)
        print(f"{row[0]:<5} {row[1]:<10} {row[2]:<15} {row[3]:<6} {row[4]:<10} {row[5]}")

    conn.close()

if __name__ == '__main__':
    create_database()
