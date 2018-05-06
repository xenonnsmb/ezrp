# ezrp
Cross-platform app that lets you create your own custom Discord rich presence!
## How to run
### Easy way
Download the latest compiled version for your platform from the Releases tab.
### From source
Run Run.bat (Windows), Run.command (Mac), or Run.sh (Linux). You will need Python 3 and wxpython installed; if you don't have wxpython, get it with ``pip3 install wxpython``.
### Build it yourself
- On Windows, run ``python3 setup.py py2exe``
- On Mac, run ``python3 setup.py py2app``
## How to use
When ezrp starts, you will be prompted for a client ID; this determines what game name will be shown in Discord. The default client ID will work, but it will make Discord say you are playing "ezrp". If you want to customize this, create your own application at https://discordapp.com/developers/applications/me, give it the name you want, and copy the client ID. Once you've chosen a client ID, the main window will open. Use the dropdown to choose a data source, and click "Start" to begin using your rich presence. Click "Configure" to set options for the current data source.
### List of data sources
- Default Example - Displays "Rich Presence Test" and "Powered by ezrp" as your rich presence. Use this to test ezrp.
- Custom - Allows you to use a customized rich presence. Click "Configure" to customize the data.

More data sources are planned to be added soon!
