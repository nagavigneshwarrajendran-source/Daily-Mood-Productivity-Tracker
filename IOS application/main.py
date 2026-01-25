import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy_garden.mapview import MapView

class VigneMapApp(App):
    def build(self):
        # 1. Main Layout
        root = BoxLayout(orientation='vertical')
        
        # 2. Search UI (Top Bar)
        search_layout = BoxLayout(size_hint_y=None, height=50)
        self.search_input = TextInput(hint_text="Search City (e.g., Toronto)", multiline=False)
        search_btn = Button(text="Search", size_hint_x=None, width=100)
        search_btn.bind(on_release=self.search_location)
        
        search_layout.add_widget(self.search_input)
        search_layout.add_widget(search_btn)
        
        # 3. Map View
        self.mapview = MapView(zoom=11, lat=43.4643, lon=-80.5204)
        
        root.add_widget(search_layout)
        root.add_widget(self.mapview)
        return root

    def search_location(self, *args):
        city_name = self.search_input.text
        if not city_name: return

        # I am using the OpenStreetMap search engine
        url = f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json"
        headers = {'User-Agent': 'VigneTrafficScout/1.0'} # Required by their policy
        
        try:
            response = requests.get(url, headers=headers).json()
            if response:
                # Get the first result's coordinates
                new_lat = float(response[0]['lat'])
                new_lon = float(response[0]['lon'])
                
                # JUMP!
                self.mapview.center_on(new_lat, new_lon)
                self.mapview.zoom = 12
                print(f"🚀 Jumping to {city_name} at {new_lat}, {new_lon}")
            else:
                print(f"❌ Could not find {city_name}")
        except Exception as e:
            print(f"⚠️ Search error: {e}")

if __name__ == '__main__':
    VigneMapApp().run()