from flask import Flask, request
from flask import render_template
from flask import json
import business_layer
import urlparse

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
    documents = business_layer.BusinessLayer().get_results(request.args)
    return render_template('titles.html', documents=documents)


@app.route('/details', methods=['GET'])
def get_document_details():
    document = business_layer.BusinessLayer().get_details(request.args.get('id'))
    return render_template('details.html', details=document)


@app.route('/comment', methods=['POST'])
def update_comment():
    commentText = request.args.get('text')
    object_id = request.args.get('object_id')
    return business_layer.BusinessLayer().add_comment(object_id, commentText)

