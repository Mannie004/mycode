# import requests
# import urllib.parse
# from time import strftime, localtime
# import datetime
# # import webbrowser 
# # import geocoder

# city = "Paris"
# country = "France"
# url = "http://api.open-notify.org/iss-now.json "

# resp = requests.get(url)

# data = resp.json()
# print(data)
# status = resp.status_code
# print(status)


# if status == 200:
#     timestamp = data['timestamp']
#     time = strftime('%T', localtime(timestamp))

#     latitude = data['iss_position']['latitude']
#     if float(latitude) > 0:
#         lat_dir = 'N'
#     else:
#         lat_dir = 'S'

#     longitude = data['iss_position']['longitude']
#     if float(longitude) > 0:
#         lon_dir = 'E'
#     else:
#         lon_dir = 'W'

#     print('International Space Station position @ {}'.format(time))
#     print('Latitude: {}° {}'.format(latitude, lat_dir))
#     print('Longitude: {}° {}'.format(longitude, lon_dir))
# else:
#     print('Request unsuccessful: {}'.format(status))



# standard library modules first
import time

# 3rd party modules second
import requests
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"

def main():
    # return API response, turn JSON into a python dictionary
    resp= requests.get(URL).json()

    # pull appropriate values for use later
    lat= resp["iss_position"]["latitude"]
    lon= resp["iss_position"]["longitude"]
    ts= resp["timestamp"]

    # convert epoch time into a human readable format
    hr_ts= time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))

    # return an ordered dictionary using our lat/lon
    locator_resp= rg.search((lat, lon))

    # slice that object to return the city name only
    city= locator_resp[0]["name"]

    # slice the object again to return the country
    country= locator_resp[0]["cc"]

    print(f"""
CURRENT LOCATION OF THE ISS:
Timestamp: {hr_ts}
Lon: {lon}
Lat: {lat}
City/Country: {city}, {country}
""")

if __name__=="__main__":
    main()