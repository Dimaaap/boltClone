from random import randint

from twilio.base.exceptions import TwilioRestException

from ..data_storage import DataStorage

data_storage = DataStorage()

class SmsMessageService:

    def send_sms_message_service(self, sms_client, request, phone_number):
        generated_sms_code = self.generate_sms_confirmation_code_service()
        request.session["otp_code"] = generated_sms_code
        self.form_sms_message_service(sms_client, generated_sms_code, phone_number)

    @staticmethod
    def generate_sms_confirmation_code_service():
        code = randint(data_storage.SMALLEST_SMS_CODE_VALUE, data_storage.HIGHEST_SMS_CODE_VALUE)
        return code

    @staticmethod
    def form_sms_message_service(client, generated_sms_code, user_phone_number):
        try:
            message = client.messages.create(
                body=f"\nЛаскаво просимо вас у Bolt Driver\n"
                     f"Ваш код для реєстрації - {str(generated_sms_code)}\n"
                     f"Нікому не повідомляйте цей код",
                from_=data_storage.AUTH_TOKEN_PHONE_NUMBER,
                to=str(user_phone_number)
            )
        except TwilioRestException:
            print("exception")