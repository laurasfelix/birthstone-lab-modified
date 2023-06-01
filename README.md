# Birthday Lab
You will be creating a website that takes in a user's birthday and returns information based on that birthday.

## MVP 1: Birthstone 
At this stage, the user should be able to input their name and birthday into a form and get back the birthstone that matches their birthday. It should also adhere to the following specifications:
1. Your `index.html` page should be formatted with bootstrap using the forms component and your `results.html` page should be formatted using bootstrap.
1. The `results.html` page should include an image and description of the right gem, the name of the person. The images of each gem for each month can be found in the `static/img` folder and were taken from [this website](https://www.gemsociety.org/article/birthstone-chart/).
1. In your `model.py`, use the `datetime` library to help parse the date input you get from the form. You should define a function to the tune of `get_birthstone(date_string)` that returns the birthstone given a particular date.

## MVP 2: Holidays
Add another input that asks what country they are from. Then, install and use the python `holidays` library to tell the user about all holidays that fall on their birthday and are observed in their country. It should follow these specifications: 
1. The form should use a dropdown input. This will ensure that you'll always get nicely formatted country inputs that work with the `holidays` library. You should include at least 10 different countries in that dropdown input.
1. The additional result retrieved from  page should be properly formatted using bootstrap, and should also support a display message that says something like "no holidays on your birthday" if none are found.
1. In your `model.py`, you should define a function to the tune of `get_holidays(date_string)` that returns a list of all holidays on that particular date. 

## MVP 3: GIPHY API 
Use any/all of their inputted information to return several gifs (i.e related to their birthstone, holidays on that day, ) using the [GIPHY API](https://developers.giphy.com/docs/api/endpoint#endpoint) and the `requests` library from flask on the `results.html` page. Feel free to ask the user for extra inputs in the form to help with the gif searching. It should also adhere to the following specifications:
1. The giphy image results should be properly formatted with bootstrap grid (and in a carousel if you want to make things harder! :))) )
1. In your `model.py`, you should define a function to the tune of `make_img_tag(gif_obj)` that takes in a gif object (which is what the GIPHY API returns) and returns a string representation of an image tag that includes a proper `src` and `alt` attribute.
1. You should also account for the chance that no images from giphy were found and should also filter out gifs with a rating of `r`.

## MVP 4: Your Own Addition
Add something else that uses inputs about user information! Feel free to look up APIs/python libraries that you'd like to use. Here are some ideas:
- The highest valued publicly traded stock on their birthday
- A list of companies founded the year they were born
- A list of companies that went bankrupt the year they were born
- Their horoscope
- Celebrity birthdays that fall on their birthday
- Free food/deals on their birthday