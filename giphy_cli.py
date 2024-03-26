import giphy_api

class GiphyCLI:
    GiphyAPI = giphy_api()
    # A CLI class that interfaces with the Giphy API to get trending gifs or search gifs    
    def get_trending(self, count, markdown):
        dict = giphy_api.call_trending(count)
        if(markdown):
            print(f'MARKDOWN FORMATTED STRING ')
            return dict
        else:
            print(f'NON-MARKDOWN FORMATTED STRING')
            return dict
        

    def get_search(self, count, markdown, query, lucky):
        #first collect the data before we proceed
        dict = giphy_api.call_search(count, query)
       #Check to see if the lucky option was used
        if lucky:
            print(f'SO YOURE FELLING LUCKY! ')
            return dict
        #Check to see if the markdown option was used
        if(markdown):
            #If so, output the data as a in markdown format
            print(f'MARKDOWN FORMATTED STRING ')
            return dict
        else:
            #If so, output the data
            print(f'NON-MARKDOWN FORMATTED STRING')
            return dict


###########This file should be the logic for the CLI Tool. It should do the MarkDown Transcripting 
###########along with getting the links form the requests and printing them ect.