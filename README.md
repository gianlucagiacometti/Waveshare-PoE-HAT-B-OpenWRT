# Waveshare-PoE-HAT-B-OpenWRT

Specifically for this PoE-HAT: https://www.waveshare.com/wiki/PoE_HAT_(B)

This is a result of adaptation of https://github.com/grootwitbaas/Waveshare-PoE-HAT-B-Home-Assistant-Addon to OpenWRT distro.

It works on Raspberry Pi 4B 64-bit with the dedicated firmware (https://firmware-selector.openwrt.org/?version=24.10.2&target=bcm27xx%2Fbcm2711&id=rpi-4)

## Test ##

Use the command
```
python3 /opt/bin/main.py &
```

## How to ##

1. copy /bin /lib /cfg into /opt
2. insert ```python3 /opt/bin/main.py &``` in rc.local
3. reboot
