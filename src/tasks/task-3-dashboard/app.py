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

    #-------products comparison------

    st.sidebar.header('Products CO2 Emission Comparison')
    product_list = df['item'].unique().tolist()
    product_comparison = st.multiselect('Choose the products', product_list)

    #------product comparison end----

try:

    item_row = df[df['item'] == text_input]

    co2 = item_row['CO2_per_kg'].iloc[0]
    co2_level = item_row['CO2_level'].iloc[0]

    #st.write(co2, co2_level)

    st.markdown("""
    <style>
    div[data-testid="metric-container"] {
       background-color: rgba(128, 128, 128, 1);
       border: 1px solid rgba(28, 131, 225, 0.1);
       padding: 5% 5% 5% 10%;
       border-radius: 5px;
       color: rgb(30, 103, 119);
       overflow-wrap: break-word;
    }
    
    /* breakline for metric text         */
    div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
       overflow-wrap: break-word;
       white-space: break-spaces;
       color: red;
    }
    </style>
    """
    , unsafe_allow_html=True)

    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.metric('CO2 value per kg', co2)
    with col2:
        st.metric('CO2 level', co2_level)


    if text_input == 'almonds':
        st.image('licensed-image.jpg', width=200)

    # Ploting with Altair

    if item_row['Agriculture'].iloc[0]==item_row['Food_processing'].iloc[0]==item_row['Transport'].iloc[0]==item_row['Packaging'].iloc[0]==0:
        print('zero value')

    else:

    #------Plotting as a Pie-plot-------------
        pie_plot = pd.melt(item_row, id_vars=['item'], value_vars=['Agriculture', 'Food_processing',    'Transport', 'Packaging'], var_name="CO2" ,value_name="CO2value")

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

    #------Product comparison-----
    df = df[df['item'].isin(product_comparison)]

    fig2 = px.bar(df, x='CO2_per_kg', y='item', color='CO2_per_kg', log_x=True, title='Carbon Footprint Comparison for Products', labels={'CO2_per_kg': 'Carbon Emission per kg', 'item': 'Products'})
    fig2.update_layout(width=900)

    st.write(fig2)
    #------Product comparison-----

except:
    st.write('Sorry, no such product')
