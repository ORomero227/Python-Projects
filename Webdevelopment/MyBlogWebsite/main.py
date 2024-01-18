import requests
import smtplib
import os
from flask import Flask, render_template, request

MY_EMAIL = "oscalito992@gmail.com"
PASSWORD = os.environ.get("GmailAppPassword")

# Retrieve the data
response = requests.get("https://api.npoint.io/78099916990f059587bc")
response.raise_for_status()
all_posts = response.json()

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template('index.html', all_posts=all_posts)


@app.route("/about")
def about_page():
    return render_template('about.html')


@app.route("/contact", methods=['GET', 'POST'])
def contact_page():
    if request.method == "POST":

        person_name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:New Message from the Blog\n\n"
                    f"Name: {person_name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")
            connection.close()
        return render_template('contact.html', msg_sent=True)
    else:
        return render_template('contact.html', msg_sent=False)


@app.route("/post/<post_title>")
def post_info(post_title):
    requested_post = None
    for post in all_posts:
        if post['title'] == post_title:
            requested_post = post
    return render_template('post.html', post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
