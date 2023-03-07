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
     
# -------------------        
# Limpeza do dataset
# -------------------

def clean_code(df):
    df['Country Code'] = df['Country Code'].transform(country_name, axis=0)
    df['Price range'] = df['Price range'].transform(create_price, axis=0)
    df['Rating color'] = df['Rating color'].transform(color_name, axis=0)
    df['Has Table booking'] = df['Has Table booking'].apply(Delivery_yes_no)
    
# ---- Inicio da Estrutura logica do codigo ---
# Import dataset
df = pd.read_csv('datasete/zoomato.csv')
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
st.title('KILL YOUR HANGRE!')
st.header('The best place for you to find your newest favorite restaurant!')
st.markdown('We have the following restaurants within our platform.')

# image_path = '/Users/hallanmiranda/Documents/repos/ftc/kill-your-hangre/images.png'
image = Image.open( 'images.png' )
st.sidebar.image(image, width=120)

st.sidebar.markdown('## KILL YOUR HANGRE')
st.sidebar.markdown("""---""")

select_pais = st.sidebar.multiselect(
    'Select the desired Country.',
    ['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'])

select_city = st.sidebar.multiselect('Select the desired City.',
    ['Las Piñas City', 'Makati City', 'Mandaluyong City', 'Manila',
       'Marikina City', 'Muntinlupa City', 'Pasay City', 'Pasig City',
       'Quezon City', 'San Juan City', 'Tagaytay City', 'Taguig City',
       'Brasília', 'Rio de Janeiro', 'São Paulo', 'Adelaide', 'Atlanta',
       'Austin', 'Boston', 'Brisbane', 'Calgary', 'Charlotte', 'Chicago',
       'Dallas', 'Denver', 'Detroit', 'Houston', 'Las Vegas',
       'Los Angeles', 'Miami', 'Montreal', 'New Orleans', 'New York City',
       'Ottawa', 'Perth', 'Philadelphia', 'Phoenix', 'Portland',
       'San Antonio', 'San Diego', 'San Francisco', 'Seattle',
       'Singapore', 'Washington DC', 'Abu Dhabi', 'Dubai', 'Fujairah',
       'Sharjah', 'Agra', 'Ahmedabad', 'Allahabad', 'Amritsar',
       'Aurangabad', 'Bangalore', 'Bhopal', 'Bhubaneshwar', 'Chandigarh',
       'Chennai', 'Coimbatore', 'Dehradun', 'Gandhinagar', 'Gangtok',
       'Ghaziabad', 'Goa', 'Gurgaon', 'Guwahati', 'Hyderabad', 'Indore',
       'Jaipur', 'Kanpur', 'Kochi', 'Kolkata', 'Lucknow', 'Ludhiana',
       'Mangalore', 'Mohali', 'Mumbai', 'Mysore', 'Nagpur', 'Nashik',
       'Nasik', 'New Delhi', 'Noida', 'Ooty', 'Panchkula', 'Patna',
       'Puducherry', 'Pune', 'Ranchi', 'Secunderabad', 'Shimla', 'Surat',
       'Thane', 'Vadodara', 'Varanasi', 'Vizag', 'Zirakpur', 'Bogor',
       'Jakarta', 'Tangerang', 'Auckland', 'Hamilton', 'Wellington',
       'Wellington City', 'Birmingham', 'Edinburgh', 'Glasgow', 'London',
       'Manchester', 'Doha', 'Cape Town', 'Clarens', 'Durban',
       'East Rand', 'Inner City', 'Johannesburg', 'Johannesburg South',
       'Midrand', 'Pretoria', 'Randburg', 'Roodepoort', 'Sandton',
       'Colombo', 'Ankara', 'İstanbul'])

select_culinaria = st.sidebar.multiselect(
    'What cuisine do you want?',
    ['Italian', 'European, Asian',
       'Filipino, American, Italian, Bakery', ...,
       'Fast Food, Izgara, Seafood, Tea, Coffee', 'Home-made, Izgara',
       'Restaurant Cafe, Kebab, Turkish Pizza'])

st.sidebar.markdown("""---""")
st.sidebar.markdown('Pawered by project company')

# --------------------------------------
# Layout Streamlit
# --------------------------------------
tab1,tab2 = st.tabs(['General Metric','Metric by Distribution'])
with tab1:
    with st.container():
        col1,col2,col3,col4,col5 =st.columns(5)
        with col1:
            ax1=len(df.loc[:,'Restaurant ID'].unique())
            col1.metric( 'Registered Restaurants',ax1 ) 
        with col2:
            país_registrado = df['Country Code'].nunique()
            col2.metric('Paises Cadastrados', país_registrado) 
            
        with col3:
            city_unicas = df['City'].nunique()
            col3.metric('Registered Cities',city_unicas) 
            
        with col4:
            total_avaliacao = df['Aggregate rating'].sum()
            col4.metric('Ratings made on the Platform',total_avaliacao) 
                        
        with col5:
            tipo_culinaria = len(df.loc[:,'Cuisines'].unique())
            col5.metric( 'Types of Cuisine', tipo_culinaria )
            
    with st.container():
        st.title('Map')
        df_aux = df.loc[:,['Country Code','City','Latitude','Longitude','Restaurant Name','Cuisines',]].groupby(['Country Code','City','Restaurant Name']).median().reset_index()
        df_aux = df_aux.loc[df_aux['City'] != 'Nan',:]
        df_aux = df_aux.loc[df_aux['Country Code'] != 'Nan',:]

        map = folium.Map()
        
        for index, location_info in df_aux.iterrows():
            folium.Marker([location_info['Latitude'],
                           location_info['Longitude']],
                           popup=location_info[['Latitude','Longitude']]).add_to(map)
         
        folium_static(map, width=1024, height=600)
               
with tab2:
    with st.container():
        st.title("Percentage of restaurants by country")
        country_counts = df['Country Code'].value_counts()
        colors =['blue', 'red', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'black', 'cyan', 'magenta', 'indigo', 'violet', 'turquoise']
        fig, ax = plt.subplots()
        plt.pie(country_counts,labels=country_counts .index, autopct='%1.1f%%', explode=[0.2]*len(country_counts), colors=colors)
        fig.set_size_inches(10, 10)
        plt.legend(country_counts.index)
        st.pyplot(fig)
                
    with st.container():
        st.title('Distribution of restaurants by price category')
        price_range_counts = df.groupby('Price range')['Restaurant Name'].count().reset_index()
        st.plotly_chart(px.bar(price_range_counts, x='Price range', y='Restaurant Name',color='Restaurant Name',text='Restaurant Name'))
            
            
    with st.container():    
        st.title('Distribution of Restaurants by  Color')
        price_range_color_counts = df.groupby('Rating color')['Restaurant Name'].count().reset_index()
        st.plotly_chart(px.bar(price_range_color_counts, x='Rating color', y='Restaurant Name',color='Restaurant Name',text='Restaurant Name' ))
            
       
   