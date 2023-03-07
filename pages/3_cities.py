# Libraries
import plotly.express as px
import folium
from folium.plugins import MarkerCluster
import pydeck as pdk
import matplotlib.pyplot as plt

# necessary libraries
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image

from streamlit_folium import folium_static

# ---------------------------------------
# function
# ---------------------------------------

COUNTRIES = {
   1: "India",
   14: "Australia",
   30: "Brazil",
   37: "Canada",
   94: "Indonesia",
   148: "New Zeland",
   162: "Philippines",
   166: "Qatar",
   184: "Singapure",
   189: "South Africa",
   191: "Sri Lanka",
   208: "Turkey",
   214: "United Arab Emirates",
   215: "England",
   216: "United States of America",
}
def country_name(country_id): 
    return COUNTRIES[country_id]

def create_price(price_range):
    if price_range == 1: return "cheap"
    elif price_range == 2: return "normal"
    elif price_range == 3: return "expensive"
    else:
        return 4
    
COLORS = {
   "3F7E00": "darkgreen",
   "5BA829": "green",
   "9ACD32": "lightgreen",
   "CDD614": "orange",
   "FFBA00": "red",
   "CBCBC8": "darkred",
   "FF7800": "darkred",
}
def color_name(color_code): 
    return COLORS[color_code]
     
def Delivery_yes_no(yes_no):
    if yes_no == 0:
        return 'yes'
    elif yes_no == 1:
        return 'no'    
    else:
        return 'nao definido' 
    
def media_max_avaliacao(df1):    
    cols = ['Restaurant Name','Cuisines','Aggregate rating']
    ax_max = df.loc[:,cols].groupby('Restaurant Name').max().sort_values(['Aggregate rating'],ascending=False).reset_index()
    return ax_max

def media_min_avaliacao(df1):   
    cols=['Restaurant Name','Cuisines','Aggregate rating']
    ax_min = df.loc[:,cols].groupby(['Restaurant Name']).min().sort_values(['Aggregate rating'],ascending=True).reset_index()
    return ax_min
     
# -------------------        
# Limpeza do dataset
# -------------------

def clean_code(df):
    df['Country Code'] = df['Country Code'].transform(country_name, axis=0)
    df['Price range'] = df['Price range'].transform(create_price, axis=0)
    df['Rating color'] = df['Rating color'].transform(color_name, axis=0)
    df['Has Table booking'] = df['Has Table booking'].apply(Delivery_yes_no)

def rename_columns(dataframe):
    df = df1.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace('','') 
    cols_old = list(df.columns)
    cols_old = list(map(title,cols_old))
    cols_old = list(map(spaces,cols_old))
    cols_old = list(map(snakecase,cols_old))
    df.columns = cols_new
    
    return df    

# ---- Inicio da Estrutura logica do codigo ---
# Import dataset
df = df = pd.read_csv('datasete/zoomato.csv')
df1 = df.copy()

# clearing data
data = clean_code(df)

# ---------------------------------
#  Sidebar
# ---------------------------------

st.set_page_config(
    page_title='cities',
    page_icon='🏙'
)
# image_path = '/Users/hallanmiranda/Documents/repos/ftc/kill-your-hangre/images.png'
image = Image.open( 'images.png' )
st.sidebar.image(image, width=120)

st.sidebar.markdown('## KILL YOUR HANGRE')
st.sidebar.markdown("""---""")

st.sidebar.markdown("""---""")
st.sidebar.markdown('Pawered by project company')

# --------------------------------------
# Layout Streamlit
# --------------------------------------
tab1,tab2 = st.tabs(['Quantities metrics by cities','Top 10 max quantities'])
with tab1:
    with st.container():
        st.title('Number of restaurants by city')
        qtd_rest_city = df1.groupby('City')['Restaurant Name'].count().head(10)
        st.plotly_chart(px.bar(qtd_rest_city, qtd_rest_city,color='Restaurant Name', text='Restaurant Name' ))
       
    with st.container():
        st.title('Number of restaurants by country')
        col = ['City','Country Code']
        pais_mais_cidades = df.loc[:, col].groupby('Country Code').count().sort_values(['City'], ascending=False).reset_index()
        st.plotly_chart(px.bar(pais_mais_cidades, x='City', y='Country Code', color='City', text='City'))
        
with tab2:
    with st.container():
        st.title('Top 10 city with max restores in the database')
        city_max_restaurants = df1.groupby('City')['Restaurant Name'].count().sort_values(ascending=False).head(10)
        st.plotly_chart(px.bar(city_max_restaurants, city_max_restaurants,color='Restaurant Name', text='Restaurant Name' ))
        
    with st.container():
        st.title('Top 7 Cities rated above 4')
        max_top7 = df1[df1['Aggregate rating'] == 4]['City'].value_counts().head(7)
        st.plotly_chart(px.bar(max_top7, max_top7,color='City'))

    with st.container():
        st.title('Top 7 Cities Rated Below 2.5')
        min_top7 = df1[df1['Aggregate rating'] <= 2.5]['City'].value_counts().head(7)
        st.plotly_chart(px.bar(min_top7, min_top7, color='City'))

    with st.container():
        st.title('Top 10 cities with distinctive cuisine restaurant')
        top10_culinaria = df1.groupby('City')['Cuisines'].count().sort_values(ascending=False).head(10)
        st.plotly_chart(px.bar(top10_culinaria, top10_culinaria, color='Cuisines'))