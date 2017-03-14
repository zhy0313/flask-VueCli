from flask import jsonify
from social import database
from social.model import User, Topic, Answer, APIClientSecurity, APIUserSecurity
import social.functions as functions


class APIClientSecurityHandler(object):

    def __init__(self):
        pass

    def is_client_exist(self, client_key=None, refresh_key=None):
        is_exist = False
        try:
            client = APIClientSecurity.query.filter_by(client_key=client_key, refresh_key=refresh_key).first()
            if client is not None:
                is_exist = True

        except Exception as e:
            functions.error()

        return is_exist


class ApiUserSecurityHandler(object):

    def __init__(self):
        pass

    def get_user_email_by_access_token(self, access_token=None) -> (bool, str):
        is_exist, user_email = False, None
        if access_token is not None:
            try:
                api_user_security = APIUserSecurity.query.filter_by(access_token=access_token).first()
                if api_user_security is not None:
                    is_exist = True
                    user_email = api_user_security.user_email
            except Exception as e:
                error()
        return is_exist, user_email


class UserHandler(object):

    def get_user_by_nick(self, nick=None) -> (bool, User):
        is_exist = False
        user = None
        if nick is not None:
            try:
                user = User.query.filter_by(nick=nick).first()
                if user is not None:
                    is_exist = True
            except Exception as e:
                error()
        return is_exist, user

    def get_user_by_email(self, email) -> (bool, User):
        is_exist = False
        user = None
        if email is not None:
            try:
                user = User.query.filter_by(email=email).first()
                if user is not None:
                    is_exist = True
            except Exception as e:
                error()
        return is_exist, user

    def get_user_by_id(self, user_id=None) -> User:
        user = None
        if user_id is not None:
            try:
                user = User.query.filter_by(id=user_id).first()
            except Exception as e:
                error()
            return user

    def is_email_or_nick_exist(self, email=None, nick=None) -> (bool, str):
        is_exist = True
        error_message = None
        if email is not None and nick is not None:
            try:
                email = User.query.filter_by(email=email).first()
                nick = User.query.filter_by(nick=nick).first()
                if email is None and nick is None:
                    is_exist = False
                elif email is not None and nick is not None:
                    error_message = 'email and nick have been already taken'
                elif email is not None:
                    error_message = 'email have been already taken'
                elif nick is not None:
                    error_message = 'nick have been already taken'

            except Exception as e:
                error()

        return is_exist, error_message

    def login(self, email=None, password=None) -> jsonify:
        is_logged_in = False
        error_message = None
        access_token = None
        if email is not None and password is not None:
            try:
                hashed_password = functions.generate_hashed_data(data=password)
                user = User.query.filter_by(email=email, password=hashed_password).first()
                if user is not None:
                    api_user_security = APIUserSecurity.query.filter_by(user_email=email).first()
                    if api_user_security is not None:
                        access_token = functions.generate_access_token(email=email)
                        api_user_security.access_token = access_token
                        database.session.commit()
                        is_logged_in = True
                else:
                    error_message = 'user is not found'

            except Exception as e:
                error()

        return jsonify(is_logged_in=is_logged_in, error_message=error_message, access_token=access_token)

    def register(self, email=None, nick=None, password=None) -> jsonify:
        is_registered = False
        error_message = None
        if email is not None and nick is not None and password is not None:
            try:
                is_user_exist, error_message = self.is_email_or_nick_exist(email=email, nick=nick)
                if not is_user_exist:
                    hashed_password = functions.generate_hashed_data(data=password)
                    new_user = User(email=email, nick=nick, password=hashed_password)
                    new_api_user_security = APIUserSecurity(user_email=email)
                    database.session.add(new_user)
                    database.session.commit()
                    database.session.add(new_api_user_security)
                    database.session.commit()
                    is_registered = True

            except Exception as e:
                error_message = 'registration error'
                error()
            return jsonify(is_registered=is_registered, error_message=error_message)

    def star_topic(self) -> jsonify:
        pass

    def up_vote_star(self) -> jsonify:
        pass

    def down_vote_star(self) -> jsonify:
        pass


class TopicHandler(object):

    def get_topic_by_id(self, topic_id=None) -> (bool, Topic):
        is_exist = False
        topic = None
        try:
            topic = Topic.query.filter_by(id=topic_id).first()
            if topic is not None:
                is_exist = True

        except Exception as e:
            error()

        return is_exist, topic

    def insert_topic(self, title=None, content=None, published_by=None):
        error_message = None
        is_error = False
        try:
            topic = Topic(title=title, content=content, published_by=published_by)
            database.session.add(topic)
            database.session.commit()
        except Exception as e:
            is_error = True
            error_message = 'some error is occured when inserting the topic'
            error()
            print(e)

        return jsonify(is_error=is_error, error_message=error_message)

    def update_topic(self, topic_id=None, title=None, content=None, updated_by=None):
        is_error = False
        error_message = None

        try:
            is_exist, topic = self.get_topic_by_id(topic_id)
            if is_exist:
                topic.title = title
                topic.content = content
                topic.updated_by = updated_by
                database.session.commit()
            else:
                is_error = True
                error_message = 'topic does not exist'

        except Exception as e:
            is_error = True
            error_message = 'some error is occered when updating the topic'
            error()

        return jsonify(is_error=is_error, error_message=error_message)

    def delete_topic(self, topic_id=None, delete_reason=None, deleted_by=None):
        pass


class AnswerHandler(object):

    def __init__(self):
        pass

    def __is_answer_exist(self, answer_id=None):
        pass

    def insert_answer(self, title=None, content=None, published_by=None):
        pass

    def update_answet(self, answer_id=None, title=None, content=None, updated_by=None):
        pass

    def delete_answer(self, answer_id, delete_reason=None, deleted_by=None):
        pass

