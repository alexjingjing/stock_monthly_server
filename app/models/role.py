from flask_security import RoleMixin
from sqlalchemy import Column, Integer, \
    String

from app.models.database import Base


class Role(Base, RoleMixin):
    __tablename__ = 'role'
    id = Column(Integer(), primary_key=True)
    name = Column(String(80, collation='utf8_bin'), unique=True)
    description = Column(String(255, collation='utf8_bin'))
