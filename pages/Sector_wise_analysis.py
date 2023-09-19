
import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Plotting Sector Analysis")

st.header('Sector-wise Amenities WordCloud')

wordcloud_df = pickle.load(open('datasets/sector_wordcloud.pkl','rb'))

sector_features = wordcloud_df.groupby('sector')['features'].apply(lambda x: ' '.join(str(i) for i in x)).reset_index()
option = st.sidebar.selectbox('Select sector',sector_features['sector'])

target_sector = option
filtered_df = sector_features[sector_features['sector'] == target_sector]

features_text = ' '.join(str(i) for i in filtered_df['features'])

# Create and display the word cloud for the specified sector
def generate_word_cloud(text, sector):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f'Word Cloud for Features in Sector: {sector}')
    plt.axis('off')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

generate_word_cloud(features_text, target_sector)


