from influxdb import InfluxDBClient

#connection
client = InfluxDBClient(host='localhost', port=8086)

#show all db
db = client.get_list_database()
print(db)

#switch do db
switch = client.switch_database('testDB')

#select all
data = client.query('SELECT * FROM "temperature"')
print(data.raw)

