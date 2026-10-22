import pandas as pd
import requests
#URL points to a whole website, a URI points to one specific thing on a website

# uri = "https://portal.app.cent-su.org/api/funnyname/random?n=5"
# response = requests.get(uri) # this is just a string
# # you need to check the response here to make sure it worked and response is what you wanted

# response.raise_for_status() # this will raise an error if the response is not a 200 OK
# # if there is an exception here, the following lines will not run and the program will stop
# # it throws and error and raises an exception if the request failed 
# # the code will continue to run if the request was successful

# data = response.json() # you get back a python format and you can loop over it and call it and its much easier to use

# for name in data:
#     print(name["first"], name["last"])

    # status codes
    # 1XX are an informational codes
    # 2XX are success codes
    # 3XX are redirection codes
        # this means that your code is going to break eventually because the website is going to 
        # change and you will have to update your code
    # 4XX are client error codes
        # 404 Not Found
        # this means the requestor made an error
    # 5XX are server error codes
        # these are not your fault, they are service errors


url = "https://portal.app.cent-su.org/api/weather/geocode"

# Pass query parameters separately; requests handles URL encoding.
# all the parameters are stoped in this dictionary 
params = {
    "language": "en",
    "count": 5,
    "place": "Syracuse, New York",
}
headers = {
    "accept": "application/json",
    "X-API-KEY": 'd404ab024a625b70d37134e1'
} # you need to fill your API key here

response2 = requests.get(url, params=params, headers=headers, timeout=30) # this is just a string
print(response2.url)
response2.raise_for_status()

data = response2.json()
df = pd.json_normalize(data["results"])
print(df)