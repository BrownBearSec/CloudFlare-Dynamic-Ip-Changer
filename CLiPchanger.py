import requests

myIP = requests.get("https://ident.me")
myIP = myIP.text
token = "REDACTED"
headers = {"X-Auth-Email": "REDACTED", "X-Auth-Key": token}
data = {"type":"A", "name": "ip.josephwitten.com", "content": myIP, "ttl": 1}

#gets a list of records so you can find record id
records = requests.get("https://api.cloudflare.com/client/v4/zones/REDACTED ZONE ID/dns_records/", headers=headers)
#print(records.text)

#changes dns
response = requests.put("https://api.cloudflare.com/client/v4/zones/REDACTED ZONE ID/dns_records/REDACTED RECORD ID", headers=headers, json=data)
print(response.text)