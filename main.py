version = "1.2.2"
from tv import ip_adresa_tv
from tv import tv_name
import os
import sys
from slovnik import philips, lg


# TODO Cold start, failover, change source, picture in picture, teplota bod 7,4, serial number, tailing, lightsensor,
# TODO humansensor, display rotation, dealy on start (tailing), factory reset, fan speed
# TODO Screenshot, teamviewer (android only), RS232 routing, WOL, autorestart, HDMI (onewhire = CEC, timer, Multiwindow)
# TODO rozdeleni televiz podle vyrobce

class Program:
    def __init__(self, ip_adresa_tv, tv_name, cmd):
        self.ip_adresa_tv = ip_adresa_tv
        self.tv_name = tv_name
        self.cmd = cmd

    ### RPI prikaz_philipsy naprimo po HDMI
    def tv_status_hdmi(self):  # On nebo Off (TV service)
        stream = os.popen('tvservice -s')  # stav TV
        self.out_tv_status_hdmi = stream.read()  # Vystup ze stavu
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

    def tv_on_hdmi(self):  # zapni televizi ale nejdriv zkontroluj jeji stav
        if self.tv_status_hdmi():
            print("pass")
            print(self.out_tv_status_hdmi)
            pass
        else:
            print("zapinam tv")
            stream2 = os.popen('tvservice -p')
            print(stream2.read())

    def tv_off_hdmi(self):  # vypni televizi ale nejdriv zkontroluj jeji stav
        if self.tv_status_hdmi():
            print("vypinamm tv")
            stream2 = os.popen('tvservice -o')
            print(stream2.read())
        else:
            print("pass")
            print(self.out_tv_status_hdmi)
            pass

    ### prikaz_philipsy primo do televize (IP)

    def prikaz_philips(self, cmd_p):
        stream_s = "echo " + cmd_p + " |xxd -r -p|nc -w 1 " + self.ip_adresa_tv + " 5000|xxd -ps"
        stream = os.popen(stream_s)
        return stream.read()

    def prikaz_lg(self, cmd_p):
        stream_s = "echo " + "'" + cmd_p + "'" + "|nc -w 1 " + self.ip_adresa_tv + " 9761"
        stream = os.popen(stream_s)
        return stream.read()

    def tv_status_ip(self):  # CMD directly to TV
        stream = self.prikaz_philips(philips["power_state"]["message_get"]["get"])
        stream = stream.strip()
        if stream == philips["power_state"]["message_get"]["report_on"]:
            print("Power is ON")
            return True
        elif stream == philips["power_state"]["message_get"]["report_off"]:
            print("Power is OFF")
            return False
        else:
            print("chyba= " + stream)

    def tv_on_ip(self):
        if self.tv_status_ip():
            print("Televize již byla zapnutá")
            pass
        else:
            print("Zapínám TV")
            self.prikaz_philips(philips["power_state"]["message_set"]["turn_on"])

    def tv_off_ip(self):
        if self.tv_status_ip():
            self.prikaz_philips(philips["power_state"]["message_set"]["turn_off"])
            print("Vypínám TV")
        else:
            print("Televize již byla vyppnutá")
            pass

    def tv_status_power_saving_mode(self):  # CMD directly to TV
        stream = self.prikaz_philips(philips["power_saving_mode"]["message_get"]["get"])
        print(stream)

        # if stream == philips["power_state"]["message_get"]["report_on"] :
        #     print("Power is ON")
        #     return True
        # elif stream == philips["power_state"]["message_get"]["report_off"]:
        #     print("Power is OFF")
        #     return False
        # else:
        #     print(f'chyba= {stream}')

    def nastav_tv(self):
        '''Spravne nastaveni televize pro uspavani cronem'''
        model = self.tv_name
        model = model.strip()
        model = model.lower()

        if "samsung" in model:
            print("Samsung - nic nenestavuji")

        elif "lg" in model:
            print("LG - nastavuji TV")
            stream = self.prikaz_lg(lg["power_saving_mode"]["message_set"]["dpm_10s"])
            print(stream)
            stream = self.prikaz_lg(lg["power_saving_mode"]["message_set"]["pm_mode"])
            print(stream)
            stream = self.prikaz_lg(lg["power_saving_mode"]["message_set"]["wake_on_lan"])
            print(stream)
            stream = self.prikaz_lg(lg["power_saving_mode"]["message_set"]["dpm_clk_data"])
            print(stream)

        elif "philips" in model:
            print("Philips - nastavuji TV")
            stream = self.prikaz_philips(philips["power_saving_mode"]["message_set"]["mode_low"])
            print(stream)
            stream = self.prikaz_philips(philips["power_saving_mode"]["message_set"]["mode_3"])
            print(stream)

        ############ Program ##############


command = str(sys.argv[1])

tv = Program(ip_adresa_tv, tv_name, command)

print(tv.cmd)

if tv.cmd == "?" or tv.cmd == "help" or tv.cmd == "h":
    print("prikaz_philipsy: tv_on_hdmi, tv_off_hdmi, tv_on_ip, tv_off_ip, nastav_tv")
if tv.cmd == "tv_on_hdmi":
    tv.tv_on_hdmi()
if tv.cmd == "tv_off_hdmi":
    tv.tv_off_hdmi()
if tv.cmd == "tv_on_ip":
    tv.tv_on_ip()
if tv.cmd == "tv_off_ip":
    tv.tv_off_ip()
if tv.cmd == "nastav_tv":
    tv.nastav_tv()


