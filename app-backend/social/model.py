import datetime
from social import database
from social.enums import Status


def now():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month  # 0 1 2 3 4 5
    if month < 10:
        month = '0' + str(month)
    day = datetime.datetime.now().day
    if day < 10:
        day = '0' + str(day)
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute

    return '{}-{}-{} {}:{}'.format(year, month, day, hour, minute)



class User(database.Model):
    __tablename__ = 'user'
    id = database.Column(database.Integer, autoincrement=True, primary_key=True, unique=True)
    email = database.Column(database.String(200), unique=True)
    password = database.Column(database.String(200))
    nick = database.Column(database.String(200), unique=True)
    status = database.Column(database.Integer, default=Status.OK)


class Topic(database.Model):
    __tablename__ = 'topic'
    id = database.Column(database.Integer, autoincrement=True, primary_key=True, unique=True)
    title = database.Column(database.String(250))
    vote = database.Column(database.Integer, default=0)
    content = database.Column(database.String(9999))
    published_by = database.Column(database.Integer, database.ForeignKey('user.id'))
    published_at = database.Column(database.String(20), default=now())
    updated_at = database.Column(database.String(20), default=now(), onupdate=now())
    status = database.Column(database.Boolean, default=True)


class Answer(database.Model):
    __tablename__ = 'answer'
    id = database.Column(database.Integer, autoincrement=True, primary_key=True)
    topic_id = database.Column(database.Integer, database.ForeignKey('topic.id'))
    title = database.Column(database.String(250))
    vote = database.Column(database.Integer(), default=0)
    content = database.Column(database.String(9999))
    published_by = database.Column(database.Integer, database.ForeignKey('user.id'))
    published_at = database.Column(database.String(20), default=now())
    updated_at = database.Column(database.String(20), default=now(), onupdate=now())
    status = database.Column(database.Boolean, default=True)


class Tag(database.Model):

    __tablename__ = 'tag'
    id = database.Column(database.Integer, autoincrement=True, primary_key=True)
    topic_id = database.Column(database.Integer, database.ForeignKey('topic.id'))
    tag = database.Column(database.String(25))
    status = database.Column(database.Boolean, default=True)


class APIClientSecurity(database.Model):
    __tablename__ = 'api_client_security'
    id = database.Column(database.Integer, autoincrement=True, primary_key=True)
    description = database.Column(database.String(250))
    client_key = database.Column(database.String(250), unique=True)
    refresh_key = database.Column(database.String(250), unique=True)
    status = database.Column(database.Boolean, default=True)


class APIUserSecurity(database.Model):
    __tablename__ = 'api_user_security'
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    user_email = database.Column(database.String(200), database.ForeignKey('user.email'), unique=True)
    access_token = database.Column(database.String(250), unique=True)
    ip_addess = database.Column(database.String(20))
    status = database.Column(database.Boolean, default=True)


class UserStar(database.Model):
    __tablename__ = 'user_star'
    id = database.Column(database.Integer, autoincrement=True, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'))
    topic_id = database.Column(database.Integer, database.ForeignKey('topic.id'))
    status = database.Column(database.Boolean, default=False)
    stared_at = database.Column(database.String(20), default=now(), onupdate=now())


class UserTopicVote(database.Model):
    id = database.Column(database.Integer, autoincrement=True, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'))
    topic_id = database.Column(database.Integer, database.ForeignKey('topic.id'))
    vote = database.Column(database.Integer, default=0)
    status = database.Column(database.Boolean, default=True)
    vote_date = database.Column(database.String(20), default=now(), onupdate=now())


class UserAnswerVote(database.Model):
    id = database.Column(database.Integer, autoincrement=True, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'))
    answer_id = database.Column(database.Integer, database.ForeignKey('answer.id'))
    vote = database.Column(database.Integer, default=0)
    status = database.Column(database.Boolean, default=True)
    vote_at = database.Column(database.String(20), default=now(), onupdate=now())