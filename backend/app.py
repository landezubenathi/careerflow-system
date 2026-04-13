#THE FOLLOWING CODE WAS DONE ONLY FOR CHECKING THE COMMIT IN GITHUB. IT IS NOT PART OF THE ACTUAL APPLICATION. PLEASE IGNORE THIS CODE.

#THIS IS THE MAIN APPLICATION FILE FOR THE BACKEND OF THE CAREERFLOW SYSTEM. IT SETS UP THE FLASK APPLICATION AND REGISTERS THE AUTHENTICATION ROUTES.
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "CareerFlow API Running"}

if __name__ == '__main__':
    app.run(debug=True)

from routes.auth_routes import auth_bp

app.register_blueprint(auth_bp, url_prefix='/auth')