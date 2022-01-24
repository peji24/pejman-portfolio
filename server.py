

from flask import Flask,render_template,request
import smtplib
import datetime


app=Flask(__name__)






OWN_EMAIL="pj.bidad@gmail.com"
OWN_PASSWORD="Zap.#MV~)$%7PZuS"

@app.route("/")
def home():
    current_year = datetime.datetime.now().year
    return render_template("index.html",year=current_year)


@app.route("/", methods=["GET","POST"])
def receive_data():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["message"])
        send_email(data["name"],data["email"],data["message"])
        return render_template("index.html", msg_sent=True)
    return render_template("index.html", msg_sent=False)


def send_email(name, email, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__=="__main__":
    app.run(debug=True)






