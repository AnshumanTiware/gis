# Geo-Insights

This multipage app aims to demonstrate various types of geospatial visualizations which can be used to gather insights for downstream business applications.
Web App URL: <https://anshumantiware-gis.streamlit.app/>

## Visualizations

The following visualizations are included in this application.

1. Heatmap: These visualizations are good to see the intensity/ magnitude of a variable of interest in different locations.
2. Interactive Dashboard: This type of dashboard shows all the desired metrics as the user hovers over the area of interest.
3. Marker Cluster: These are good for clustering the locations based on certain predefined metric.
4. Split Map: These maps are good for comparison purposes, the split halves may represent the status before and after the change for instance.
5. Interactive Map: A map visualization to show the locations at a fine grained location around the area of interest.
6. Basemaps: This app is a demonstration of searching and loading basemaps from xyzservices and Quick Map Services (QMS). Selecting from 1000+ basemaps with a few clicks.
7. Web Map Service: This app is a demonstration of loading Web Map Service (WMS) layers.

## Instructions

1. To see the app in action go to the link mentioned above.
2. Fork the GitHub repo to use it as a starter for your own project.
3. To run the app locally (after forking the repository and cloning it locally) use the following commands:

## Run Locally

Clone the project:

```bash
    git clone https://github.com/AnshumanTiware/gis.git



```

Note if you fork the repository, you must place the link of your forked repository in the above git clone command.

Install dependencies:

```bash
Go to the project directory
    pip install -r requirements.txt

```

Start the server

```bash
    streamlit run app.py
```
