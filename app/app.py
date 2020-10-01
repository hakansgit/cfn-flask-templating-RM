from flask import Flask
from flask.globals import request
from flask.json import jsonify
from flask.templating import render_template
# from invalidUsage import InvalidUsage
from romanConverter import RomanConvertor

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main_get():
    return render_template('index.html', not_valid=False, developer_name='Hakan')

@app.route('/', methods=['POST'])
def main_post():
    number_str = request.form['number']
    try:
        return render_template('result.html', number_decimal=number_str, number_roman=RomanConvertor.convert(number_str), developer_name='Hakan')
    except Exception as e:
        return render_template('index.html', not_valid=True, developer_name='Hakan')

# @app.errorhandler(InvalidUsage)
# def handle_invalid_usage(error):
#     response = jsonify(error.to_dict())
#     response.status_code = error.status_code
#     return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)