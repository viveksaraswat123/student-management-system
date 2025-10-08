import pymysql

# Connect to the database
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="vivek",
    database="students",
    cursorclass=pymysql.cursors.DictCursor
)

# Create table if it doesn't exist
with conn.cursor() as cursor:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students_detail (
        uni_no INT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        course VARCHAR(255) NOT NULL,
        phone_number VARCHAR(15) NOT NULL
    );
    """)
    conn.commit()

def add_student(uni_no, name, course, phone_number):
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO students_detail (uni_no, name, course, phone_number) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (uni_no, name, course, phone_number))
            conn.commit()
            print("Student added successfully!")
    except Exception as e:
        print(f"Failed to add student: {e}")

def view_students():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM students_detail")
        return cursor.fetchall()

    conn.close()
def update_student(uni_no, name, course, phone_number):
    with conn.cursor() as cursor:
        sql = """
            UPDATE students_detail 
            SET name = %s, course = %s, phone_number = %s
            WHERE uni_no = %s
        """
        cursor.execute(sql, (name, course, phone_number, uni_no))
        conn.commit()

        if cursor.rowcount > 0:
            print("Student record updated successfully.")
        else:
            print("No student found with that University Number.")

def delete_student(uni_no):
    with conn.cursor() as cursor:
        sql = "DELETE FROM students_detail WHERE uni_no=%s"
        cursor.execute(sql, (uni_no,))
        conn.commit()



# def main():
#     while True:
#         print("\n1. Add Student")
#         print("2. View Students")
#         print("3. Exit")
#         choice = input("Choose an option: ")

#         if choice == '1':
#             uni_no = input("Enter University Number: ")
#             name = input("Enter Name: ")
#             course = input("Enter Course: ")
#             phone_number = input("Enter Phone Number: ")

#             if not uni_no or not name or not course or not phone_number:
#                 print("Please fill in all fields.")
#             else:
#                 add_student(uni_no, name, course, phone_number)

#         elif choice == '2':
#             view_students()

#         elif choice == '3':
#             print("Exiting...")
#             break

#         else:
#             print("Invalid option. Try again.")

# if __name__ == "__main__":
#     main()
