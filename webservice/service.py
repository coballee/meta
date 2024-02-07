import uuid

from flask import Flask

from webservice.service import meta_blueprint

app = Flask(__name__, template_folder='templates', static_folder='templates/assets')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = uuid.uuid4().hex
app.debug = True

app.register_blueprint(meta_blueprint, url_prefix='')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=54321, debug=True)
