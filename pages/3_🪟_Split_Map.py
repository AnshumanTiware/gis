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

st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        m.split_map(
            left_layer="ESA WorldCover 2020 S2 FCC", right_layer="ESA WorldCover 2020"
        )
        m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")

m.to_streamlit(height=700)
