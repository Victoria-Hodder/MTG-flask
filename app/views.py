from flask import render_template, Flask
from app import app
import requests

menu = {
	'links' : [
		{
			'url': '/',
			'text' : 'Link1'
		},
		{
			'url': '/',
			'text' : 'Link2'
		},
		{
			'url': '/',
			'text' : 'Link3'
		}

	]
}

@app.route('/')
@app.route('/index')
def index():
	content = {
		"title" : "Homepage"
	}
	return render_template('index.html', content=content, nav=menu)

@app.route('/demo')
def demo():
	content = {
		"title" : "Demo Page"
	}
	return render_template('page.html', content=content, nav=menu)