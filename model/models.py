from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from config import mysql_config
from utils import gravatar

Base = declarative_base()

class User(Base):
    __tablename__ = 'wt_user'
    uid = Column('u_id', Integer, primary_key = True)
    uname = Column('u_username', String(45))
    uemail = Column('u_email', String(45))
    upwd = Column('u_password', String(45))
    uavatar = Column('u_avatar', String(45))
    ucreatedate = Column('u_created_date', DateTime)

    