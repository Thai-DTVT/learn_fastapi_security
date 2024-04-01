from sqlmodel import (
    SQLModel,
    create_engine,
)  # import cac thanh phan can thiet tu thu vien SQLModel de lam viec voi csdl va tao doi tuong du lieu
from sqlmodel import Session

# Khai báo đường dẫn kết nối đến cơ sở dữ liệu SQLite
DATABASE_URL = "sqlite:///./test.db"

# Tạo engine để kết nối đến cơ sở dữ liệu
engine = create_engine(DATABASE_URL, echo=True)


# Tạo bảng trong cơ sở dữ liệu
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


create_db_and_tables()


# Tạo session
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
