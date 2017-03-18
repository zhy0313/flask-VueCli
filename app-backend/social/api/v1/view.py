from social import app
from flask import jsonify, request
from social.handlers.database_handler import database_handler
import social.functions as functions

databaseHandler = database_handler.DatabaseHandler()

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials','true')
    return response


@app.route('/api/v1/login', methods=['POST'])
def sign_on():
    is_sign_on, error_message = False, None
    try:
        json = request.get_json(silent=True)
        email = json['email']
        password = json['password']
        client_key = json['client_key']

        if client_key == '':
            raise Exception('client refresh keys are null')

        elif email == '' or password == '':
            error_message = 'email or password is wrong'
        else:
            return databaseHandler.sign_on(email=email, password=password, client_key=client_key)

    except Exception as e:
        functions.error()
        error_message = 'access denied'

    return jsonify(
        error_message=error_message,
        is_sign_on=is_sign_on
    )


@app.route('/api/v1/register', methods=['POST'])
def sign_in():
    is_sign_in, error_message = False, None
    try:
        json = request.get_json(silent=True)
        email = json['email']
        password = json['password']
        client_key = json['client_key']
        nick = json['nick']

        if client_key == '':
            raise Exception('client refresh keys are null')

        elif email == '' or password == '' or nick == '':
             error_message='email, password or nick cannot be empty'
        else:
            return databaseHandler.sign_in(email=email, password=password, nick=nick, client_key=client_key)

    except Exception as e:
        functions.error()
        error_message = 'access denied'

    return jsonify(
        error_message=error_message,
        is_sign_in=is_sign_in
    )


@app.route('/api/v1/topic', methods=['POST', 'PUT'])
def topic():
    is_ok, error_message = False, None
    try:
        json = request.get_json(silent=True)
        title = json['title']
        content = json['content']
        client_key = json['client_key']
        access_token = json['access_token']

        if client_key == '' or access_token == '':
            raise Exception('client refresh keys are null')

        elif title == '' or content == '':
            error_message = 'title or content cannot be empty'

        else:
            if request.method == 'POST': # INSERT, POST METHOD
                return databaseHandler.add_new_topic(title=title, content=content, client_key=client_key, access_token=access_token)

            elif request.method == 'PUT': # UPDATE, PUT METHOD
                topic_id = json['topic_id']
                return databaseHandler.update_topic(topic_id=topic_id, title=title, content=content, client_key=client_key, access_token=access_token)

            else:
                raise Exception('topic add update method or parameter problem')
    except Exception as e:
        functions.error()
        error_message = 'access denied'

    return jsonify(
        is_ok=is_ok,
        error_message=error_message
    )


@app.route('/api/v1/star', methods=['POST'])
def star_topic():
    is_ok, error_message = False, None
    try:
        json = request.get_json(silent=True)
        client_key = json['client_key']
        refresh_key = json['refresh_key']
        access_token = json['access_token']
        topic_id = json['topic_id']
        if client_key == '' or refresh_key == '' or access_token == '':
            raise Exception('client_key, refresh_key or access_token cannot be null')
        else:
            return databaseHandler.start_topic(topic_id=topic_id, client_key=client_key, access_token=access_token)

    except Exception as e:
        functions.error()
        error_message = 'access denied'

    return jsonify(
        is_ok=is_ok,
        error_message=error_message
    )


@app.route('/api/v1/topic/vote', methods=['POST'])
def vote_topic():
    is_ok, error_message = False, None
    try:
        json = request.get_json(silent=True)
        client_key = json['client_key']
        access_token = json['access_token']
        topic_id = json['topic_id']
        vote = json['vote']

        if client_key == '' or access_token == '':
            raise Exception('client_key, refresh_key or access_token cannot be null')
        else:
            return databaseHandler.vote_topic(topic_id=topic_id, vote=vote, client_key=client_key, access_token=access_token)
    except Exception as e:
        functions.error()
        print(e)
        error_message = 'access denied'

    return jsonify(
        is_ok=is_ok,
        error_message=error_message
    )


@app.route('/api/v1/hot', methods=['POST'])
def hot():
    is_ok, error_message = False, None
    try:
        json = request.get_json(silent=True)
        client_key = json['client_key']
        access_token = json['access_token']
        if client_key == '' or access_token == '':
            error_message = 'client key or access token can not be empty'
            raise Exception(error_message)

        return databaseHandler.hot(client_key=client_key, access_token=access_token)
    except Exception as e:
        functions.error()
        print(e)
        error_message = 'access denied'
        return jsonify(
            error_message=error_message,
            is_ok=is_ok
        )

@app.route('/api/v1/topic/detail', methods=['POST'])
def view_topic():
    is_ok, error_message = False, None
    try:
        json = request.get_json(silent=True)
        client_key = json['client_key']
        access_token = json['access_token']
        topic_id = json['topic_id']
        if client_key == '' or access_token == '':
            error_message = 'client key or access token can not be empty'
            raise Exception(error_message)

        return databaseHandler.view_topic(topic_id=topic_id, client_key=client_key, access_token=access_token)

    except Exception as e:
        functions.error()
        print(e)
        return jsonify(
            error_message=error_message,
            is_ok=is_ok
        )


@app.route('/api/v1/answer', methods=['POST', 'PUT'])
def answer():
    is_ok, error_message = False, None
    try:
        json = request.get_json(silent=True)
        client_key = json['client_key']
        access_token = json['access_token']
        topic_id = json['topic_id']
        content = json['content']
        if client_key == '' or access_token == '':
            error_message = 'client key or access token can not be empty'
            raise Exception(error_message)

        if request.method == 'POST':
            return databaseHandler.add_new_answer(topic_id=topic_id, content=content, client_key=client_key, access_token=access_token)
        elif request.method == 'PUT':
            pass

    except Exception as e:
        functions.error()
        print(e)
        return jsonify(
            error_message=error_message,
            is_ok=is_ok
        )