from configparser import ConfigParser

config = ConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def get_login_url():
        url = config.get("common info","login_url")
        return url

    @staticmethod
    def get_Emai_id():
        email_id = config.get("common info","Email_Id")
        return email_id

    @staticmethod
    def get_password():
        password = config.get("common info","password")
        return password

    @staticmethod
    def get_customer_email_id():
        email_id = config.get("customer info","email_id")
        return email_id

    @staticmethod
    def get_customer_first_name():
        first_name = config.get("customer info","first_name")
        return first_name

    @staticmethod
    def get_customer_last_name():
        last_name = config.get("customer info","last_name")
        return last_name
