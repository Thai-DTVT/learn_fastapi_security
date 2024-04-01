from passlib.context import CryptContext
from models import User
from sqlmodel import Session

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


# Hàm tìm người dùng theo tên đăng nhập
def get_user(username: str, db: Session):
    return db.query(User).filter(User.username == username).first()


# Hàm kiểm tra tên người dùng và mật khẩu
def authenticate_user(username: str, password: str, db: Session):
    user = get_user(username, db)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user
