from flask import Flask, render_template, request, flash, redirect
from flask_scss import Scss
from flask_mail import Mail, Message
import os

app = Flask(__name__, static_url_path="", static_folder="static")
Scss(app, static_dir='static', asset_dir='assets')

# Gettin get environment variables
gmail_user = os.getenv('GMAIL_USERNAME')
gmail_pass = os.getenv('GMAIL_PASSWORD')

# Configuring values
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME=gmail_user,
    MAIL_PASSWORD=gmail_pass,
)

key = 'abadfgasgasdgadsgdfgasgasdgfasdra123afgsdafasfsadga2a3rg'
app.config['SECRET_KEY'] = key
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = gmail_user
app.config['MAIL_PASSWORD'] = gmail_pass
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# Instantiate Mail
mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['get'])
def contact():
    return render_template('contact.html')


@app.route('/contact', methods=['post'])
def contact_post():
    # Getting data from the form
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    if not name:
        flash('Name is required!')
    elif not email:
        flash('Email is required!')
    elif not subject:
        flash('Subject is required!')
    elif not message:
        flash('Message is required!')
    else:
        try:
            print('Preparing email')
            print(f'User: {gmail_user}')
            print(f'Pass: {gmail_pass}')
            print(f'name: {name}')
            print(f'email: {email}')
            print(f'subject: {subject}')
            print(f'message: {message}')

            # Sending message to gmail
            msg = Message(subject=subject,
                          sender=(name, email),
                          recipients=gmail_user,
                          body=message)
            mail.send_message(msg)
            print('Email sent!')
        except Exception as e:
            print(f'Exception: {e}')

    return redirect('contact')


@app.route('/portfolio-details1')
def portfolio_details1():
    return render_template('portfolio-details1.html')


@app.route('/portfolio-details2')
def portfolio_details2():
    return render_template('portfolio-details2.html')


@app.route('/portfolio-details3')
def portfolio_details3():
    return render_template('portfolio-details3.html')


@app.route('/portfolio-details4')
def portfolio_details4():
    return render_template('portfolio-details4.html')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
