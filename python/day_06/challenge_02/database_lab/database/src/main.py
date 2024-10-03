from models.user import User
from models.user import Company
from db import Database


def main():
    """
    Main function that demonstrates the usage of the Database class.
    The function performs the following steps:
        1. Creates a connection to the SQLite database file "sqlite.db".
        2. Creates necessary tables in the database.
        3. Creates a list of User objects.
        4. Inserts each User object into the database.
        5. Retrieves a user with the ID of 1 from the database.
        6. Prints the retrieved user.
        7. If a user is found, updates the user's name to "John Smith" and deletes the user.
        8. Drops the tables from the database.
    """
    with Database("sqlite.db") as db:
        db.create_tables()

        users = [
            User(name="John Doe"),
            User(name="Jane Doe"),
            User(name="Jack Doe"),
            User(name="Jill Doe"),
        ]
        
        companies = [
            Company(name="Natixis"),
            Company(name="BPCE"),
            Company(name="Partecis")
            
        ]

        for user in users:
            db.create_user(user)
            
        for company in companies:
            db.create_company(company)
            
        user = db.get_user(1)
        
        company = db.read_company(2)

        print(user)
        print(company)

        # if user:
        #     db.update_user(user_id=user.id, name="John Smith")

        #     db.delete_user(user_id=user.id)

        # db.drop_tables()


if __name__ == "__main__":
    main()
