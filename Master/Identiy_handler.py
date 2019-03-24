# Importing socket library
import socket


class IdentityGetters:
    """This class handles the Master and Slave devices"""
    def __init__(self,target_device):
        self.target_device = target_device

    def get_Host_name_IP(self):
        """This function display's hostname,target name and their IP addresses"""
        try:
            self.host_name = socket.gethostname()
            self.host_ip = socket.gethostbyname(self.host_name)
            self.target_ip = socket.gethostbyname(self.target_device)  # IP adress of remote computer
            print("**************************************************")
            print("Master :  ", self.host_name)
            print("Master IP Address : ", self.host_ip)
            print("Slave : " + self.target_device)
            print("Slave IP Address: ",self.target_ip)
            print("**************************************************")


        except:
            print("Unable to get Hostname and IP")
