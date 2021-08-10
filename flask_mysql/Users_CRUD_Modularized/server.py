from flask import app
from flasp_app.controllers import users_controller

if __name__=="__main__":
    app.run(debug=True)