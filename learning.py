import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("聖地巡礼アプリの実験")


m = folium.Map(location=[35.6853, 139.7203], zoom_pytostart=15)
folium.Marker(
    location=[35.6853, 139.7203],
    popup="須賀神社前階段",
    tooltip="君の名は",    
    icon= folium.Icon(color="red",icon="info-sign")
).add_to(m)

st_folium(m, width=700, height=500)
