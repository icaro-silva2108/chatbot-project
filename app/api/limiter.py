from flask import request
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from flask_limiter import Limiter

# Identificação para rate limiter(JWT ou IP)
def jwt_or_ip_identifier():

    jwt_identifier = verify_jwt_in_request(optional=True)
    if jwt_identifier:
        return str(get_jwt_identity())
    else:
        return request.remote_addr

limiter = Limiter(
    key_func=jwt_or_ip_identifier,
    default_limits=["150 per minute"]
    )

def init_limiter(app):    
    limiter.init_app(app)