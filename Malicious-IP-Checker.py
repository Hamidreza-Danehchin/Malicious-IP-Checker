import tkinter as tk
from tkinter import messagebox
import pip._vendor.requests
import json
import datetime

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/check'

time_report = datetime.datetime.now().strftime("[%a, %d %b %Y] [%H:%M:%S]")

def gui_for_checking_ip_address_in_abuseipdb():
    # Create the main window
    window = tk.Tk()
    window.title("Check input IP with AbuseIPDB.com")
    window.resizable(False, False)

    # Calculate the x and y coordinates to center the window
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_reqwidth()) / 2
    y = (screen_height - window.winfo_reqheight()) / 2

    # Set the position of the window to the center of the screen
    window.geometry("+%d+%d" % (x, y))

    # ################ Create the Label & Entry objects ###################

    # 'attacker_ipaddress_label'
    attacker_ipaddress_label = tk.Label(window, text="Attacker IP Address", font=("TimesNewRoman", 14))
    attacker_ipaddress_label.grid(row=2, column=0, padx=5, pady=30)
    # 'attacker_ipaddress_entry'
    attacker_ipaddress_entry = tk.Entry(window, width=17, font=("TimesNewRoman", 14, "bold"), fg="red")
    attacker_ipaddress_entry.grid(row=2, column=1, padx=5, pady=30)

    # 'check_button_is_clicked()' function
    def check_button_is_clicked():
  
        ipadd = attacker_ipaddress_entry.get()
        querystring = {
         'ipAddress': ipadd,
         'maxAgeInDays': '90'
        }

        headers = {
            'Accept': 'application/json',
            'Key': 'received key from abuseipdb.com'
        }
        response = pip._vendor.requests.request(method='GET', url=url, headers=headers, params=querystring)

        # Formatted output
        decodedResponse = json.loads(response.text)
        #decodedResponse = response.json()
        if "data" in decodedResponse:
            ip_data = decodedResponse["data"]
            #country = ip_data["countryName"]
            IP_Address = ip_data["ipAddress"]
            country_Code = ip_data["countryCode"]
            confidence_score = ip_data["abuseConfidenceScore"]
            score = ip_data["totalReports"]
            
        messagebox.showerror(
        "Malicious IP Checker", "Report Time: "f"{time_report}\n\n" "IP: "
        f"{IP_Address}\n\n" "Country Code: "f"{country_Code}\n\n" "Confidence Score: "f"{confidence_score}\n\n" "Total Reports: "f"{score}\n\n")

    # Bind the <Return> event to the 'block_button_is_clicked' function
    window.bind('<Return>', lambda event=None: check_button_is_clicked())

    # holds 'block_button' & 'unblock_button' objects
    frame_holding_buttons = tk.Frame(window)
    frame_holding_buttons.grid(row=3, column=1)

    # Create 'check_button'
    check_button = tk.Button(frame_holding_buttons, text="Check IP", font=("TimesNewRoman", 16), height=1, width=11,
                             relief="raised", activebackground="red", command=check_button_is_clicked)
    check_button.pack(side=tk.LEFT, padx=20, pady=10)

    # Start the main event loop
    window.mainloop()
gui_for_checking_ip_address_in_abuseipdb()
