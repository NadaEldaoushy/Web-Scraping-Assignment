import requests , json , csv , time

url = 'http://api.weatherstack.com/current?access_key=cce43aa3a3de500cc32c5df0e67c9408&query=Cairo'
response = requests.get(url)
json_response = json.loads(response.text)

with open ('weather.csv','w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=['Weather','Humidity','Visibility','Pressure','Wind Speed'])
    writer.writeheader()

    for i in range(10):
        descriptions = json_response['current']
        weather = descriptions['weather_descriptions'][0]
        humidity = descriptions['humidity']
        visibility = descriptions['visibility']
        pressure = descriptions['pressure']
        wind_speed = descriptions['wind_speed']
        writer.writerow({'Weather':weather,'Humidity':humidity,'Visibility':visibility,'Pressure':pressure,'Wind Speed':wind_speed})
        
        time.sleep(3)