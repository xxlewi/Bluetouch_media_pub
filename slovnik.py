version = "1.3.1"

tv = {
    "philips": {
        "power_state": {
            "message_get": {
                "get": "050100191D",
                "report_on": "06010119021d",  # pozor změnila se tam skupina z 00 na 01 - možná to budu parsovat
                "report_off": "06010119011e"
            },
            "message_set": {
                "turn_on": "06010018021D",
                "turn_off": "06010018011E"
            }
        },
        "power_saving_mode": {
            "message_get": {
                "get": "050100D3D7",
                "mode_1": "060101d304d1",
                "mode_2": "060101d305d0",
                "mode_3": "060101d306d3",
                "mode_4": "060101d307d2"
            },
            "message_set": {
                "mode_low": "060100DD01DB",  # ok stejny jako je OFF
                "mode_1": "060101d204d0",
                "mode_2": "060101d205d1",
                "mode_3": "060101d206d2",
                "mode_4": "060101d207d3"
            }
        }
    },
    
    "samsung": {
        "power_state": {
            "message_get": {
                "get": "",
                "report_on": "", 
                "report_off": ""
            },
            "message_set": {
                "turn_on": "",
                "turn_off": ""
            }
        },
        "power_saving_mode": {
            "message_get": {
                "get": "",
                "mode_1": "",
                "mode_2": "",
                "mode_3": "",
                "mode_4": ""
            },
            "message_set": {
                "mode_low": "",
                "mode_1": "",
                "mode_2": "",
                "mode_3": "",
                "mode_4": ""
            }
        }
    },
    
    "lg": {
        "power_state": {
            "message_get": {
                "get": "sv 00 03 FF",  # 46. Status check
                "report_on": "v 01 OK0300x",
                "report_off": "v 01 OK0304x"
            },
            "message_set": {  # 1. Power
                "turn_on": "ka 00 02",
                "turn_off": "mc 00 08"
            }
        },
        "power_saving_mode": {
            "message_set": {
                "dpm_10s": "fj 00 02",  # 39 DPM 10s
                "pm_mode": "sn 00 0c 04",  # 48 PM Mode
                "wake_on_lan": "fw 00 01",  # 52 Wired Wake on lan
                "dpm_clk_data": "sn 00 0b 01",  # 83. DPM Wake Up Control
            },
            "select_input": {
                "message_get": {

                },
                "message_set": {
                    "hdmi_1": "xb 00 90",
                    "hdmi_2": "xb 00 91",
                }
            }
        }

    }
}


