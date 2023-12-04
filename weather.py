import requests
from bs4 import BeautifulSoup

# kingston     url = 'https://weather.com/weather/today/l/b15381ad1ee97bd0e295a0684e9b8b8a20fdd41dc59e667f151fe2d76a533eaf'
def get_temperature():
    url = 'https://weather.com/weather/today/l/8d3c01aa71b25a3afc3bc9e96d0653a61c481add341f589c9700e7c286e6192e'
    contents = requests.get(url)
    soup = BeautifulSoup(contents.text, 'html.parser')

    rows = soup.find('span', class_='CurrentConditions--tempValue--MHmYY')

    temp = rows.text

    return temp

def get_conditions():
    url = 'https://weather.com/weather/today/l/8d3c01aa71b25a3afc3bc9e96d0653a61c481add341f589c9700e7c286e6192e'
    contents = requests.get(url)
    soup = BeautifulSoup(contents.text, 'html.parser')

    rows = soup.find('div', class_='CurrentConditions--phraseValue--mZC_p')

    conditions = rows.text

    return conditions




