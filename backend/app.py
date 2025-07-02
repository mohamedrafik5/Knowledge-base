from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL
from config import MYSQL_CONFIG
from routes.auth_routes import auth_bp

app = Flask(__name__)

# ✅ Setup CORS to allow requests from frontend
CORS(app, resources={r"/api/*": {"origins": "*"}})

# ✅ MySQL config
app.config['MYSQL_HOST'] = MYSQL_CONFIG['host']
app.config['MYSQL_USER'] = MYSQL_CONFIG['user']
app.config['MYSQL_PASSWORD'] = MYSQL_CONFIG['password']
app.config['MYSQL_DB'] = MYSQL_CONFIG['database']

mysql = MySQL(app)
app.mysql = mysql

# ✅ Register auth routes
app.register_blueprint(auth_bp, url_prefix="/api/auth")

if __name__ == "__main__":
    app.run(debug=True, port=5050)
