import requests
try:
  response = requests.get('http://www.google.com')
except:
  print ('Can\'t connect to Google\'s server')
  input('Press any key to exit.')
  quit()

# use the Google Maps API
import googlemaps
gmaps = googlemaps.Client(key='YOUR_KEY')
origins = (28.61394,77.20902)
destinations = (28.4410664,77.2333789)
matrix = gmaps.distance_matrix(origins, destinations, mode="walking")
print (matrix)
