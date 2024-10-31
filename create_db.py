from app import app, db  

with app.app_context():
       print("Creating database...")
       db.create_all()  # This creates the database and tables
       print("Database created.")