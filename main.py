import requests
from send_email import send_email

api_key = "fa4a0fd3104d4fc0974571bdaecd92d3"
url= "https://newsapi.org/v2/everything?q=tesla&from=2024-12-30&sortBy=publishedAt&apiKey=fa4a0fd3104d4fc0974571bdaecd92d3"

#make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

num=1

body=''
#Access article titles and descriptions:
for article in content['articles']:
    body = body + article['title'] + article['description'] + 2*"\n"
    # print(f"below are the articles {num} - {article['title']} \n")
    # print(f"Also find the description for above title {num} \n {article['description']}")
    # num+=1

print(body[0])
body = body.encode("utf-8")
send_email(message=body)
