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
def get_database_results():
    """
    Accept GET request with search string
    Query database for documents matching search string
    Render list of matching database documents with Jinja2 template
    :return: HTML-formatted documents
    """
    documents_list = []
    searchText = request.args.get('text')
    if searchText is str or not searchText.isspace():
        documents_list = business_layer.BusinessLayer().search_by_default(searchText)
    return render_template('results.html', documents_list=documents_list)


@app.route('/comment', methods=['POST'])
def update_comment():
    """
    Accept a POST request with comment text and object_id
    Update specified document with comment
    :return: TBD
    """
    commentText = request.args.get('text')
    object_id = request.args.get('object_id')
    business_layer.BusinessLayer().add_comment(object_id, commentText)
