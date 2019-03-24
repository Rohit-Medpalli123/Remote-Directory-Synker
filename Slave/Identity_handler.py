# Importing socket library
import socket


class IdentityGetters:
    """This class handles the host and target device"""
    def __init__(self,target_device):
        self.target_device = target_device

    def get_devicenames_ips(self):
        """This function display's hostname,target name and IP addresses"""
        try:
            self.host_name = socket.gethostname()
            self.host_ip = socket.gethostbyname(self.host_name)
            self.target_ip = socket.gethostbyname(self.target_device)  # IP adress of remote computer
            print("**************************************************")
            print("Slave :  ", self.host_name)
            print("Slave IP Address : ", self.host_ip)
            print("Master : " + self.target_device)
            print("Master IP Address: ",self.target_ip)
            print("**************************************************")
            return self.target_ip

        except:
            print("Unable to get Hostname and IP")