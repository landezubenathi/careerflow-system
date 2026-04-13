from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "CareerFlow API Running"}

if __name__ == '__main__':
    app.run(debug=True)

from routes.auth_routes import auth_bp

app.register_blueprint(auth_bp, url_prefix='/auth')