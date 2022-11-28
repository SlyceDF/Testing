from flask import Flask, render_template, request, redirect
import logging
import os

app = Flask(  # Create a flask app
  __name__,
  template_folder='frontend',  # Name of directory for template files
  static_folder='frontend'  # Name of directory for static files
)

#@app.route('/', methods=['GET', 'POST'])
#def index():
#  return render_template('index.html')

#@app.errorhandler(404)
#def page_not_found(e):
#return render_template('404.html'), 404

#@app.errorhandler(500)
#def server_error(e):
#return render_template('500.html'), 500
