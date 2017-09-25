from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>

<html>
  <head>
    <style>
      form {{
          background-color: #eee;
          padding: 20px;
          margin: 0 auto;
          width: 540px;
          font: 16px sans-serif;
          border-radius: 10px;
      }}

      textarea {{
          margin: 10px 0;
          width: 540px;
          height: 120px;
      }}
    </style>
  </head>
  <body>
    <form action="/" method='post'>
      <label>Rotate by:</label>
      <input type="text" name="rot"/>
      <textarea type="textarea" name="text">{0}</textarea>
      <input type="submit" />
  </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    message = request.form['text']
    rotate = request.form['rot']
    new_mess = rotate_string(message, int(rotate))
    return '<h1>' + form.format(new_mess) + '</h1>'
    


@app.route("/")
def index():
    return form.format("")

app.run()