import requests, json, time

status = "Example status"
token = "Account authencation token here"

class main:
    def __init__(self, token, status):
        self.token = token
        self.status = status
        i = 0
        try:
            while True:
                string = self.status[0:i+1]
                print(string)
                self.set_status(string)
                i += 1
                if len(string) > len(self.status)-1:
                    time.sleep(1)
                    i = 0
                    string = self.status[0:i+1]
                    print(string) 
                    self.set_status(string)
                    i += 1             
                time.sleep(1)
        
        except KeyboardInterrupt:
            print("Stopped auto status!")
            exit()
    def set_status(self, status):
        requests.patch("https://discord.com/api/v9/users/@me/settings", headers={"authorization": self.token,"content-type": "application/json"}, data=json.dumps({"custom_status":{"text":status,"emoji_name":"👉"}}))

if __name__ == "__main__":
    if requests.patch("https://discord.com/api/v9/users/@me", headers={"authorization": token,"content-type": "application/json"}).status_code == 400:
        main(token, status)
    else:
        print("Failed to connect to token")
        exit()
