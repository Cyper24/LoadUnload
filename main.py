# Creator: XXiv
import pandas as pd
import requests
import os

clear = lambda: os.system('cls')
clear()

url = "https://jmsgw.jntexpress.id/transportation/trackingDeatil/loading/scan/list"
headers = {
        "cookie": "HWWAFSESID=x; HWWAFSESTIME=x",
        "authtoken": "input authtoken",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"}

with open("listkt.txt") as f:
    lines = [line.rstrip('\n') for line in f]
    
list = []
for kt in lines:
    print("=====================================")
    print(kt)
    unload = []
    querystring = {"shipmentNo":f"{kt}"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    r=response.json()
    for lo in r["data"]:
        if lo["scanNetworkCode"] == "SOC999" and lo["loadingTypeName"] == "1":
            valuelo = lo["scanWaybillNum"]
            valuelo = int(valuelo)
            print(f"Total Load: {valuelo}")
        else:
                value = 0

    for unl in r["data"]:
        
        if unl["loadingTypeName"] == "2":
                valueunl = unl["scanWaybillNum"]
                valueunl = int(valueunl)
                unload.append(valueunl)
        else:
                value = 0
    un = sum(unload)
    print(f"Total Unload: {un}")
    final = {'Kode Tugas' : kt,'Load' : valuelo,'Unload':un}
    list.append(final)
    df = pd.DataFrame(list)
    df.to_csv('jnt.csv')
else:
    print("Done")
