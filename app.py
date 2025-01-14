from flask import Flask

app = Flask(__name__)

#dummy api key
api_key = 'AKIAIOSFODNN7EXAMPLE'

@app.route('/')
def home():
    return "Welcome to the Simple Flask App for DefectDojo!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
