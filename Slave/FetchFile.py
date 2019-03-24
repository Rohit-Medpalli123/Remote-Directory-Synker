import requests


class FetchRemoteFile:
    def __init__(self,target_ip):
        self.target_ip = target_ip

    def get_text_file(self):
        """This function fetches the text file from the remote machine"""

        try:
            # Generate a file url to fetch the remote file
            target_url = 'http://'+ self.target_ip + ':8000/list_of_files.txt'
            print(target_url)

            # Fetch the remote file
            r = requests.get(target_url,allow_redirects = True)
            print(r.status_code)

            try:
                # Make a local copy of remote file
                with open("remote_DS.txt","w") as RDS:
                    RDS.write(r.content)
            except:
                print("unable to perform operation!! ")

        except:
            print("Unable to get Hostname and IP")

