import datetime

import jwt

from django.conf import settings


class TokenService:
    def generate_token(self, session_id):
        payload = {
            "session_id": session_id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=600)
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        return token

    def check_if_token_verified(self, request, verification_code):
        driver = self.verify_token(verification_code)
        if isinstance(driver, str):
            return False
        request.session["verification_code"] = verification_code
        return True

    @staticmethod
    def verify_token(token, secret_key=settings.SECRET_KEY):
        print("In user verify_token")
        try:
            decoded_payload = jwt.decode(token, secret_key, algorithms=["HS256"])
            return bool(decoded_payload)
        except jwt.ExpiredSignatureError:
            return "Token has expired"
        except jwt.InvalidTokenError:
            return "Invalid token"