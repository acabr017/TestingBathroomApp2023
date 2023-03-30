from flask import Flask, url_for, redirect, session
from views import views
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")
app.secret_key = '714e1eb705c43b09a498eb4e22e1de32'

#oauth config
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='607824139544-0on2v47n2qs94u7dqr2rullncd0qt64n.apps.googleusercontent.com',
    client_secret='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',
    access_token_url='https://accounts.google.com/o/oauth2/token/',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs=('scope'=='openid profile email')
)

@app.route('/')
def hello_world():
    email = dict(session).get('email', None)
    return f'Hello, {email}!'

@app.route('/login')
def login():
    google = oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    # do something with the token and profile
    session['email'] = user_info['email']
    return redirect('/')

@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')

if __name__ == '__main__':
    app.run()