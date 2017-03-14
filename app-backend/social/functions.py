from hashlib import md5, sha256
import time
import sys
import os


def generate_hashed_data(data=None) -> str:
    try:
        password_encoded = data.encode('utf-8')
        password_md5 = md5(password_encoded).digest()
        password_sha256 = sha256(password_md5).hexdigest()
        return password_sha256
    except Exception as e:
        print(e)


def generate_access_token(email=None) -> str:
    str_time = str(time.time())
    hashed_email = generate_hashed_data(data=email + str_time)
    hashed_time = generate_hashed_data(data= str_time)
    return '{}{}'.format(hashed_email, hashed_time)


def error():
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)