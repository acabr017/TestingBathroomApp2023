from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
    #turn off debug=True when everything is finished
    app.run(debug=True)