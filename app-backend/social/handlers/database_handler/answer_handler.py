from flask import jsonify
from social import database
from social.model import Answer
from social.model import Topic
from social.model import User
import social.functions as functions


class AnswerHandler(object):

    def __init__(self):
        pass

    def api_answer_serializer(self, answer: Answer):
        try:
            user = User.query.filter_by(id=answer.published_by).first()
        except Exception as e:
            functions.error()
            print(e)
        return dict(
            id=answer.id,
            content=answer.content,
            submitted_by=user.nick,
            submitted_at=answer.published_at,
            vote = answer.vote,
            is_topic=False
        )

    def get_answer_by_id(self, answer_id) -> (bool, Answer):
        is_exist, answer = False, None
        try:
            answer = Answer.query.filter_by(id=answer_id).first()
            if answer is not None:
                is_exist = True
        except Exception as e:
            functions.error()
            print(e)
        return is_exist, answer

    def insert_answer(self, content, topic: Topic,  user: User):
        is_ok, error_message = False, None
        try:
            new_answer = Answer(topic_id=topic.id, content=content, published_by=user.id)
            database.session.add(new_answer)
            database.session.commit()
            is_ok = True
        except Exception as e:
            print(e)
            functions.error()
            error_message = 'access denied'
        return jsonify(
            is_ok=is_ok,
            error_message=error_message,
            topic_id=topic.id
        )

    def update_answet(self, answer_id, title, content, updated_by):
        pass

    def delete_answer(self, answer_id, delete_reason, deleted_by):
        pass

    def get_topic_answers(self, topic:Topic) -> list:

        answers = []
        try:
            answers = Answer.query.filter_by(topic_id=topic.id).all()
            answers = [self.api_answer_serializer(answer) for answer in answers]
            sorted(answers, key= lambda answer: answer['vote'])
            is_ok = True
        except Exception as e:
            functions.error()
            print(e)
            error_message = 'answers cannot be fetched'

        return answers