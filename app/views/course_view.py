from flask import jsonify, render_template, request, abort, url_for
from app.models.course import get_courses, get_course_by_name, add_course, update_course_in_database, delete_course
from flask import Blueprint
 
course_view_api = Blueprint('course_view_api', __name__)
 
 
# Define the routes and controller functions
@course_view_api.route('/courses', methods=['GET'])
def get_all_courses():
    courses = get_courses()
    return jsonify(courses)
 
@course_view_api.route('/courses/<string:name>', methods=['GET'])
def get_course(name):
    course = get_course_by_name(name)
    if course:
        return jsonify(course)
    else:
        abort(404, "Course not found")
 
@course_view_api.route('/courses', methods=['POST'])
def add_new_course():
    print("Received request:", request.form)
    data = request.json  # Change to request.form to access form data
    if not data:
        return jsonify({'error': 'No form data received'}), 400
 
    # Check if all required keys are present
    required_keys = ['name', 'description', 'instructor', 'duration']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Missing required keys in form data'}), 400
   
    # Extract data from form
    name = data['name']
    description = data['description']
    instructor = data['instructor']
    duration = data['duration']
 
    add_course(name, description, instructor, duration)
    return jsonify({'message': 'Course added successfully'}), 201
 
 
@course_view_api.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    print("Received request to update course with ID:", course_id)
    data = request.json # Change to request.form to access form data
    if not data:
        return jsonify({'error': 'No form data received'}), 400
 
    # Check if all required keys are present
    required_keys = ['name', 'description', 'instructor', 'duration']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Missing required keys in form data'}), 400
   
    # Extract data from form
    name = data['name']
    description = data['description']
    instructor = data['instructor']
    duration = data['duration']
 
    update_course_in_database(course_id, name, description, instructor, duration)
    return jsonify({'message': 'Course added successfully'}), 200




 
@course_view_api.route('/courses/<string:name>', methods=['DELETE'])
def delete_existing_course(name):
    delete_course(name)
    return jsonify({'message': 'Course deleted successfully'}), 200
 
@course_view_api.route('/')
def index():
    return 'Welcome to the Course Management System!'
 
@course_view_api.route('/add_course')
def add_course_form():
    return render_template('add_course.html')
 
 
 