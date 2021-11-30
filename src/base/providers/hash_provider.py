from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])

def hash_generate(text):
    return pwd_context.hash(text)

def hash_verify(text, hash):
    return pwd_context.verify(text, hash)