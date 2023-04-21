import requests
from bs4 import BeautifulSoup

"""Solution 1"""
# enter city name
city = "gebze"

# creating url and requests instance
url = "https://www.google.com/search?q=" + "weather" + city
html = requests.get(url).content

# getting raw data
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str1 = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

#print(str1)
# formatting data
data = str1.split('\n')
#print(data)
time = data[0]
sky = data[1]

# getting all div tag
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
strd = listdiv[5].text

# getting other required data
pos = strd.find('Wind')
other_data = strd[pos:]

# printing all data
print("Temperature is", temp)
print("Time: ", time)
print("Sky Description: ", sky)
print(other_data)

"""Solution 2"""
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
def find_weather(city_name):
    city_name = city_name.replace(" ", "+")

    try:
        res = requests.get(f'https://www.google.com/search?q={city_name}&oq={city_name}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)

        print("Loading...")

        soup = BeautifulSoup(res.text, 'html.parser')
        location = soup.select('#wob_loc')[0].getText().strip()
        time = soup.select('#wob_dts')[0].getText().strip()
        info = soup.select('#wob_dc')[0].getText().strip()
        temperature = soup.select('#wob_tm')[0].getText().strip()
        print("Location: " + location)
        print("Temperature: " + temperature + "&deg;C")
        print("Time: " + time)
        print("Weather Description: " + info)
    except:
        print("Please enter a valid city name")

city_name = input("Enter City Name: ")
city_name = city_name + " weather"
find_weather(city_name)
