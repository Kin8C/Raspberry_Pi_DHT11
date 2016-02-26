import Adafruit_DHT as dht
h,t = dht.read_retry(dht.DHT22, 4)
f = t/10
hu = h/10

c = ((f-32)/9)*5
archivoTemperatura = open("/home/pi/Documents/urbaneyes/temperatura.kin", "w")
archivoTemperatura.write('{0:1.2f}'.format(c))
archivoTemperatura.close()

archivoHumedad = open("/home/pi/Documents/urbaneyes/humedad.kin", "w")
archivoHumedad.write('{0:0.1f}'.format(hu))
archivoHumedad.close()

