from flask import Flask
from app.api.public_routes import public_routes
from app.api.protected_routes import protected_routes
from app.api.JWTmanager import init_jwt
from app.api.limiter import init_limiter
from datetime import timedelta

app = Flask(__name__, static_folder="static")

app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=15)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=7)

# Inicializa JWT
init_jwt(app)

# Inicializa limiter
init_limiter(app)

# Registro de Blueprints
app.register_blueprint(public_routes, url_prefix="/api")
app.register_blueprint(protected_routes, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)