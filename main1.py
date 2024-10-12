from flask import Flask
from datetime import datetime
app=Flask(__name__)

@app.route('/')
def currentTime():
     return f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'

if __name__ == '__main__':
    app.run()