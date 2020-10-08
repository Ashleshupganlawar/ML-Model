import folium
import pandas as pd
import json
data = pd.read_csv("in.csv")
lat = list(data["lat"])
lon = list(data["lng"])
city = list(data["population"])

def color_icon (population):
    if population > 10000000:
        return "orange"
    elif population < 1000000:
        return "green"
    elif 5000000 > population < 10000000:
        return "red"
    else:
        return "blue"


map = folium.Map(location=[19.775604, 79.365134],zoom_start=10,tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="my map")
fp = folium.FeatureGroup(name="world map")

for lt,ln,ct in zip(lat,lon,city):
    fg.add_child(folium.CircleMarker(location=[lt,ln],raidus=6,popup="population "+str(ct),fill_color=color_icon(ct),color="gray",fill=True,fill_opacity=0.7))

fp.add_child(folium.GeoJson(data=open('world.json').read(),style_function = lambda x:{'fillcolor':'orange'} ))

map.add_child(fg)
map.add_child(fp)
map.add_child(folium.LayerControl())

map.save("hap.html")
