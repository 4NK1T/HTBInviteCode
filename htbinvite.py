import requests
import base64
r = requests.post("https://www.hackthebox.eu/api/invite/generate")
c = str(base64.b64decode(r.text[29:69]))
d = str.replace(c, "'", "")
print("This is your invite code ==> " , d[1:30])
