from flask import Flask

AI=Flask(__name__)

@AI.route('/wish')
def wish():
    return '<h1>good morning</h1>'


if __name__=='__main__':
    AI.run(debug=True)