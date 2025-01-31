import streamlit as st
import requests
from send_email2 import send_email

api_key = "Ekuf9BVcWhzncj4rgphbD0irrTKF8XszImvuVPgV"
url = ("https://api.nasa.gov/planetary/apod?"\
       f"&api_key={api_key}")

#make request
response= requests.get(url)

#Get a dictionary with data
content = response.json()
print(content)

#title for the content
news_title = content['title']
print(news_title)

#URL for image
image_url = content['url']
print(image_url)

#data for title
title_info = content['explanation']
print(title_info)

#download the image
image_filepath = "img.png"
response_2 = requests.get(image_url)

with open(image_filepath,'wb') as file:
       file.write(response_2.content)

def import_data():
       print(news_title)
       return news_title,image_filepath,title_info,content

