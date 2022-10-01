from distutils.log import debug
from flask import Flask

app = Flask(__name__)


# showing a get reuest, /hello is the endpoint .. running this to the endpoint will display Hello World
@app.get('/hello')
def get_hello():
    return 'Hello World!'

app.run(debug=True)