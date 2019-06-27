from pprint import pprint

from app import app
from app.forms import AnnouncementForm
from flask import render_template, redirect
from influxdb import InfluxDBClient

client = InfluxDBClient(host='db', port=8086, username='root', password='root', database='test')


@app.route('/')
@app.route('/index')
def index():
	return redirect('/event')


@app.route('/event', methods=['GET', 'POST'])
def add_event():
	form = AnnouncementForm()
	if form.validate_on_submit():
		json_body = [
			{
				"measurement": "events",
				"fields": {
					"title": form.title.data,
					"description": form.description.data,
					"url": "https://google.co.uk"
				}
			}
		]
		client.write_points(points=json_body)

		pprint(json_body)
		return redirect('/event')
	# return str(form.title + '\n' + form.description)
	return render_template('event.html', title='New Event', form=form)
