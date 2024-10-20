from flask import Flask
from flask import request
app = Flask (__name__)
@app.route("/",methods =["Get"])
def mainHome():
        username = request.args.get('username')
        return f"<h2>Hello,{str(username)}</h2><br>Welcome to ypur personalized lab manual."
if __name__ == "__main__":
        app.run()