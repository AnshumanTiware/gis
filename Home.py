import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
This app explores different types of geospatial applications geared towards effective and efficient data visualization to draw useful insights for downstream applications.
<https://github.com/AnshumanTiware/gis>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "public/logo.jpeg"
st.sidebar.image(logo)

# Customize page title
st.title("Geo-Insights")

st.markdown(
    """
    This multipage app aims to demonstrate various types of geospatial visualizations which can be used to gather insights for downstream business applications. 
    """
)

st.header("Visualizations")

markdown = """
1. Heatmap: These visualizations are good to see the intensity/ magnitude of a variable of interest in different locations.
2. Interactive Dashboard: This type of dashboard shows all the desired metrics as the user hovers over the area of interest.
3. Marker Cluster: These are good for clustering the locations based on certain predefined metric.
4. Split Map: These maps are good for comparison purposes, the split halves may represent the status before and after the change for instance.
5. Interactive Map: A map visualization to show the locations at a fine grained location around the area of interest.
6. Basemaps: This app is a demonstration of searching and loading basemaps from xyzservices and Quick Map Services (QMS). Selecting from 1000+ basemaps with a few clicks.
7. Web Map Service: This app is a demonstration of loading Web Map Service (WMS) layers. 
"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
