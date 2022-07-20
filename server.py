#how the web works
# browser makes request to server to ask for data on page
# communication with protocol http and https
#server has 3 files (html - content; css- styling -colours,fonts...; javascript - gives websites behaviour)
# python can be used to the server part - can write logic and rules that servers can act upon
#built our own server


#module python http server - allows create a server - but not secure

#USE FRAMEWORK - Flask - uses http server and the security are pre-built for us - micro framewrok - small but fast
#DJANGO FRAMEWORK --- REally really big

from flask import Flask, render_template, url_for, request, redirect  #render_templeate allows us to send html file
import csv

app = Flask(__name__)

"""
@app.route("/<username>/<int:post_id>")  #routes to pages
def hello_world(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)  # automatically trys to find folder template
    #return "<p>Hello, Pedro. This is our  server in Ptyhon!</p>"


@app.route("/about.html")  #routes to pages
def about():
    return render_template('about.html')  # automatically trys to find folder template


@app.route("/blog/2020/dogs")
def blog2():
    return "<p>this is my dog</p>"

#variable rules

#data transfer - from servers to browser
#MIME type - Multipurpose Internet Mail Extension - indicates natures and content of file type
"""

@app.route('/')
def my_home():
    return render_template('index.html')


#instead of the below - create one call to each page - lets do it dinamyc ---
"""
@app.route('/index.html')
def my_home2():
    return render_template('index.html')


@app.route("/about.html")
def about():
    return render_template('about.html')


@app.route("/works.html")
def works():
    return render_template('works.html')

@app.route("/work.html")
def work():
    return render_template('work.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')
"""
#super simple and easy to understand
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong... try again!'
