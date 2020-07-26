import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = sqlalchemy.create_engine('sqlite:///base.db', echo=False)
Base = declarative_base()
DB = sessionmaker(bind=engine)()


class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    city = Column(String)
    city_id = Column(Integer)
    is_hide = Column(Integer)


def save_user(user_id, first_name, last_name, city, city_id, is_hide):
    DB.add(
        User(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            city=city,
            city_id=city_id,
            is_hide=is_hide
        )
    )
    DB.commit()


class Public(Base):
    __tablename__ = 'public'
    public_id = Column(Integer, primary_key=True)
    name = Column(String)
    target = Column(Integer)
    link = Column(String)


def save_public(public_id, name, target, link):
    DB.add(
        Public(
            public_id=public_id,
            name=name,
            target=target,
            link=link,
        )
    )
    DB.commit()


def get_publics():
    return DB.query(Public).all()


def get_users():
    return DB.query(User).all()


class UserInThePublic(Base):
    __tablename__ = 'user_in_the_public'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    public_id = Column(Integer, ForeignKey('public.public_id'))
    user = relationship("User", foreign_keys=[user_id])
    public = relationship("Public", foreign_keys=[public_id])
    is_target = Column(Integer)


def create_tables():
    metadata = MetaData()
    user = Table(
        'user', metadata,
        Column('user_id', Integer, primary_key=True),
        Column('first_name', String),
        Column('last_name', String),
        Column('city', String),
        Column('city_id', Integer)
    )

    public = Table(
        'public', metadata,
        Column('public_id', Integer, primary_key=True),
        Column('name', String),
        Column('target', Integer),
        Column('link', String),
    )

    user_in_the_public = Table(
        'user_in_the_public', metadata,
        Column('id', Integer, primary_key=True),
        Column('user_id', Integer, ForeignKey('user.user_id')),
        Column('public_id', Integer, ForeignKey('public.public_id')),
        Column('is_target', Integer)
    )
    metadata.create_all(engine)


def get_user_in_the_public():
    return DB.query(UserInThePublic).all()


def save_user_in_the_public(user_id, public_id, is_target):
    DB.add(
        UserInThePublic(
            user_id=user_id,
            public_id=public_id,
            is_target=is_target,
        )
    )
    DB.commit()


if __name__ == '__main__':
    save_user_in_the_public(
        user_id=1,
        public_id=2,
        is_target=3
    )
