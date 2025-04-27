import requests
import yaml
import os
import subprocess

def processIP(response):
    responseList = response.text.splitlines()
    remoteAddr = responseList[4]
    ipList = remoteAddr.split(":")
    ipAddr = ipList[1]
    ipAddr = ipAddr.strip()
    return ipAddr

def compareIP(currentIP, settingsDict):
    if currentIP != settingsDict["wanIP"]:
        settingsDict["wanIP"] = currentIP
        updateAndSendSettings(settingsDict)

def updateAndSendSettings(settingsDict):
    with open(settingsFile, 'w') as file:
        yaml.dump(settingsDict, file)
        p = subprocess.Popen(["scp", settingsFile, "zyzyx@barqu.xyz:/home/zyzyx/test.txt"])
        sts = os.waitpid(p.pid, 0)

settingsFile = os.path.join(os.getcwd(), "settings.yml")
with open(settingsFile, 'r') as file:
    settingsDict = yaml.safe_load(file)
    currentIP = processIP(requests.get(settingsDict["sourceURL"]))
    compareIP(currentIP, settingsDict)