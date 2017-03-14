from flask import jsonify
from social import database
from social.model import Topic, User, Answer
import social.functions as functions

class TopicHandler(object):

    def api_hot_serializer(self, topic: Topic) -> dict:
        try:
            answer_length = len(Answer.query.filter_by(topic_id = topic.id).all())
            print(answer_length)
        except Exception as e:
            functions.error()
            print(e)

        return dict(
            id=topic.id,
            title=topic.title,
            published_by=topic.published_by,
            published_at=topic.published_at,
            vote=topic.vote,
            answer=answer_length
        )

    def get_topic_by_id(self, topic_id) -> (bool, Topic):
        is_exist = False
        topic = None
        try:
            topic = Topic.query.filter_by(id=topic_id).first()
            if topic is not None:
                is_exist = True

        except Exception as e:
            functions.error()

        return is_exist, topic

    def insert_topic(self, title, content, user: User) -> jsonify:
        error_message = None
        is_ok = False
        try:
            topic = Topic(title=title, content=content, published_by=user.id)
            database.session.add(topic)
            database.session.commit()
            is_ok = True
        except Exception as e:
            error_message = 'some error is occured when inserting the topic'
            functions.error()
            print(e)

        return jsonify(is_ok=is_ok, error_message=error_message)

    def update_topic(self, topic_id, title, content, user: User) -> jsonify:
        is_ok = False
        error_message = None

        try:
            is_exist, topic = self.get_topic_by_id(topic_id)
            if is_exist and topic.published_by == user.id:
                topic.title = title
                topic.content = content
                #topic.updated_by = user.id
                database.session.commit()
                is_ok = True

            else:
                error_message = 'topic update request is rejected'

        except Exception as e:
            is_ok = True
            error_message = 'some error is occered when updating the topic'
            functions.error()

        return jsonify(is_ok=is_ok, error_message=error_message)

    def delete_topic(self, topic_id, delete_reason, deleted_by):
        pass

    def get_hot_topic(self) -> jsonify:
        is_ok = False
        topics = []
        try:
            topics = Topic.query.all()
            topics = [self.api_hot_serializer(topic) for topic in topics]
            sorted(topics, key= lambda topic: topic['vote'])
            is_ok = True
        except Exception as e:
            functions.error()
            print(e)
        return jsonify(
            is_ok=is_ok,
            topics=topics
        )
