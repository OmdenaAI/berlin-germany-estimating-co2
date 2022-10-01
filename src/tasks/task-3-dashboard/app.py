import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('CO2-Dashboard')

df = pd.read_csv('data.csv')

all_items = df['item']

with st.sidebar:
    #text_input = st.text_input('Type the name of the product')
    text_input = st.selectbox('Choose the name of the product', all_items)

# ToDo: Transform everything to lower case

try:
    item_row = df[df['item'] == text_input]

    co2 = item_row['CO2_per_kg'].iloc[0]
    co2_level = item_row['CO2_level'].iloc[0]

    st.write(co2, co2_level)

    if text_input == 'Almonds':
        st.image('licensed-image.jpg', width=200)

    # some plt chart
    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    st.pyplot(fig)

except:
    st.write('Sorry, no such product')
