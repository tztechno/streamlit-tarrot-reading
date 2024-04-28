import streamlit as st
import pandas as pd
import os
import random
from PIL import Image

data_dir = './cards'
files = os.listdir(data_dir)
data = pd.read_json('./tarot-images.json', orient='records')
data = pd.json_normalize(data['cards'])
data1 = data[['name', 'img', 'fortune_telling']][data['arcana'] == 'Major Arcana']

def predict():
    rand3 = random.sample(range(22), k=3)
    fortune = []
    name = []
    file = []
    for i in rand3:
        fortune.append(data1.loc[i, 'fortune_telling'][0])
        name.append(data1.loc[i, 'name'])
        file.append(data1.loc[i, 'img'])
    times = ['Past', 'Present', 'Future']
    images = []
    for i in range(3):
        img = Image.open(os.path.join(data_dir, file[i]))
        images.append(img)
    return times, fortune, name, images

st.title("Tarot Reading!")

if st.button("Predict Your Fortune"):
    times, fortune, name, images = predict()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(images[0], caption=name[0], use_column_width=True)
        st.write(f'Your {times[0]} is {name[0]}.')
        st.write(f'{fortune[0]}.')
    with col2:
        st.image(images[1], caption=name[1], use_column_width=True)
        st.write(f'Your {times[1]} is {name[1]}.')
        st.write(f'{fortune[1]}.')
    with col3:
        st.image(images[2], caption=name[2], use_column_width=True)
        st.write(f'Your {times[2]} is {name[2]}.')
        st.write(f'{fortune[2]}.')