import streamlit as st
from main2 import import_data
from send_email2 import send_email

heading,image_link,data,content=import_data()
st.set_page_config(layout="wide")


st.title(heading)
st.image(image_link)
st.write(data)


send_email(f"Subject : NASA APOD : Astronomy Picture of the Day \n"\
           f"Hey there!! please find todays NASA's APOD information \n"
           f" todays topic is {heading}"
           f" please find the image of it {content['url']} and explanation {data}")


