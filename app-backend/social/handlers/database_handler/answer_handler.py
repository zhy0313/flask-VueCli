from flask import jsonify
from social import database
from social.model import Answer
from social.model import Topic
import social.functions as functions


class AnswerHandler(object):

    def __init__(self):
        pass

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


    def insert_answer(self, title, content, published_by):
        pass

    def update_answet(self, answer_id, title, content, updated_by):
        pass

    def delete_answer(self, answer_id, delete_reason, deleted_by):
        pass
