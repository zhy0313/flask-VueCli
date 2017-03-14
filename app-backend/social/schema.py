from social import marshmallow
from social.model import  Topic

class TopicPreviewSchema(marshmallow.ModelSchema):
    class Meta:
        model = Topic
        exclude = ['content']

