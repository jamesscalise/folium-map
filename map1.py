import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
name = list(data["NAME"])
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
Name: %s <br />
Height: %s m
"""

def color_producer(el):
    if el < 1000:
        return 'green'
    elif 1000 <= el < 3000:
        return 'orange'
    else:
        return 'red'

map= folium.Map(location=[38.58,-99.09], zoom_start=6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")



for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (nm, el), width=200, height=100)
    fg.add_child(folium.CircleMarker(radius=6, fill=True, location=[lt, ln], popup=folium.Popup(iframe), fill_opacity=0.7, color=color_producer(el)))


fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding="utf-8-sig").read()),
style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' 
if 10000000 < x['properties']['POP2005'] < 20000000 else 'red'}))



map.add_child(fg)
map.save("Map3.html")