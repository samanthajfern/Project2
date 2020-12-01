from flask_wtf import FlaskForm
from pip._vendor import requests
from wtforms import StringField, RadioField, SelectField

from Project2_Flask import main_functions


class NewsForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    option = RadioField("Choice",
                        choices=[('review', 'Best Seller Reviews'),
                                 ('description', 'Book Description')])
    option2 = SelectField("Choice2",
                          choices=[('1', '1'), ('2', '2'),
                                    ('8', '8'), ('20', '20'), ('9', '9')])


def generateDataFromAPI():
    my_key_dict = main_functions.read_from_file("Project2_Flask/JSON_Files/api_key.json")
    my_key = my_key_dict["my_key"]
    url = "https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key=" + my_key
    response = requests.get(url).json()
    main_functions.save_to_file(response, "Project2_Flask/JSON_Files/response.json")
    bestselling_books = main_functions.read_from_file("Project2_Flask/JSON_Files/response.json")
    print(bestselling_books.get("status"))

    # find out if a book is best selling
    data_requested = bestselling_books

    return data_requested
