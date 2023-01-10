version = "1.3.4"
from tv import ip_adresa_tv
from tv import tv_name
import os
import sys
from slovnik import tv


# TODO Cold start, failover, change source, picture in picture, teplota bod 7,4, serial number, tailing, lightsensor,
# TODO humansensor, display rotation, dealy on start (tailing), factory reset, fan speed
# TODO Screenshot, teamviewer (android only), RS232 routing, autorestart, Multiwindow)

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


################################### STATUS TV ################################## 


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
            print("IP - Neznam stav TV po IP")

    def tv_status_cec(self):  # On nebo Off (CEC)
        stream = os.popen("echo 'pow 0.0.0.0' | cec-client -s -d 1")  # stav TV
        self.out_tv_status_cec = stream.read()  # Vystup ze stavu
        # print(self.out_tv_status_cec[-3:])
        status = self.out_tv_status_cec.split("power status:")[-1]
        status = status.strip()

        if status == "on":
            print("CEC - Power is ON")
            return True 
        elif status == "standby":
            print("CEC - Power is OFF")
            return False
        else:
            print("Neznam stav TV po CEC, ignoruji prikaz")
        
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
            
################################### END STATUS TV ##################################           

################################### ON/OFF TV ################################## 

    def tv_on_hdmi(self):  # zapni televizi ale nejdriv zkontroluj jeji stav
        status = self.tv_status_hdmi()
        if status:
            print("Televize je jiz zapnuta pres HDMI")
            print(self.out_tv_status_hdmi)
            pass
        
        elif status == False:
            print("Zapinam TV pres HDMI")
            stream2 = os.popen('tvservice -p')
            print(stream2.read())

    def tv_off_hdmi(self):  # vypni televizi ale nejdriv zkontroluj jeji stav
        status = self.tv_status_hdmi()
        if status:
            print("Vypinamm TV pres HDMI")
            stream2 = os.popen('tvservice -o')
            print(stream2.read())
            
        elif status == False:
            print("Televize je jiz vypnuta pres HDMI")
            print(self.out_tv_status_hdmi)
            pass
            
#################################################################################### 

    def tv_on_ip(self):
        status = self.tv_status_ip()
        if status:
            print("Televize jiz byla zapnuta pres IP")
            pass
        
        elif status == False:
            print("Pokousim se zapnout TV")
            self.prikaz(tv[self.model]["power_state"]["message_set"]["turn_on"])
            
        else:
            print("Neznam stav TV po IP, ignoruji prikaz")
            pass

    def tv_off_ip(self):
        status = self.tv_status_ip()
        if status:
            self.prikaz(tv[self.model]["power_state"]["message_set"]["turn_off"])
            print("Pokousim se vypnout TV")
            
        elif status == False:
            print("Televize jiz byla vyppnuta")
            pass
                    
        else:
            print("Chyba, neznamy TV stav po IP, ignoruji prikaz")
            pass

#################################################################################### 

    def tv_on_cec(self):
        
        status = self.tv_status_cec()
        if status: 
            print("Televize jiz byla zapnuta pres CEC")
            pass
            
        elif status == False:
            print("Zapinamm TV pres CEC")
            stream2 = os.popen("echo 'on 0.0.0.0' | cec-client -s -d 1")
            print(stream2.read())
            
        else:
            print("Nepovedlo se mi zapnout TV pres CEC")
        
    def tv_off_cec(self):

        status = self.tv_status_cec()
        if status:  
            print("Vypinamm TV pres CEC")
            stream2 = os.popen("echo 'standby' 0.0.0.0 | cec-client -s -d 1")
            print(stream2.read())
            
        elif status == False:
            print("Televize jiz byla vyppnuta pres CEC")
            pass
            
        
        else:
            print("Nepovedlo se mi vypnout TV pres CEC")
            
 
################################### ON/OFF TV ##################################          

    def on(self):

        try: 
            print("Pokousim se zapnout TV pres HDMI")
            self.tv_on_hdmi()
        except:
            print("Nepovedlo se mi zapnout TV pres HDMI")
            
        try: 
            print("Pokousim se zapnout TV po IP")
            self.tv_on_ip()
        except:
            print("Nepovedlo se mi zapnout TV po IP")
            
        try: 
            print("Pokousim se zapnout TV po CEC")
            self.tv_on_cec()
        except:
            print("Nepovedlo se mi zapnout TV po CEC")



    def off(self):

        try: 
            print("Pokousim se vypnout TV pres HDMI")
            self.tv_off_hdmi()   
        except:
            print("Nepovedlo se mi vypnout TV pres HDMI")
        
        try: 
            print("Pokousim se vypnout TV po IP")
            self.tv_off_ip()
        except:
            print("Nepovedlo se mi vypnout TV po IP")
            
        try: 
            print("Pokousim se vypnout TV po CEC")
            self.tv_off_cec()
        except:
            print("Nepovedlo se mi vypnout TV po CEC")
            
            
################################### END ON/OFF TV ##################################


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


    def update(self):
        print("Aktualizuji tv")
        stream2 = os.popen('./update.sh /home/pi/Bluetouch_media_pub/update.sh')
        print(stream2.read())

    def status(self):

        self.tv_status_hdmi()
        self.tv_status_ip()
        self.tv_status_cec()



############ Program ##############


command = str(sys.argv[1])

prog = Program(ip_adresa_tv, tv_name, command)

print(prog.cmd)

if prog.cmd == "?" or prog.cmd == "help" or prog.cmd == "h":
    print("BTM v: " + version)
    print("Prikazy: on, off, nastav_tv, update, status")
    
# if prog.cmd == "tv_on_hdmi":
#     prog.tv_on_hdmi()
# if prog.cmd == "tv_off_hdmi":
#     prog.tv_off_hdmi()
# if prog.cmd == "tv_on_ip":
#     prog.tv_on_ip()
# if prog.cmd == "tv_off_ip":
#     prog.tv_off_ip()
# if prog.cmd == "tv_on_cec":
#     prog.tv_on_cec()
# if prog.cmd == "tv_off_cec":
#     prog.tv_off_cec()

if prog.cmd == "nastav_tv":
    prog.nastav_tv()
if prog.cmd == "update":
    prog.update()
if prog.cmd == "status":
    prog.status()
if prog.cmd == "on":
    prog.on()
if prog.cmd == "off":
    prog.off()




