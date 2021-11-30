from datetime import datetime, timedelta
from jose import jwt
from jose.constants import Algorithms


#CONFIGURATION

SECRET_KEY = 'cdcfe6daf28136bbf7df921d61010e96'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 3600

def create_acess_token(data : dict):
    dataToken = data.copy()
    expiration = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    dataToken.update({'exp': expiration})

    token_jwt = jwt.encode(dataToken, SECRET_KEY, algorithm=ALGORITHM)

    return token_jwt

def verify_acess_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    return payload.get('sub')