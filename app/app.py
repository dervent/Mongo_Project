from flask import Flask, request
from flask import render_template
import business_layer

# Entry point for micro-service

app = Flask(__name__)


@app.route('/')
def show_homepage():
    """
    Render static resources when a new request is made to the home URL, http://127.0.0.1:5000/
    :return: application's homepage
    """
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def get_results():
    """
    Accept GET request with search string and selected filter and or sort options.
    Return list of matching titles in rendered template.
    :return:
    """
    documents = business_layer.BusinessLayer().get_results(request.args)
    return render_template('titles.html', documents=documents)


@app.route('/details', methods=['GET'])
def get_document_details():
    """
    Accept GET request with ObjectId.
    Return details of the matching document in rendered template.
    :return:
    """
    document = business_layer.BusinessLayer().get_details(request.args.get('id'))
    return render_template('details.html', details=document)


@app.route('/comment', methods=['POST'])
def update_comment():
    """
    Accept POST request with ObjectId
    :return: Return 201 or 500 response code to browser.
    """
    return business_layer.BusinessLayer().add_comment(request.form)
