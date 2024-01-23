from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from forms import CafeForm
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

# Exercise:
# Make the form write a new row into cafe-data.csv
# with   if form.validate_on_submit()


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', "a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe_name.data},{form.cafe_location.data},{form.opening_time.data},"
                           f"{form.closing_time.data},{form.coffee_rating.data},{form.wifi_rating.data},"
                           f"{form.power_availability.data}")
        return render_template("success.html")
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_cafes = []
        for row in csv_data:
            list_of_cafes.append(row)
        column_titles = [title for title in list_of_cafes[0]]
        list_of_cafes.remove(column_titles)
    return render_template('cafes.html', columns_titles=column_titles, all_cafes=list_of_cafes)


if __name__ == '__main__':
    app.run(debug=True)
