from config import MYSQL_CONNECTION
def get_courses():
    cur = MYSQL_CONNECTION.cursor()
    cur.execute("SELECT * FROM courses")
    courses = cur.fetchall()
    cur.close()
    return courses
 
def get_course_by_name(name):
    cur = MYSQL_CONNECTION.cursor()
    cur.execute("SELECT * FROM courses WHERE name = %s", (name,))
    course = cur.fetchone()
    cur.close()
    return course
 
def add_course(name, description, instructor, duration):
    cur = MYSQL_CONNECTION.cursor()
    cur.execute("INSERT INTO courses (name, description, instructor, duration) VALUES (%s, %s, %s, %s)",
                (name, description, instructor, duration))
    MYSQL_CONNECTION.commit()
    cur.close()
 
def update_course_in_database(course_id, name, description, instructor, duration):
    cur = MYSQL_CONNECTION.cursor()
    cur.execute("UPDATE courses SET description=%s, instructor=%s, duration=%s, name=%s WHERE course_id=%s",
                (description, instructor, duration, name, course_id))
    MYSQL_CONNECTION.commit()
    cur.close()

 
def delete_course(name):
    cur = MYSQL_CONNECTION.cursor()
    cur.execute("DELETE FROM courses WHERE name = %s", (name,))
    MYSQL_CONNECTION.commit()
    cur.close()