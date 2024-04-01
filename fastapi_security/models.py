from sqlmodel import Field, SQLModel


# Model SQLModel cho người dùng
class UserBase(SQLModel):
    username: str
    password: str
    full_name: str = None
    disabled: bool = False


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class Users(UserBase):
    pass
