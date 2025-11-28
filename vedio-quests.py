import requests
import time
import random

EMAIL = "UR EMAIL"
PASSWORD = "UR PASSWORD"
QUEST_URL = input(" Enter Quest Link -> ")

QUEST_ID = QUEST_URL.split('/')[-1]
SUPER = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiaGFzX2NsaWVudF9tb2RzIjpmYWxzZSwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgRGlzY29yZC8xLjAuMCBDaHJvbWUvMTIwLjAuMC4wIEVsZWN0cm9uLzI4LjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMjguMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmVfY3VycmVudCI6Imdvb2dsZSIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjQ3MjkxNCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiY2xpZW50X2xhdW5jaF9pZCI6IjQyNmM2MzdmLTNjZGQtNDAwOS05YjU0LTdmMDg1MTdhOWRjYSIsImxhdW5jaF9zaWduYXR1cmUiOiIzMDA5ZTEyYS03NzJhLTQ3MzgtOGYwYS1hODk5ZWE2N2I3YWQiLCJjbGllbnRfaGVhcnRiZWF0X3Nlc3Npb25faWQiOiJkNjBmNzE4NC1lODA1LTQ5YjItYTQ0NCM2MzI4NTY5NmI2MWIiLCJjbGllbnRfYXBwX3N0YXRlIjoiZm9jdXNlZCJ9'

res = requests.post("https://discord.com/api/v9/auth/login", 
    json={'login': EMAIL, 'password': PASSWORD, 'undelete': False},
    headers={'User-Agent': "Discord-Android/306013;RNA", 'Content-Type': "application/json"})
TOKEN = res.json()['token']
print(f" Ur Token :  {TOKEN}")

requests.post(f"https://discord.com/api/v9/quests/{QUEST_ID}/enroll",
    json={'location': 11, 'is_targeted': False, 'metadata_raw': None},
    headers={'authorization': TOKEN, 'x-super-properties': SUPER})
print(f" - Accept Quest {QUEST_ID}")

t = 0
while True:
    t += random.uniform(0.5, 40)
    try:
        r = requests.post(f"https://discord.com/api/v9/quests/{QUEST_ID}/video-progress",
            json={'timestamp': t},
            headers={'authorization': TOKEN, 'content-type': 'application/json', 'x-super-properties': SUPER})

        print(f"{t:.1f}s - just wait..{r.status_code}")

        if '"message": "400: Bad Request", "code": 0' in r.text or "400" in r.text:

            t = 0
            continue

        if '"completed_at":null' not in r.text and 'completed_at' in r.text:
            print("Quest complet!")
            break

    except:
        pass
        time.sleep(1)
