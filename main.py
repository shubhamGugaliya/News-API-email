import requests
from pandas.io.sas.sas_constants import text_block_size_length

from send_email import send_email

topic = 'love'
api_key = "fa4a0fd3104d4fc0974571bdaecd92d3"
url= ("https://newsapi.org/v2/everything?"\
       f"q=topic"\
      "&language=en"
       "&from=2024-12-30"\
      "&sortBy=publishedAt"\
      "&apiKey=fa4a0fd3104d4fc0974571bdaecd92d3")

#make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

num=1

body=''
#Access article titles and descriptions:
for article in content['articles'][:20]:
    if article['title'] is not None:
        body = body + article['title'] + article['description'] + article["url"] + 2*"\n"
    # print(f"below are the articles {num} - {article['title']} \n")
    # print(f"Also find the description for above title {num} \n {article['description']}")
    # num+=1

body = body.encode("utf-8")

send_email(message=body)
