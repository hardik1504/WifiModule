import subprocess


def turn_wifi_off():
    args = ["networksetup", "-setairportpower", "en0", "off"]
    cmd = subprocess.run(args=args)
    return [cmd.returncode]


def turn_wifi_on():
    args = ["networksetup", "-setairportpower", "en0", "on"]
    cmd = subprocess.run(args=args)
    return [cmd.returncode]


def is_connected(ssid):
    args = ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport", "-I", "|", "grep SSID"]
    cmd = subprocess.run(args=args, universal_newlines=True, stdout=subprocess.PIPE)
    stdout = cmd.stdout.splitlines()
    connected = False
    for item in stdout:
        if item.find(ssid) != -1:
            connected = True
            break
    return [cmd.returncode, connected]


def scan_wifi(ssid):
    args = ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport", "scan"]
    cmd = subprocess.run(args=args, universal_newlines=True, stdout=subprocess.PIPE)
    stdout = cmd.stdout.splitlines()
    found = False
    for item in stdout:
        if item.find(ssid) != -1:
            found = True
            break
    return [cmd.returncode, found]


def connect_wifi(ssid, passw):
    args = ["networksetup", "-setairportnetwork", "en0", ssid, passw]
    cmd = subprocess.run(args=args)
    return [cmd.returncode]


if __name__ == "__main__":
    print(turn_wifi_off())
    print(turn_wifi_on())
    print(scan_wifi("SSID"))
    print(connect_wifi("SSID", "PASSWORD"))
    print(is_connected("SSID"))
