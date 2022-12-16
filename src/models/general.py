from models.core import BaseModel
from sqlalchemy import String, Column


class User(BaseModel):
    __repr_name__ = 'Пользователь системы'
    __tablename__ = 'users'

    first_name: str = Column(String(256), nullable=False, comment='Имя')
    last_name: str = Column(String(256), nullable=False, comment='Фамилия')
    middle_name: str = Column(String(256), nullable=False, comment='Отчество')
