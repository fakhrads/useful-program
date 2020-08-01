import requests, json

class Instagram:
    
    def get_data_profile(self, username):
        instaUrl = "https://www.instagram.com/%s/?__a=1" % username
        data = requests.get(instaUrl)
        data = data.json()
        return data

    def parse_data_profile(self, jsonData):
        data = json.dumps(jsonData)  
        data = json.loads(data)  
        re_ = "Username : %s" % str(data['graphql']['user']['username'])
        re_ += "\nBiograph : %s" % str(data['graphql']['user']['biography'])
        re_ += "\nPrivate? : %s" % str(data['graphql']['user']['is_private'])
        re_ += "\nProfile Pict : %s" % str(data['graphql']['user']['profile_pic_url'])
        re_ += "\nProfile Pict (HD) : %s" % str(data['graphql']['user']['profile_pic_url_hd'])
        return re_
        
        
insta = Instagram()
data = insta.get_data_profile("fakhrads")
print(insta.parse_data_profile(data))