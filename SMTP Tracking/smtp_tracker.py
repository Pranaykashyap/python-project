from scapy.all import *
import logging
from datetime import datetime
from plyer import notification
import sys

try:
    filename = "smtpscan_"+datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p")+".log"
    logging.basicConfig(filename=filename, filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    smtp_port = [25, 587, 465]
    def smtp_scanner(packets):
        for packet in packets:
            if isinstance(packet[2].sport, int) and packet[2].sport in smtp_port:
                if packet.haslayer(Raw) and not None:
                    logging.warning("{}  |  {}  |  {}  |  {}\n".format(packet[1].src, packet[1].dst, packet[2].sport, packet[3].load))
                    now = datetime.now()
                    t_string = now.strftime("%I:%M")
                    notification.notify(title = "SMTP Detected",
                        message="there was a SMPT action Detected at " + t_string,
                        app_icon = None,
                        timeout=15)
      
    sniff(filter="ip", prn=smtp_scanner)
except Exception:
    sys.exit()
