version = "1.3.0"
from tv import ip_adresa_tv
from tv import tv_name
import os
import sys
from slovnik import tv


# TODO Cold start, failover, change source, picture in picture, teplota bod 7,4, serial number, tailing, lightsensor,
# TODO humansensor, display rotation, dealy on start (tailing), factory reset, fan speed
# TODO Screenshot, teamviewer (android only), RS232 routing, WOL, autorestart, HDMI (onewhire = CEC, timer, Multiwindow)

class Program:
    def __init__(self, ip_adresa_tv, tv_name, cmd):
        self.ip_adresa_tv = ip_adresa_tv
        self.tv_name = tv_name
        self.cmd = cmd
        self.model = self.model_name()

    def model_name(self):
        model = self.tv_name
        model = model.strip()
        model = model.lower()

        if "samsung" in model:
            return "samsung"
        elif "lg" in model:
            return "lg"
        elif "philips" in model:
            return "philips"

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
            print("HDMI - Power is OFF")
            return False
        elif list == On:
            print("HDMI - Power is ON")
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

    def prikaz(self, cmd):
        if self.model == "philips":
            stream_s = "echo " + cmd + " |xxd -r -p|nc -w 1 " + self.ip_adresa_tv + " 5000|xxd -ps"  # TODO kontrola uvozovek u prikazu
            stream = os.popen(stream_s)
            return stream.read()

        elif self.model == "lg":
            stream_s = "echo " + "'" + cmd + "'" + "|nc -w 1 " + self.ip_adresa_tv + " 9761"
            stream = os.popen(stream_s)
            return stream.read()

    def tv_status_ip(self):  # CMD directly to TV
        stream = self.prikaz(tv[self.model]["power_state"]["message_get"]["get"])
        stream = stream.strip()
        if stream.strip() == tv[self.model]["power_state"]["message_get"]["report_on"]:
            print("IP - Power is ON")
            return True
        elif stream == tv[self.model]["power_state"]["message_get"]["report_off"]:
            print("IP - Power is OFF")
            return False
        else:
            print("chyba= " + stream)

    def tv_on_ip(self):
        if self.tv_status_ip():
            print("Televize jiz byla zapnuta")
            pass
        else:
            print("Pokousim se zapnout TV")
            self.prikaz(tv[self.model]["power_state"]["message_set"]["turn_on"])

    def tv_off_ip(self):
        if self.tv_status_ip():
            self.prikaz(tv[self.model]["power_state"]["message_set"]["turn_off"])
            print("Pokousim se vypnout TV")
        else:
            print("Televize jiz byla vyppnuta")
            pass

    def nastav_tv(self):

        if self.model == "samsung":
            print("Samsung - nic nenestavuji")

        elif self.model == "lg":
            print("LG - nastavuji TV")
            stream = self.prikaz(tv["lg"]["power_saving_mode"]["message_set"]["dpm_10s"])
            print(stream)
            stream = self.prikaz(tv["lg"]["power_saving_mode"]["message_set"]["pm_mode"])
            print(stream)
            stream = self.prikaz(tv["lg"]["power_saving_mode"]["message_set"]["wake_on_lan"])
            print(stream)
            stream = self.prikaz(tv["lg"]["power_saving_mode"]["message_set"]["dpm_clk_data"])
            print(stream)

        elif self.model == "philips":
            print("Philips - nastavuji TV")
            stream = self.prikaz(tv["philips"]["power_saving_mode"]["message_set"]["mode_low"])
            print(stream)
            stream = self.prikaz(tv["philips"]["power_saving_mode"]["message_set"]["mode_3"])
            print(stream)

        else:
            # Vyzkouší všechny příkazy
            print("LG - nastavuji TV")
            stream = self.prikaz(tv["lg"]["power_saving_mode"]["message_set"]["dpm_10s"])
            print(stream)
            stream = self.prikaz(tv["lg"]["power_saving_mode"]["message_set"]["pm_mode"])
            print(stream)
            stream = self.prikaz(tv["lg"]["power_saving_mode"]["message_set"]["wake_on_lan"])
            print(stream)
            stream = self.prikaz(tv["lg"]["power_saving_mode"]["message_set"]["dpm_clk_data"])
            print(stream)
            print("Philips - nastavuji TV")
            stream = self.prikaz(tv["philips"]["power_saving_mode"]["message_set"]["mode_low"])
            print(stream)
            stream = self.prikaz(tv["philips"]["power_saving_mode"]["message_set"]["mode_3"])
            print(stream)

    def update(self):
        print("Aktualizuji tv")
        stream2 = os.popen('./update.sh /home/pi/Bluetouch_media_pub/update.sh')
        print(stream2.read())

    def on(self):

        self.tv_on_hdmi()
        if self.tv_status_hdmi():
            print("HDMI ON")
            try:
                if self.tv_status_ip():
                    print("TV po IP je zapnuta a kumunikuje")
                else:
                    self.tv_on_ip()

            except:
                print("nejaka chyba")

        else:
            self.tv_on_hdmi()
            print("nepovedlo se, zkousim to zapnout")

    def off(self):

        self.tv_off_hdmi()
        if self.tv_status_hdmi() == False:
            print("HDMI OFF")
            try:
                if self.tv_status_ip() == False:
                    print("TV po IP je vypnuta ale kumunikuje")
                else:
                    self.tv_off_ip()

            except:
                print("nejaka chyba")

        else:
            print("nepovedlo se")

    def status(self):

        self.tv_status_hdmi()
        self.tv_status_ip()

        ############ Program ##############


command = str(sys.argv[1])

prog = Program(ip_adresa_tv, tv_name, command)

print(prog.cmd)

if prog.cmd == "?" or prog.cmd == "help" or prog.cmd == "h":
    # print("prikaz_philipsy: tv_on_hdmi, tv_off_hdmi, nastav_tv, update")
    print("prikaz_philipsy: tv_on_hdmi, tv_off_hdmi, tv_on_ip, tv_off_ip, nastav_tv, update")
if prog.cmd == "tv_on_hdmi":
    prog.tv_on_hdmi()
if prog.cmd == "tv_off_hdmi":
    prog.tv_off_hdmi()
if prog.cmd == "tv_on_ip":
    prog.tv_on_ip()
if prog.cmd == "tv_off_ip":
    prog.tv_off_ip()
if prog.cmd == "nastav_tv":
    prog.nastav_tv()
if prog.cmd == "update":
    prog.update()
if prog.cmd == "on":
    prog.on()
if prog.cmd == "off":
    prog.off()
if prog.cmd == "status":
    prog.status()


