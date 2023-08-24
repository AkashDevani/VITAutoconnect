import urllib.parse
path=input("the path where the file will be saved")
path=path+"\\autoconnect1.bat"
myBat = open(path ,'w+')
username=input("enter username")
password=urllib.parse.quote(input("enter password"))
password=password.replace('%','%'+'%')
myBat.write("@echo off\nnetsh wlan connect ssid=VIT5G name=VIT5G\ntimeout /t 2 \ncurl -X POST -d \"userId="+username+"&password="+password+"&serviceName=ProntoAuthentication&Submit22=Login\" " "\"http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://captive.apple.com/hotspot-detect.html\""+"\npause")
myBat.close()