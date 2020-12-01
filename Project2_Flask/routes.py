from Project2_Flask import app
from Project2_Flask import forms
from flask import request, render_template


@app.route('/')
@app.route('/page1')
def page1():
    return "page 1"


@app.route('/search', methods=['GET', 'POST'])
def search():
    #instantiate the flask form NewsForm class
    my_form = forms.NewsForm(request.form)
    data = forms.generateDataFromAPI()
    print(data.get("status"))

    # this block is only entered when the form is submitted
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        option = request.form['option']
        option2 = request.form['option2']

        i = option2
        print(i)
        #description = book_title + ' by ' + book_author

        if option == 'review':
            book_title2 = data['results'][int(i)]['title']
            book_author = data['results'][int(i)]['author']
            #This particular API does not have many reviews to work with, I put the .get
            # to avoid getting a Key error, and instead display None.
            #This API was one of the only ones I was interested in, which is why I decided
            #to keep with it, but the lack of data didn't help. The project still
            #has all the required functionallity.
            reviews = data.get(['results'][int(i)][2]['sunday_review_link'])
            review1 = "Here are your results " \
                      "of best-selling books: \n" + str(book_title2) + str(reviews)
        elif option == 'description':
            book_title2 = data['results'][int(i)]['title']
            book_author = data['results'][int(i)]['author']
            description = str(book_title2) + " by " + str(book_author)

        response = [first_name, last_name, option, option2]
        return render_template('results.html', response=response,
                               description=description, form=my_form,
                               data=data, review1=review1)

    return render_template('search.html', form=my_form)
