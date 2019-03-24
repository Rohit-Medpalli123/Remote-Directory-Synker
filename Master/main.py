from Server_settings import HostServer
from Mining_directory import DirectoryStructure
from Identiy_handler import IdentityGetters
import configparser

if __name__ == '__main__':
    #Read the config file
    parser = configparser.ConfigParser()
    parser.read('config.ini')

    #Fetch the target device name
    target_device = parser.get('RequiredData', 'TargetDevice')
    get_identities = IdentityGetters(target_device)
    get_identities.get_Host_name_IP()

    #Fetch the folder path which you want to sync
    folder_to_scan = parser.get('RequiredData', 'FolderToScan')
    handle_directory_structure = DirectoryStructure(folder_to_scan)
    handle_directory_structure.scan_directory()

    #Host the generated text file using httpserver
    port = parser.get('ServerSettings', 'Port')
    handle_server = HostServer(int(port))
    handle_server.turn_on_server()