from config import MYSQL_CONNECTION

def add_course_content(course_id, title, description, duration):
    cur = MYSQL_CONNECTION.cursor()
    cur.execute("INSERT INTO course_content (course_content_id, title, description, duration) VALUES (%s, %s, %s, %s)",
                (course_id, title, description, duration))
    MYSQL_CONNECTION.commit()
    cur.close()

def update_course_content(course_id, content_id, title, description, duration):
    cur = MYSQL_CONNECTION.cursor()
    cur.execute("UPDATE course_content SET title=%s, description=%s, duration=%s WHERE id=%s AND course_content_id=%s",
                (title, description, duration, content_id, course_id))
    MYSQL_CONNECTION.commit()
    cur.close()

def delete_course_content(course_id, content_id):
    cur = MYSQL_CONNECTION.cursor()
    cur.execute("DELETE FROM course_content WHERE id=%s AND course_content_id=%s", (content_id, course_id))
    MYSQL_CONNECTION.commit()
    cur.close()

def get_course_content(course_id):
    cur = MYSQL_CONNECTION.cursor()
    cur.execute("SELECT * FROM course_content WHERE course_content_id = %s", (course_id,))
    content = cur.fetchall()
    cur.close()
    return content

def get_single_course_content(course_id, content_id):
    cur = MYSQL_CONNECTION.cursor()
    cur.execute("SELECT * FROM course_content WHERE course_content_id = %s AND id = %s", (course_id, content_id))
    content = cur.fetchone()
    cur.close()
    return content
