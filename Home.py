import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='Home',
    page_icon='🏭'
)
st.title('Delivery Fast Food')

# image_path = '/Users/hallanmiranda/Documents/repos/ftc/kill-your-hangre/images.png'
image = Image.open( 'images.png' )
st.sidebar.image(image, width=120)

st.sidebar.markdown('## KILL YOUR HANGRE')
st.sidebar.markdown('### Fastest Delivery in Town')
st.sidebar.markdown("""---""")
st.sidebar.markdown('Pawered by project company')
# --------------------------------------
# Layout Streamlit
# --------------------------------------


with st.container():
    st.write("# KILL YOUR HUNGRY BUSINESS METRICS PANEL ")
    st.markdown(
           """ 
Business Metrics Panel foi construido, para acompanhar as metricas dos restaurantes dos paises e cidades que estao em nossas plataformas. 

### Como ultilizar esse Panel?
         
Esta página deve incluir informações sobre o número de: 
- Overview:
    * General metrics com quantidades:
        - Restaurantes registrados, paises e cidades.
        - Culinarias registradas.
        - Avaliaçoes feitas na plataforma.
    * Metric by Distribution com as :
        - Porcentagem de restaurantes por Paises.
        - Distribuicao de Restaurantes por Preço.
        - Distribuicao de Restaurantes por Cor.
- Países:
    * Metrics Overview Countries.
        - Top 10 paises com maior quantidade de  restaurantes.
        - Top 10 cidades com maior quantidade de  restaurantes.
        - Quantidade de restaurante por país.
        - Quantidade de cidades registrada por país.
    * Average Overview Countries.
        - Media de votos por país.
        - Media de preco de prato para 2 pessoas.
- Cidades:
    * Quantities metrics by cities.
        - Number of restaurants by country 
        - Number of restaurants by city
    * Top 10 max quantities.
        - Top 10 city with max restores in the database 
        - Top 7 Cities rated above 4 
        - Top 7 Cities Rated Below 2.5 
        - Top 10 cities with distinctive cuisine restaurant

- Culinárias/Restaurantes:
    * Metrics Restaurants
        - Quantidade de restaurantes resgistrado por País.
        - Quantidade de restaurantes por cidade
        - Quantidade de restaurants per note 
        - Top 15 restaurantes por tipo de culinaria
        - Quantidade de restaurantes que fazem e nao fazem reservas.
        - Quantidade de restaurantes que aceita e nao aceita pedidos on-line.  
    * Metrics Cuisines
        - Top 10 Paises com a maior quantidade de culinaria.
        - Top 10 Paises com menor quantidade de culinaria
        - Top 10 Cidades com a maior culinaria
        - Top 10 Cidades com a menor culinaria
   
### Ask for Help
- Time de Data Science no Discord
- hallanmiranda@icloud.com
"""
)

