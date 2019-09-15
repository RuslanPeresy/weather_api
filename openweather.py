from flask import Flask, render_template, redirect, url_for, flash
from forms import LocationForm
from get_forecast import get_forecast

app = Flask(__name__)
app.config['SECRET_KEY'] = '9e03341b9de4fbdaf994841caed8547e'

@app.route('/', methods=['GET', 'POST'])
def location():
	form = LocationForm()
	if form.validate_on_submit():
		cityname = form.cityname.data
		return redirect(url_for('forecast', cityname=cityname))

	return render_template('location.html', form=form)

@app.route('/forecast/<string:cityname>', methods=['GET'])
def forecast(cityname):
	current_weather = get_forecast(cityname=cityname, apikey='ec191befe6624ab05ccbd9825e0ee1d4')
	if current_weather['status']:
		flash(current_weather['desc'], 'success')
		return render_template('forecast.html', cityname=cityname, current_weather=current_weather)
	else:
		flash(current_weather['desc'], 'danger')
		return redirect(url_for('location'))

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')