from flask import Flask

app = Flask('calc')

@app.route('/calc', methods = ['GET'])

def calc():
    return 'Do you think you are a coder?'

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port = 9696)
