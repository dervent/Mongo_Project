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
    documents = []
    searchText = request.args.get('text')
    # improve this check for blank strings or null values
    if searchText is str or not searchText.isspace():
        documents = business_layer.BusinessLayer().get_names_by_default(searchText)
    return render_template('results.html', documents=documents)


@app.route('/comment', methods=['POST'])
def update_comment():
    commentText = request.args.get('text')
    object_id = request.args.get('object_id')
    return business_layer.BusinessLayer().add_comment(object_id, commentText)

