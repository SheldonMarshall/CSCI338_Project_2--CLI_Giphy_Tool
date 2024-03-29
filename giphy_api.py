# class GiphyAPI:
import requests

class GiphyAPI:
       
    #API Constructor
    # def __init__(self, api_key):
    #     self.api_key = api_key
    #     self.base_url = 'https://api.giphy.com/v1/gifs'
    
    def call_search(self, API_Key, count, term):
        endpoint = f"https://api.giphy.com/v1/gifs/search?api_key={API_Key}&q={term}&limit={count}&offset=0&rating=g"
        data = requests.get(endpoint)
        return data.json()

    def call_trending(self, API_Key, count):
        endpoint = f"https://api.giphy.com/v1/gifs/trending?api_key={API_Key}&limit={count}&offset=0&rating=g"
        data = requests.get(endpoint)
        return data.json()
    
    
    
    #######This file needs to process and make/send the calls to the Giphy API