from giphy_api import GiphyAPI
import os
import random

#API Key import
# API_KEY=os.environ["GIPHY_API_KEY"]
Giphy_API = GiphyAPI()
class GiphyCLI:

    # def __init__(self, api_key):
    #     self.api_key = api_key
          

    # A CLI class that interfaces with the Giphy API to get trending gifs or search gifs    
    def get_trending(self, API_Key, count, markdown):
        # GiphyAPI = giphy_api(self.api_key)
        dict = Giphy_API.call_trending(API_Key, count)
        if(markdown):
            # print(f'MARKDOWN FORMATTED STRING ')
            for i, dict in enumerate(dict["data"][:count]):
                gif_title = dict["title"]
                gif_URL = dict["images"]["original"]["url"]
                string = (f"{i+1}) ![{gif_title}]({gif_URL})")
                # string = (f"{i+1}) ![{(dict["title"])}]({(dict["images"]["original"]["url"])})")
                print(string)
        else:
            # print(f'NON-MARKDOWN FORMATTED STRING')
            for i, dict in enumerate(dict["data"][:count]):
                gif_title = dict["title"]
                gif_URL = dict["bitly_url"]
                string = (f"{i+1}) {gif_title} ({gif_URL})")
                # string = (f"{i+1}) {(dict["title"])} ({(dict["bitly_url"])})")
                print(string)
        

    def get_search(self, API_Key, count, markdown, query, lucky):
        #first collect the data before we proceed
        # GiphyAPI = giphy_api(self.api_key)
        dict = Giphy_API.call_search(API_Key, count, query)
       #Check to see if the lucky option was used
        if lucky:
            print(f'SO YOURE FELLING LUCKY! ')
            return dict
        #Check to see if the markdown option was used
        if(markdown):
            # print(f'MARKDOWN FORMATTED STRING ')
            for i, dict in enumerate(dict["data"][:count]):
                gif_title = dict["title"]
                gif_URL = dict["images"]["original"]["url"]
                string = (f"{i+1}) ![{gif_title}]({gif_URL})")
                # string = (f"{i+1}) ![{(dict["title"])}]({(dict["images"]["original"]["url"])})")
                print(string)
        else:
            # print(f'NON-MARKDOWN FORMATTED STRING')
            for i, dict in enumerate(dict["data"][:count]):
                gif_title = dict["title"]
                gif_URL = dict["bitly_url"]
                string = (f"{i+1}) {gif_title} ({gif_URL})")
                # string = (f"{i+1}) {(dict["title"])} ({(dict["bitly_url"])})")
                print(string)


###########This file should be the logic for the CLI Tool. It should do the MarkDown Transcripting 
###########along with getting the links form the requests and printing them ect.