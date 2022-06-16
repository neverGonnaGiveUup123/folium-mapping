import folium
import pandas

data = pandas.read_csv('volcanoes.csv')
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEVATION"])

map = folium.Map(location=[-36.844660, 174.766619], tiles="Stamen Terrain", zoom_start=6)

fgv = folium.FeatureGroup(name='volcanoes')

def colour_elev(elev):
    if elev < 1000:
        return 'green'
    elif elev >= 1000 and elev < 2000:
        return 'orange'
    else:
        return 'red'

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], popup=str(el) + "m", 
    radius=6, fill_opacity=0.7, color='black', fill_color=colour_elev(el)))

fgp = folium.FeatureGroup(name='population')

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 
else 'red' if 10000000 <= x['properties']['POP2005'] < 50000000 else 'grey'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")