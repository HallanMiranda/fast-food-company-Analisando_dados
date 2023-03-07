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
    page_title='Main Page',
    page_icon='📊'
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
tab1, tab2 = st.tabs(['Metrics Restaurants','Metrics Cuisines'])
with tab1:
    
    with st.container():
        st.title('Number of registered restaurants per country')
        pais_mais_restaurantes = df.groupby(['Country Code']).count().sort_values(['Restaurant Name'], ascending=False).reset_index()
        st.plotly_chart(px.bar(pais_mais_restaurantes,  x='Restaurant Name', y='Country Code',color='Restaurant Name',text = 'Restaurant Name'))
        
    with st.container():
        st.title('Number of restaurants by city')
        qtd_rest_pais = df.groupby('City').nunique().sort_values(['Restaurant Name'], ascending=False).reset_index()
        st.plotly_chart(px.bar(qtd_rest_pais, x='City', y='Restaurant Name', color='Restaurant Name', text='City'))
        
    with st.container():
        st.title('Number of restaurants per note')
        qtd_rest_voto = df.groupby('Aggregate rating').count().sort_values(['Restaurant Name']).reset_index()
        st.plotly_chart(px.bar(qtd_rest_voto, x='Aggregate rating', y='Restaurant Name', text='Aggregate rating'))
        
    with st.container():
        st.title('Top 15 restaurants by type of cuisine')
        col = ['Cuisines','Restaurant Name']
        qtd_rest_culinaria = df.loc[:,col].groupby('Restaurant Name').count().sort_values(['Cuisines'], ascending=False).reset_index().head(15)
        st.plotly_chart(px.bar(qtd_rest_culinaria, x='Restaurant Name',y='Cuisines', color='Cuisines' , text='Cuisines'))
        
    with st.container():
        st.title(" Number of restaurants that make reservations and that don't ")
        col = ['City','Has Table booking','Restaurant Name']
        qtd_rest_reserva = df.loc[:,col].groupby('Has Table booking').count().reset_index()                             
        st.plotly_chart(px.bar(qtd_rest_reserva,x='City', y='Has Table booking', color='Restaurant Name', text='Restaurant Name'))
        
    with st.container():
        st.title('Number of restaurants that accept and do not accept online orders.')
        col = ['City','Has Online delivery','Restaurant Name']
        qtd_rest_pedidos_on = df.loc[:,col].groupby('Has Online delivery').count().reset_index()
        st.plotly_chart(px.bar(qtd_rest_pedidos_on,x='Has Online delivery',y='City', color='City',text='City'))
        
with tab2:
    with st.container():
        st.title('Top 10 countries with the highest quantities of cuisines.') 
        top_country_culinaria_max = df.groupby('Country Code')['Cuisines'].count().reset_index()
        st.plotly_chart(px.bar(top_country_culinaria_max,x='Country Code',y='Cuisines', color='Cuisines' ,text='Cuisines'))
        
    with st.container():
        st.title('Top 10 countries with less cuisine') 
        top_country_culinaria_min = df.groupby('Country Code')['Cuisines'].count().sort_values(ascending=True).reset_index().head(10)
        st.plotly_chart(px.bar(top_country_culinaria_min,x='Country Code', y='Cuisines', color ='Cuisines' , text='Cuisines'))
    
    with st.container():
        st.title('Top 10 cities with the greatest cuisine') 
        top_city_culinaria_max = df.groupby('City')['Cuisines'].count().sort_values(ascending=False).reset_index().head(10)
        st.plotly_chart(px.bar(top_city_culinaria_max, x='City', y='Cuisines', color ='Cuisines' , text='Cuisines'))
        
    with st.container():
        st.title('Top 10 cities with the smallest cuisine') 
        top_country_culinaria_min = df.groupby('City')['Cuisines'].count().sort_values(ascending=True).reset_index().head(10)
        st.plotly_chart(px.bar(top_country_culinaria_min, x='City', y='Cuisines', color = 'Cuisines', text='Cuisines'))
             
            
           