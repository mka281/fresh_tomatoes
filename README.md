# Fresh_Tomatoes

This project is for Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

I wrote the server-side code to display my favorite movies using provided [started code](https://github.com/udacity/ud036_StarterCode) and [The Movie DB API](https://www.themoviedb.org/documentation/api).

You can view the generated HTML page [here](https://mka281.github.io/fresh_tomatoes/)

## How to run the code

* Clone the repository `git clone https://github.com/mka281/fresh_tomatoes.git`
* Go to the project folder `cd fresh_tomatoes`
* Make sure you have Python 3 installed with `python3 --version`
* If you don't see an output like "Python 3.x.x", you can download [here](https://www.python.org/downloads/)
* To make API requests, you need an API key from [The Movie DB API](https://developers.themoviedb.org/3/getting-started/introduction)
* Change the `api_key` variable with your API key in the `entertainment_center.py` file
* Run `python3 entertainment_center.py`
* The generated HTML file will be appear on your default browser.

## How to display your own movie list

* Before running `python3 entertainment_center.py` follow these steps:
* If you have a list on [The Movie DB](https://www.themoviedb.org)
* Go to the lists page and choose the list you want to display
* You will see page url is like https://www.themoviedb.org/list/XXXXX
* Change the `list_id` on the entertainment center with `XXXXX` part of the url.
* You can try this with any valid list_id from The Movie DB
