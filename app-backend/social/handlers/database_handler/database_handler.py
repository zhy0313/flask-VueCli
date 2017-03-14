from flask import jsonify
from social.handlers.database_handler import answer_handler
from social.handlers.database_handler import topic_handler
from social.handlers.database_handler import user_handler
from social.handlers.database_handler import security_handler
import social.functions as functions

class DatabaseHandler(object):

    def __init__(self):
        self.answer_handler = answer_handler.AnswerHandler()
        self.topic_handler = topic_handler.TopicHandler()
        self.api_security_handler = security_handler.APIClientSecurityHandler()
        self.user_handler = user_handler.UserHandler()

    def sign_on(self, email, password, client_key) -> jsonify:
        try:
            if self.api_security_handler.is_client_exist(client_key=client_key):
                return self.user_handler.sign_on(email=email, password=password)

            raise Exception('sign_on exception')

        except Exception as e:
            functions.error()
            return jsonify(
                error_message='access denied',
                sign_on=False,
                access_token=None
            )

    def sign_in(self, email, password, nick, client_key) -> jsonify:
        try:
            if self.api_security_handler.is_client_exist(client_key=client_key):
                return self.user_handler.sign_in(email=email, password=password, nick=nick)

            raise Exception('sig_in error')

        except Exception as e:
            functions.error()
            return jsonify(
                error_message='access denied',
                sign_on=False,
                access_token=None
            )

    def hot(self, client_key, access_token) -> jsonify:
        try:
            is_client_exist = self.api_security_handler.is_client_exist(client_key=client_key)
            is_topic_exist, user = self.user_handler.get_user_email_by_access_token(access_token=access_token)
            if is_client_exist and is_topic_exist:
                return self.topic_handler.get_hot_topic()

        except Exception as e:
            functions.error()
            print(e)
            return jsonify(
                error_message='access denied'
            )
    def add_new_topic(self, title, content, client_key, access_token) -> jsonify:
        try:
            if self.api_security_handler.is_client_exist(client_key=client_key):
                is_exist, user = self.user_handler.get_user_email_by_access_token(access_token=access_token)
                if is_exist:
                    return self.topic_handler.insert_topic(title=title, content=content, user=user)
            raise Exception('add_new_topic, accessing error')

        except Exception as e:
            functions.error()
            return jsonify(
                error_message='access denied',
                is_topic_added=False,
            )

    def update_topic(self, topic_id, title, content, client_key, access_token) -> jsonify:
        try:
            if self.api_security_handler.is_client_exist(client_key=client_key):
                is_exist, user = self.user_handler.get_user_email_by_access_token(access_token=access_token)
                if is_exist:
                    return self.topic_handler.update_topic(topic_id=topic_id, title=title, content=content, user=user)
            raise Exception('add_new_topic, accessing error')

        except Exception as e:
            functions.error()
            return jsonify(
                error_message='access denied',
                is_ok=False,
            )

    def start_topic(self, topic_id, client_key, access_token) -> jsonify:
        try:
            if self.api_security_handler.is_client_exist(client_key=client_key):
                is_user_exist, user = self.user_handler.get_user_email_by_access_token(access_token=access_token)
                is_topic_exist, topic = self.topic_handler.get_topic_by_id(topic_id=topic_id)
                if is_user_exist and is_topic_exist:
                    return self.user_handler.star_topic(user=user, topic=topic)

            raise Exception('user or topic is not found')

        except Exception as e:
            functions.error()
            return jsonify(
                error_message='access denied',
                is_ok = False
            )

        except Exception as e:
            functions.error()

    def vote_topic(self, topic_id, vote, client_key, access_token) -> jsonify:
        try:
            if self.api_security_handler.is_client_exist(client_key=client_key):
                is_user_exist, user = self.user_handler.get_user_email_by_access_token(access_token=access_token)
                is_topic_exist, topic = self.topic_handler.get_topic_by_id(topic_id=topic_id)
                if is_user_exist and is_topic_exist:
                    return self.user_handler.vote_topic(user=user, topic=topic, vote=vote)

                raise Exception('user or topic is not found')

        except Exception as e:
            print(e)
            functions.error()
            return jsonify(
                is_ok=False,
                error_message='access denied'
            )

    def vote_answer(self, answer_id, vote, client_key, access_token) -> jsonify:
        try:
            if self.api_security_handler.is_client_exist(client_key=client_key):
                is_user_exist, user = self.user_handler.get_user_email_by_access_token(access_token=access_token)
                is_answer_exist, answer = self.answer_handler.get_answer_by_id(answer_id=answer_id)
                if is_user_exist and is_answer_exist:
                    return self.user_handler.vote_answer(user=user, answer=answer, vote=vote)

                raise Exception('user or topic is not found')

        except Exception as e:
            print(e)
            functions.error()
            return jsonify(
                is_ok=False,
                error_message='access denied'
            )

