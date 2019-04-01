# Remote Directory Synker [![Python 2.7](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

This is a utility written in python 3.Here this script keeps a directory (all folders within them) on a remote device (laptop) in sync so one is a direct copy of the other. Ideal for backing up work both locally and remote.

#### Motivation:
Nothing lasts forever, and digital images can disappear in seconds. People lose their most important photos when hard drives fail, when smartphones and laptops are stolen. If there is one thing I am obsessed with when it comes to technology, it’s my family pictures. I am equally as fanatical about getting them backed up. I have an old windows laptop that I have setup to act as a network attached storage, this machine is used as a backup facility for my personal laptop which has the family pictures, wedding videos, personal documents, family documents, etc.

#### Built With:
- [Python 3](https://www.python.org/download/releases/3.0/)
- [SocketServer](https://docs.python.org/3/library/socketserver.html) - A framework for creating network servers.
- [http.server](http://docs.python-requests.org/en/master/) - To set up a very basic web server serving files relative to the current directory.
- [socket](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - Provides access to the BSD socket interface.
- [email](https://docs.python.org/2/library/email.html#module-email) - Library for sending email messages.
-  [requests](http://docs.python-requests.org/en/master/) - allows you to send organic, grass-fed HTTP/1.1 requests.

#### Steps performed by the Master script are as follows:
1. Scans the source directory which you want to sync with the remote directory. 
2. Writes the directory structure(sub-directories and files) to a text file.
3. Hosts the generated text file using HTTPServer.

#### Steps performed by the Slave script (Remote) are as follows:
1. Scans the source directory which you want to sync.
2. Writes the directory structure(sub-directories and files) to a text file.
3. Fetch the text file from the remote computer (**master**).
4. Compare two text files. 
5. Email the difference between two text files

## Getting Started:

#### Prerequisites:
1. Python 3
2. This project already has pipfile so go ahead and install all the dependencies from it . Use the below command:Install from Pipfile, if there is one: Please refer to [link](https://pipenv.readthedocs.io/en/latest/basics/#example-pipenv-workflow).

 ```bash
 pipenv install
 ```
#### Running the tests:
Please follow the below Steps to run the scripts:
1. Connect the two machines(**Master and Slave** ) either to the wifi network or to LAN
2. Place the Master folder in the Master machine
3. Place the Slave folder in the Slave machine


##### TO DO:
- [x] Report the difference in the directory structure for Sync action.
- [ ] Move files accross the network.
- [ ] Send Email with proper formatting 

##### Note: 
_we have two options for the sending the email_
1. Email module
2. Boto3 

#### How to run the script:
Here we have two options for setup.
1. Set up a _cron job_ daily (**_recommended_**)
2. Run the script manually when it's needed












 



