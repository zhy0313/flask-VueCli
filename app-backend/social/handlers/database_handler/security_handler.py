from social.model import APIClientSecurity
import social.functions as functions


class APIClientSecurityHandler:

    def is_client_exist(self, client_key) -> bool:
        is_exist = False
        try:
            client = APIClientSecurity.query.filter_by(client_key=client_key, status=True).first()
            if client is not None:
                is_exist = True

        except Exception as e:
            functions.error()

        return is_exist
