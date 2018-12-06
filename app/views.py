from flask import render_template, Flask, session, redirect, url_for, escape, request, abort
from app import app

import requests

info = {
	'title': 'This is the website title',
	'description' : 'This is the description of the website',
	'logo' : 'https://res.cloudinary.com/yuduyu/image/upload/v1543961049/yuduyu_logo_black.png',
	'social': {
		'twitter': 'twitter',
		'facebook' : 'facebook',
		'instagram' : 'instagramstar'
	}
}
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
		'settings': [
		{
			'type' : 'jumbotron',
			'title' : 'Some Amazing Title',
			'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
			'imgUrl' : 'https://dynaimage.cdn.cnn.com/cnn/q_auto,w_1100,c_fill,g_auto,h_619,ar_16:9/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F171219210515-i12-010575.jpg',
			'linkUrl' : 'http://www.google.com',
			'linkText' : 'Click Me'
		},
		{
			'type' : 'imageText',
			'title' : 'Some Amazing Title',
			'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
			'imgUrl' : 'https://dynaimage.cdn.cnn.com/cnn/q_auto,w_1100,c_fill,g_auto,h_619,ar_16:9/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F171219210515-i12-010575.jpg',
			'linkUrl' : 'http://www.google.com',
			'linkText' : 'Click Me'
		},
		{
			'type' : 'carousel',
			'title' : 'Some Amazing Title',
			'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
			'blocks' : [
				{
					'title' : 'Some Amazing Title',
					'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
					'imgUrl' : 'https://dynaimage.cdn.cnn.com/cnn/q_auto,w_1100,c_fill,g_auto,h_619,ar_16:9/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F171219210515-i12-010575.jpg',
					'linkUrl' : 'http://www.google.com',
					'linkText' : 'Click Me'
				},
				{
					'title' : 'Some Amazing Title',
					'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
					'imgUrl' : 'https://dynaimage.cdn.cnn.com/cnn/q_auto,w_1100,c_fill,g_auto,h_619,ar_16:9/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F171219210515-i12-010575.jpg',
					'linkUrl' : 'http://www.google.com',
					'linkText' : 'Click Me'
				},
				{
					'title' : 'Some Amazing Title',
					'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
					'imgUrl' : 'https://dynaimage.cdn.cnn.com/cnn/q_auto,w_1100,c_fill,g_auto,h_619,ar_16:9/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F171219210515-i12-010575.jpg',
					'linkUrl' : 'http://www.google.com',
					'linkText' : 'Click Me'
				},
				{
					'title' : 'Some Amazing Title',
					'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
					'imgUrl' : 'https://dynaimage.cdn.cnn.com/cnn/q_auto,w_1100,c_fill,g_auto,h_619,ar_16:9/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F171219210515-i12-010575.jpg',
					'linkUrl' : 'http://www.google.com',
					'linkText' : 'Click Me'
				}
			]
		},
		{
			'type' : 'textImage',
			'title' : 'Some Amazing Title',
			'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
			'imgUrl' : 'https://dynaimage.cdn.cnn.com/cnn/q_auto,w_1100,c_fill,g_auto,h_619,ar_16:9/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F171219210515-i12-010575.jpg',
			'linkUrl' : 'http://www.google.com',
			'linkText' : 'Click Me'
		},
		{
			'type' : 'infoBlocks',
			'title' : 'Some Amazing Title',
			'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
			'blocks' : [
				{
					'title' : 'Some Amazing Title',
					'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
					'imgUrl' : 'https://dynaimage.cdn.cnn.com/cnn/q_auto,w_1100,c_fill,g_auto,h_619,ar_16:9/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F171219210515-i12-010575.jpg',
					'linkUrl' : 'http://www.google.com',
					'linkText' : 'Click Me'
				},
				{
					'title' : 'Some Amazing Title',
					'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
					'imgUrl' : 'https://dynaimage.cdn.cnn.com/cnn/q_auto,w_1100,c_fill,g_auto,h_619,ar_16:9/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F171219210515-i12-010575.jpg',
					'linkUrl' : 'http://www.google.com',
					'linkText' : 'Click Me'
				},
				{
					'title' : 'Some Amazing Title',
					'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
					'imgUrl' : 'https://dynaimage.cdn.cnn.com/cnn/q_auto,w_1100,c_fill,g_auto,h_619,ar_16:9/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F171219210515-i12-010575.jpg',
					'linkUrl' : 'http://www.google.com',
					'linkText' : 'Click Me'
				},
				{
					'title' : 'Some Amazing Title',
					'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
					'imgUrl' : 'https://dynaimage.cdn.cnn.com/cnn/q_auto,w_1100,c_fill,g_auto,h_619,ar_16:9/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F171219210515-i12-010575.jpg',
					'linkUrl' : 'http://www.google.com',
					'linkText' : 'Click Me'
				}
			]
		},
		{
			'type' : 'gallery',
			'title' : 'Some Amazing Title',
			'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
			'blocks' : [
				{
					'title' : 'Some Amazing Title',
					'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
					'imgUrl' : 'https://dynaimage.cdn.cnn.com/cnn/q_auto,w_1100,c_fill,g_auto,h_619,ar_16:9/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F171219210515-i12-010575.jpg',
					'linkUrl' : 'http://www.google.com',
					'linkText' : 'Click Me'
				},
				{
					'title' : 'Some Amazing Title',
					'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
					'imgUrl' : 'https://dynaimage.cdn.cnn.com/cnn/q_auto,w_1100,c_fill,g_auto,h_619,ar_16:9/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F171219210515-i12-010575.jpg',
					'linkUrl' : 'http://www.google.com',
					'linkText' : 'Click Me'
				},
				{
					'title' : 'Some Amazing Title',
					'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
					'imgUrl' : 'https://dynaimage.cdn.cnn.com/cnn/q_auto,w_1100,c_fill,g_auto,h_619,ar_16:9/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F171219210515-i12-010575.jpg',
					'linkUrl' : 'http://www.google.com',
					'linkText' : 'Click Me'
				},
				{
					'title' : 'Some Amazing Title',
					'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
					'imgUrl' : 'https://dynaimage.cdn.cnn.com/cnn/q_auto,w_1100,c_fill,g_auto,h_619,ar_16:9/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F171219210515-i12-010575.jpg',
					'linkUrl' : 'http://www.google.com',
					'linkText' : 'Click Me'
				},
				{
					'title' : 'Some Amazing Title',
					'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
					'imgUrl' : 'https://dynaimage.cdn.cnn.com/cnn/q_auto,w_1100,c_fill,g_auto,h_619,ar_16:9/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F171219210515-i12-010575.jpg',
					'linkUrl' : 'http://www.google.com',
					'linkText' : 'Click Me'
				},
				{
					'title' : 'Some Amazing Title',
					'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
					'imgUrl' : 'https://dynaimage.cdn.cnn.com/cnn/q_auto,w_1100,c_fill,g_auto,h_619,ar_16:9/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F171219210515-i12-010575.jpg',
					'linkUrl' : 'http://www.google.com',
					'linkText' : 'Click Me'
				},
				{
					'title' : 'Some Amazing Title',
					'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
					'imgUrl' : 'https://dynaimage.cdn.cnn.com/cnn/q_auto,w_1100,c_fill,g_auto,h_619,ar_16:9/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F171219210515-i12-010575.jpg',
					'linkUrl' : 'http://www.google.com',
					'linkText' : 'Click Me'
				},
				{
					'title' : 'Some Amazing Title',
					'text' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec venenatis velit. Cras vel lacus tellus. Cras non neque eu libero tincidunt pellentesque. In non lacus turpis. Aenean eu dignissim diam. Duis ligula nibh, euismod vehicula urna sit amet, ornare cursus nisi. Suspendisse potenti. Cras ipsum nisl, facilisis vel sagittis vel, lobortis eget massa. In tempus dignissim augue a lobortis. In quis turpis leo. Fusce dapibus mollis odio in fermentum. In id fringilla diam. Integer ultricies viverra ante vel varius. Nunc quam tellus, pulvinar eu dignissim sit amet, vehicula ut tortor. Nulla porttitor quam eu ante fringilla tincidunt.',
					'imgUrl' : 'https://dynaimage.cdn.cnn.com/cnn/q_auto,w_1100,c_fill,g_auto,h_619,ar_16:9/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F171219210515-i12-010575.jpg',
					'linkUrl' : 'http://www.google.com',
					'linkText' : 'Click Me'
				}
			]
		}

		]
	}
	return render_template('index.html', content=content, nav=menu, info=info)



@app.route('/demo')
def demo():
	content = {
		'settings': [
		
		]
	}
	return render_template('page.html', content=content, nav=menu, info=info)