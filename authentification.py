import pyrebase
from config import config

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def _register_user(content):
    username = content.controls[0].content.controls[1].controls[1].content.value
    user_email = content.controls[0].content.controls[2].controls[1].content.value
    user_password = content.controls[0].content.controls[3].controls[1].content.value
    try:
        auth.create_user_with_email_and_password(user_email, user_password)
        print("USER Registered")
    except Exception as e:
        print(e)


def _login_user(landing_anim):
    # print("ok")
    user_email = (
        landing_anim.content.controls[0].content.controls[1].controls[1].content.value
    )

    user_password = (
        landing_anim.content.controls[0].content.controls[2].controls[1].content.value
    )
    try:
        user = auth.sign_in_with_email_and_password(user_email, user_password)
        info = auth.get_account_info(user["idToken"])
        print(info)
    except:
        print("Wrong email or password")
