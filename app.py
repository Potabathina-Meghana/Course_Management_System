from flask import Flask
from app.views.course_view import course_view_api
from app.views.user_view import user_view_api
from app.views.course_content_view import course_content_api

cms = Flask(__name__)
cms.register_blueprint(course_view_api)
cms.register_blueprint(user_view_api)
cms.register_blueprint(course_content_api)


if __name__ == '__main__':
    cms.run(debug=True)
