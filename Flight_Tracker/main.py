# Track Flight Position

import requests
import smtplib
from email.message import EmailMessage


avstack_api = "API KEY"
my_email = "EMAIL"
password = "PASSWORD"

url = "https://api.aviationstack.com/v1/flights"

params = {
    'access_key': avstack_api,
    'limit': 50,
    "airline_name": "AIRLINE NAME",
}


response = requests.get("http://api.aviationstack.com/v1/flights", params)
api_response = response.json()
flight_arrival = api_response
dict = []

for arrivals in flight_arrival['data']:
    dict.append(arrivals)



index = (len(flight_arrival))

arrival_airports = []
target_airports = ["CPT", "JNB", "PLZ", "GRJ", "KIM", "DUR", "UTN", "HLA", "ELS", "MQP", "BFN", "PRY", "PTG", "RCB", 
                   "PZB", "MGH", "PHW", "UTT", "QRA", "MBD", "AAM", "AGZ", "SZK", "VIR", "BIY", "NTY", "HDS", "ULD", 
                   "SIS", "ALJ", "ADY", "KLZ", "GCJ", "SBU", "PBZ", "ELL", "LAY", "NLP", "WEL", "HLW", "LLE", "ROD", 
                   "NCS", "OVG", "TCU"]

for airports in range(index):
    flight_arrival = api_response["data"][airports]["arrival"]["iata"]
    arrival_airports.append(flight_arrival)

for i in range(index):
    if arrival_airports[i] in target_airports:
        details = (f"Flight Details: {arrival_airports[i]} \nFlight Date: {api_response['data'][i]['flight_date']} \n\nFlight Status: {api_response['data'][i]['flight_status']}\nEstimated Arrival Date: {api_response['data'][i]['arrival']['estimated']}")
        with open("Flights.txt", mode="a") as f:
            f.write(details)

msg = EmailMessage()
msg['Subject'] = "EQUATORIAL GUINEA FLIGHT DETECTED!"
msg['From'] = my_email
msg['To'] = "danielbooysenjr@gmail.com"
msg.set_content("Please see attached file for flight details.")

with open('Flights.txt', 'rb') as f:
    file_data = f.read()
    file_name = f.name

msg.add_attachment(file_data, maintype='text', subtype='plain', filename=file_name)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.send_message(msg)