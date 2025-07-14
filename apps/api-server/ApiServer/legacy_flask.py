from flask import Flask

legacy_app = Flask(__name__)

@legacy_app.route("/legacy")
def legacy():
    return {"message": "Legacy Flask endpoint"}