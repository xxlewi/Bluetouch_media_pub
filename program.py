version = "1.0.0"
from ipaddress import ip_address
import os
import sys
from slovnik import slovnik
from tv_ip import ip

# TODO Cold start, failover, change source, picture in picture, teplota bod 7,4, seriál number, tailing, lightsensor,
# TODO humansensor, display rotation, dealy on start (tailing), factory reset, fan speed
# TODO Screenshot, teamviewer (android only), RS232 routing, WOL, autorestart, HDMI (onewhire = CEC, timer, Multiwindow)
# TODO

class Program:
    def __init__(self, ip, cmd):
        self.ip = ip
        self.cmd = cmd

    ### RPI příkazy napřímo po HDMI
    def tv_status_hdmi(self): # On nebo Off (TV service)
        stream = os.popen('tvservice -s') #stav TV
        self.out_tv_status_hdmi = stream.read() # Výstup ze stavu
        Off = ['0', 'x', '2']
        On = ['0', 'x', 'a']
        list = []
        index = 0
        for x in self.out_tv_status_hdmi:
            if index == 6 or index == 7 or index == 8:
                list.append(x)
            index += 1
        if list == Off:
            print("Offline")
            return False
        elif list == On:
            print("Online")
            return True
        else:
            print(self.out_tv_status_hdmi)

    def tv_on_hdmi(self): # zapni televizi ale nejdřív zkontroluj její stav
        if self.tv_status_hdmi():
            print("pass")
            print(self.out_tv_status_hdmi)
            pass
        else:
            print("zapínám tv")
            stream2 = os.popen('tvservice -p')
            print(stream2.read())

    def tv_off_hdmi(self):
        if self.tv_status_hdmi():
            print("vypínám tv")
            stream2 = os.popen('tvservice -o')
            print(stream2.read())
        else:
            print("pass")
            print(self.out_tv_status_hdmi)
            pass


    ### Příkazy přímo do televize (IP)
    def prikaz(self, cmd_p):
        stream = os.popen(f"echo '{cmd_p}'|xxd -r -p|nc -w 1 {self.ip} 5000|xxd -ps")
        return stream.read()

    def tv_status_ip(self): # CMD directly to TV
        stream = self.prikaz(slovnik["power_state"]["message_get"]["get"])
        stream = stream.strip()
        if stream == slovnik["power_state"]["message_get"]["report_on"] : 
            print("Power is ON")
            return True
        elif stream == slovnik["power_state"]["message_get"]["report_off"]:
            print("Power is OFF")
            return False
        else:
            print(f'chyba= {stream}')

    def tv_on_ip(self):
        if self.tv_status_ip():
            print("Televize již byla zapnutá")
            pass
        else:
            print("Zapínám TV")
            self.prikaz(slovnik["power_state"]["message_set"]["turn_on"])
        

    def tv_off_ip(self):
        if self.tv_status_ip():
            self.prikaz(slovnik["power_state"]["message_set"]["turn_off"])
            print("Vypínám TV")
        else:
            print("Televize již byla vyppnutá")
            pass





############ Program ##############

####### Argumenty PROD #######

# ip_address = str(sys.argv[1])
# ip_address = "10.122.0.29"
ip_address = ip
command = str(sys.argv[1])

####################


# tv = Program("", "tv_on_ip") ### DEV
tv = Program(ip_address, command) ### PROD

if tv.cmd == "?" or tv.cmd == "help" or tv.cmd == "h":
    print(f"tv_on_hdmi, tv_off_hdmi, tv_on_ip, tv_off_ip")
if tv.cmd == "tv_on_hdmi":
    tv.tv_on_hdmi()
if tv.cmd == "tv_off_hdmi":
    tv.tv_off_hdmi()
if tv.cmd == "tv_on_ip":
    tv.tv_on_ip()
if tv.cmd == "tv_off_ip":
    tv.tv_off_ip()

