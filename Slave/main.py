from Mining_directory import DirectoryStructure
from FetchFile import Fetch_remote_file
from File_diff import Show_diff
from Identiy_handler import IdentityGetters
import configparser

if __name__ == '__main__':
    # Read the config file
    parser = configparser.ConfigParser()
    parser.read('config.ini')

    #Fetch the target device name
    target_device = parser.get('RequiredData', 'TargetDevice')
    get_identities = IdentityGetters(target_device)
    target_ip = get_identities.get_devicenames_ips()

    # Fetch the folder path which you want to sync
    folder_to_scan = parser.get('RequiredData', 'FolderToScan')
    handle_directory_structure = DirectoryStructure(folder_to_scan)
    handle_directory_structure.scan_directory()

    # Fetch the diff text file from master
    remote_dirstruct = Fetch_remote_file(target_ip)
    remote_dirstruct.get_text_file()

    # Fetch remote and local file paths
    RemoteFilePath = parser.get('FilePaths', 'RemoteFile')
    LocalFilePath = parser.get('FilePaths', 'LocalFile')

    #Compare both the text files 
    differentiator = Show_diff(RemoteFilePath,LocalFilePath)
    differentiator.comapre_files()


