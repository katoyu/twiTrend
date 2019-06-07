from requests_oauthlib import OAuth1Session

class Request_info():

    def __init__(self):
        self.url_timeline = "https://api.twitter.com/1.1/statuses/home_timeline.json"
        #↓エンドポイントURLを追加
        self.url_friendships = "https://api.twitter.com/1.1/friendships/lookup.json"
        self.ck = "tdRm2l0DSa4SHSwoyIh0PqHG3"
        self.cs = "jO3tWKk0b41qgxxxTvGx2n8DByjEDyvrgTC0l8Lv0JD19PcfRV"
        self.at = "4014297194-QUlxbyRdppb0LUR3aJ00G1mODnHCU2v7rauO8xC"
        self.ats = "AjtqfOKjLNczhmfgs8W4hRsu4qror7AV8cWFW4AgVD7uz"

class Read_api(Request_info):

    def get_timeline(self):
        continer = []
        twitter = OAuth1Session(self.ck, self.cs, self.at, self.ats)
        req = twitter.get(self.url_timeline, params={})
        if req.status_code == 200:
            return [True, req.status_code, req]
        else:
            status = "GET TIMELINE" + str(req.status_code)
            return [False, status, False]


    def get_friendships(self, ids):
        #判定用の情報をAPIから取得する
        params = {"user_id": ids}
        twitter = OAuth1Session(self.ck, self.cs, self.at, self.ats)
        req = twitter.get(self.url_friendships, params=params)
        if req.status_code == 200:
            return [True, req.status_code, req]
        else:
            status = "GET FRIENDSHIPS" + str(req.status_code)
            return [False, status, False]
