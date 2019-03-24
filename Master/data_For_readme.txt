how to keep two folders (and all folders within them) in sync so one is a direct copy of the other. Ideal for backing up work both locally, to a cloud/network server or a USB drive.

I have an old windows computer that I have setup acting as a server for various functions, one of which is a cheap network attached storage which acts as both a media server and backup to all my family's computer data.

As my family all like to work locally on their PCs, we needed an easy way to backup our data regularly.

Therefore with a small bit of effort, I wrote a python script which would sync the folders we all needed. I could then customise and distribute this to the family as an executable which I could set windows to run on a regular basis in the background. The computer user had to be none the wiser.

Step 4: Running Automatically
You are now ready to sync any folders without having to copy, paste and delete repeatedly by just double clicking on the executable. But we want to go a step further than that and have Windows run the process automatically so you do not need to worry.

To do this we will use the Task Scheduler program that comes with Windows, this process is based on Windows 10 but is almost identical on other Windows platforms.

Open up the Task Scheduler from the start menu.
On the right hand side select 'Create Task' from the menu.
Give it a name and description and at the bottom make sure it is configured for the right operating system.
On the 'Triggers' tab, create a new trigger by clicking on 'New' on the bottom left, on the new pop up select the configuration you want, I chose to begin the task at Log on and repeat every hour so I know I have a backup of my work every hour. Click OK.
On the 'Actions' tab create a new action in the same way. The action we need is to start a program which is the default. Browse to the executable we created earlier and select. NOTE :- if you move the executable after creating the task, the task and therefore the sync will not complete.
On the 'Conditions' tab de-check the power settings so it will run on battery as well as plugged in.
Click OK and you have now created your task.
Restart the computer and after a while check the target folder location and see that the sync worked, please note if you have a large folder, the sync may take a while to copy all the folders across the first time.

Using DirSync Pro you can make incremental backups. In this way you'll spare lots of time because you don't have to copy all the files each time you want to update your backup; only new/modified/larger files would be copied.


I have various files that download to my computer automatically. They arrive at different times of the day or night. When they do, I like to transfer them to a network drive on another computer automatically.