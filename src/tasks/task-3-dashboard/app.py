import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px


st.title('CO2-Dashboard')

df = pd.read_csv('final_df.csv')

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

    if text_input == 'almonds':
        st.image('licensed-image.jpg', width=200)

    # some plt chart
    #arr = np.random.normal(1, 1, size=100)
    #fig, ax = plt.subplots()
    #ax.hist(arr, bins=20)

    #st.pyplot(fig)


    # Ploting with Altair

    if item_row['Agriculture'].iloc[0]==item_row['Food_processing'].iloc[0]==item_row['Transport'].iloc[0]==item_row['Packaging'].iloc[0]==0:
        print('zero value')

    else:
        chart = (alt.Chart(item_row).mark_bar()
        .encode(
            alt.X('CO2_per_kg'),
            alt.Y('item'),
            alt.Tooltip(['Agriculture', 'Food_processing', 'Transport', 'Packaging']),
            ).interactive()
        )
        st.altair_chart(chart)



        pie_plot = pd.melt(item_row, id_vars=['item'], value_vars=['Agriculture', 'Food_processing',    'Transport', 'Packaging'], var_name="CO2" ,value_name="CO2value")

        #print(pie_plot)
        #item_name = item_row

        pie_chart = px.pie(pie_plot,
                       title=f"CO2 of {text_input}",
                       values="CO2value",
                       color="CO2",
                       color_discrete_map={ 'Agriculture':'darkgreen',
                                            'Food_processing':'lime',
                                            'Transport':'yellow',
                                            'Packaging':'orange'},
                       names="CO2"
                      )

        st.plotly_chart(pie_chart)

except:
    st.write('Sorry, no such product')
