from flask import Flask
from apps.login import loginBlue
from apps.core import coreBlue

app = Flask(__name__)

app.register_blueprint(loginBlue, url_prefix='/login')  # 前缀
app.register_blueprint(coreBlue, url_prefix='/core')

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True, host='0.0.0.0')
