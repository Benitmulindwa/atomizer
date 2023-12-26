import pyrebase
from config import config
import json


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


def _register_user(content):
    username = content.controls[0].content.controls[1].controls[1].content.value
    user_email = content.controls[0].content.controls[2].controls[1].content.value
    user_password = content.controls[0].content.controls[3].controls[1].content.value
    try:
        if len(user_password) >= 7 and username != None:
            auth.create_user_with_email_and_password(user_email, user_password)
            auth.sign_in_with_email_and_password(user_email, user_password)
            return True
        else:
            content.controls[0].content.controls[3].controls[
                1
            ].content.error_text = "The password must have at least 7 characters"
            content.controls[0].content.update()
    except Exception as e:
        error_ = json.loads("{" + "".join(str(e).splitlines()[1:]))

        content.controls[0].content.controls[2].controls[1].content.error_text = error_[
            "error"
        ]["message"].lower()
        content.controls[0].content.update()


def _login_user(login_form):
    user_email = (
        login_form.content.controls[0].content.controls[1].controls[1].content.value
    )

    user_password = (
        login_form.content.controls[0].content.controls[2].controls[1].content.value
    )
    try:
        user = auth.sign_in_with_email_and_password(user_email, user_password)
        info = auth.get_account_info(user["idToken"])
        print(info)
        return True
    except:
        login_form.content.controls[0].content.controls[1].controls[
            1
        ].content.error_text = "Wrong email or password"
        login_form.content.controls[0].content.controls[2].controls[
            1
        ].content.error_text = "Wrong email or password"
        login_form.content.controls[0].update()
