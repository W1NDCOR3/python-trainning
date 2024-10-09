import os
import psycopg2

# Function to save results to PostgreSQL database
def save_result_to_db(operation, result):
    try:
        # Connect to PostgreSQL database
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        cursor = conn.cursor()

        # Create the table if it does not exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS results (
                id SERIAL PRIMARY KEY,
                operation TEXT NOT NULL,
                result TEXT NOT NULL
            )
        """)

        # Insert the result into the table
        cursor.execute(
            "INSERT INTO results (operation, result) VALUES (%s, %s)",
            (operation, result)
        )

        # Commit the changes and close the connection
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"An error occurred while saving to the database: {e}")

# Main function for calculator logic
def main():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter operation (+, -, *, /): ")

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2
            else:
                print("Invalid operation")
                continue

            result_str = f"The result is: {result}"
            print(result_str)

            # Save the operation and result to the database
            operation_str = f"{num1} {operation} {num2}"
            save_result_to_db(operation_str, str(result))

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
