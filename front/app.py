from flask import Flask, request, render_template, flash
import requests
import json
from forms import LoginForm, app
from flask_bootstrap import Bootstrap
Bootstrap(app)

@app.route("/x")
def hello_world():
    url = 'http://localhost:8080/graphql'
    r = requests.post(url, json={'query': query})
    print(r.text)
    x = r.json()['data']['queryuser'][0]['password']

    return f"<p>{x}</p>"

@app.route("/", methods=["GET", "POST"])
def login():
  form = LoginForm()

  if request.method == 'POST':
    query = '''query {
  queryuser(filter: {email: {allofterms: "correo@correo.com"}}) {
		password
  }
}'''.replace("emailx", form.email.data) 

    url = 'http://localhost:8080/graphql'
    r = requests.post(url, json={'query': query})
    print(f"Holaaaa {query}")

    pass_bd = r.json()['data']['queryuser'][0]['password']

    if pass_bd == form.password.data:
      flash("Mu bien")
    else:
      flash("Password incorrect, please try again.")
  
  return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5010, debug=True)