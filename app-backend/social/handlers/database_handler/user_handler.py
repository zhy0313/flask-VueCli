from flask import jsonify
from social import database
from social.model import User
from social.model import APIUserSecurity
from social.model import UserStar
from social.model import UserTopicVote
from social.model import UserAnswerVote
from social.model import Topic
from social.model import Answer
import social.functions as functions


class UserHandler(object):

    def get_user_email_by_access_token(self, access_token) -> (bool, User):
        is_exist, user_email, user = False, None, None
        try:
            api_user_security = APIUserSecurity.query.filter_by(access_token=access_token).first()
            if api_user_security is not None:
                is_exist = True
                user_email = api_user_security.user_email
                user = User.query.filter_by(email=user_email).first()
        except Exception as e:
            functions.error()

        return is_exist, user

    def get_user_by_nick(self, nick) -> (bool, User):
        is_exist = False
        user = None

        try:
            user = User.query.filter_by(nick=nick).first()
            if user is not None:
                is_exist = True
        except Exception as e:
            functions.error()
        return is_exist, user

    def get_user_by_email(self, email) -> (bool, User):
        is_exist = False
        user = None
        try:
            user = User.query.filter_by(email=email).first()
            if user is not None:
                is_exist = True
        except Exception as e:
            functions.error()

        return is_exist, user

    def get_user_by_id(self, user_id) -> User:
        user = None
        try:
            user = User.query.filter_by(id=user_id).first()
        except Exception as e:
            functions.error()
        return user

    def is_email_or_nick_exist(self, email, nick) -> (bool, str):
        is_exist = True
        error_message = None

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
            functions.error()

        return is_exist, error_message

    def sign_on(self, email, password) -> jsonify:
        is_ok = False
        error_message = None
        access_token = None

        try:
            hashed_password = functions.generate_hashed_data(data=password)
            user = User.query.filter_by(email=email, password=hashed_password).first()
            if user is not None:
                api_user_security = APIUserSecurity.query.filter_by(user_email=email).first()
                if api_user_security is not None:
                    access_token = functions.generate_access_token(email=email)
                    api_user_security.access_token = access_token
                    database.session.commit()
                    is_ok = True
            else:
                error_message = 'user is not found'

        except Exception as e:
            functions.error()

        return jsonify(is_ok=is_ok, error_message=error_message, access_token=access_token)

    def sign_in(self, email, nick, password) -> jsonify:
        is_ok = False
        error_message = None

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
                is_ok = True

        except Exception as e:
            error_message = 'registration error'
            functions.error()

        return jsonify(is_ok=is_ok, error_message=error_message)

    def star_topic(self, user: User, topic: Topic) -> jsonify:
        is_ok, error_message = False, None
        try:
            was_stared = UserStar.query.filter_by(user_id=user.id, topic_id=topic.id).first()
            if was_stared is not None:
                was_stared.status = not was_stared.status
            else:
                star = UserStar(user_id=user.id, topic_id=topic.id, status=True)
                database.session.add(star)
            database.session.commit()
            is_ok = True
        except Exception as e:
            print(e)
            functions.error()
            error_message = 'access denied'

        return jsonify(
            is_ok=is_ok,
            error_message=error_message
        )

    def vote_topic(self, user: User, topic: Topic, vote) -> jsonify:
        is_ok, error_message = False, None
        topic_id = topic.id
        if vote == 'UP':
            vote = 1
        elif vote == 'DOWN':
            vote = -1
        else:
            raise Exception('vote is not UP or DOWN')
        
        try:
            if user.id == topic.published_by:
                raise Exception('Cannot vote own topic')

            was_voted = UserTopicVote.query.filter_by(user_id=user.id, topic_id=topic.id).first()
            if was_voted is not None:
                if was_voted.vote != vote:
                    was_voted.vote = vote
                    if topic.vote + 1 == 0:
                        vote += 1
                    elif topic.vote - 1 == 0:
                        vote -= 1
                    topic.vote += vote
                else:
                    if was_voted.vote == -1:
                        topic.vote += 1
                    elif was_voted.vote == 1:
                        topic.vote -= 1
                    was_voted.vote = 0
                is_ok = True

            else:
                topic_vote = UserTopicVote(user_id=user.id, topic_id=topic.id, vote=vote)
                database.session.add(topic_vote)
                topic.vote += vote
                is_ok = True

            database.session.commit()
        except Exception as e:
            functions.error()
            error_message = str(e)

        return jsonify(
            topic_id=topic_id,
            is_ok=is_ok,
            error_message=error_message
        )

    def vote_answer(self, user: User, answer: Answer, vote) -> jsonify:
        is_ok, error_message = False, None
        if vote == 'UP':
            vote = 1
        elif vote == 'DOWN':
            vote = -1
        else:
            raise Exception('vote is not UP or DOWN')

        try:
            was_voted = UserAnswerVote.query.filter_by(user_id=user.id, topic_id=answer.id).first()
            if was_voted is not None:
                if was_voted.vote != vote:
                    was_voted.vote = vote
                    answer.vote += vote
            else:
                answer_vote = UserTopicVote(user_id=user.id, topic_id=answer.id, vote=vote)
                database.session.add(answer_vote)
                answer.vote += vote

            database.session.commit()
            is_ok = True
        except Exception as e:
            functions.error()
            error_message = 'access denied'

        return jsonify(
            is_ok=is_ok,
            error_message=error_message
        )
