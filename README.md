# WifiModule
A dead simple module to control wireless network on MacOs in python.
Given methods use terminal commands in background to control the wifi network.


## Methods

following methods are available to control wifi network on MacOs

### turn_wifi_off()
To turn off the wifi call function turn_wifi_off()
```python
turn_wifi_off()
```

function returns a list with 1 element that is returncode from terminal

### turn_wifi_on()
To turn on the wifi call function turn_wifi_on()
```python
turn_wifi_on()
```

function returns a list with 1 element that is returncode from terminal

### is_connected("SSID")
To check if passed ssid is currently connected call function is_connected() which takes 1 string argument that is SSID
```python
is_connected("SSID")
```

function returns a list with 2 elements 1st is returncode from terminal 2nd is bool value which is True if connected and False if not connected

### scan_wifi("SSID")
To check if SSID is available to connect call function scan_wifi() which takes 1 string argument that is SSID
```python
scan_wifi("SSID")
```

function returns a list with 2 elements 1st is returncode from terminal 2nd is bool value which is True if available to connect and False if not available

### connect_wifi("SSID", "password")
To connect to wifi call function connect_wifi with 2 string arguments 1st is SSID and 2nd is password 
```python
connect_wifi("SSID", "password")
```

function returns a list with 1 element that is returncode from terminal

