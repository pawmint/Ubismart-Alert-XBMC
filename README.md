# Ubismart Alert XBMC

XBMC add-on: Display a custom alert dialog to XBMC, from a JSON-RPC request.

# Install

Run XBMC, go to Settings>Services>Webserver and tick *Allow control of XBMC via HTTP*, on port 8080, with no username/password
Copy this folder in your $HOME/.xbmc/addons directory.

# Run an alert

Assuming you are testing on localhost, run the following command (you may change the text in line1 and line2):
```bash
$ curl -i http://localhost:8080/jsonrpc -X POST -H "Content-Type: application/json" -d '{"jsonrpc": "2.0", "id": 1, "method": "Addons.ExecuteAddon", "params": { "addonid": "plugin.program.helloworld_gui", "params": { "line1": "Mr. Endelin", "line2": "It is time to take your medications" } } }'
```

# Develop

Follow the [XBMC README](https://github.com/xbmc/xbmc/blob/master/docs/) to compile it on your local folder (unless you want to test on your system-wide install).

```bash
$ cd $MY_XBMC_FOLDER
$ git submodule add https://github.com/pawmint/Ubismart-Alert-XBMC.git addons/plugin.program.ubismartalert
```

To run XBMC with your local config (rather than the system-wide config):
```bash
$ ./xbmc.bin -p
```
