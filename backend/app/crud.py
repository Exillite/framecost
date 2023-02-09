from models import User
import bcrypt

def get_hashed_password(plain_text_password: str) -> str:
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

def check_password(plain_text_password: str, hashed_password: str) -> bool:
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(plain_text_password, hashed_password)


def regidtration(name: str, surname: str, login: str, email: str, password: str) -> User:
    # Check if user exists
    if User.objects(email=email).first():
        return None
    if User.objects(login=login).first():
        return None
    
    user = User(name=name, surname=surname, email=email, password=get_hashed_password(password), role="user", is_active=True, login=login)
    user.save()
    return user

def login(email: str, password: str) -> User:
    user = User.objects(email=email).first()
    if user:
        if check_password(password, user.password):
            return user
        else:
            return None
    else:
        return None
    
def get_tocken(user: User) -> str:
    return get_hashed_password(user.email)

def update_user(name: str, surname: str, login: str) -> User:
    user = User.objects(login=login).first()
    if user:
        user.name = name
        user.surname = surname
        user.save()
        return user
    else:
        return None