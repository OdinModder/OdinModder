import requests
import os
import time

os.system('clear')
print('\033[01;35mSeja Bem Vindo Consulta IP By:OdinModder ϟ')
print('\033[01;36m=========================================')
ip = input('\033[01;34m>>> ')

r = requests.get('http://ip-api.com/json/{}'.format(ip));data = r.json( )
print('\033[01;33mConsulta Realizada!!')
print( )
print("IP: {}".format(data['query']))
print("Status: {}".format(data['status']))
print("País: {}".format(data['country']))
print("Código_País: {}".format(data['countryCode']))
print("Código_Região: {}".format(data['region']))
print("Nome_Região: {}".format(data['regionName']))
print("Cidade: {}".format(data['city']))
print("Zip: {}".format(data['zip']))
print("Lat: {}".format(data['lat']))
print("Lon: {}".format(data['lon']))
print("TimeZone: {}".format(data['timezone']))
print("Isp: {}".format(data['isp']))
print("Org: {}".format(data['org']))
print("As: {}".format(data['as']))
print("\033[01;32mby:OdinModder ϟ\n")

back = str(input("\n\033[0mnova consulta?[\033[32mS\033[0m/\033[31mN\033[0m]: "))

while back == "s" or back == "S":
	back = str(input("\n\033[0mnova consulta?[\033[32mS\033[0m/\033[31mN\033[0m]: "))