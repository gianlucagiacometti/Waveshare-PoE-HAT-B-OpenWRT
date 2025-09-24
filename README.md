# Waveshare-PoE-HAT-B-OpenWRT

Specifically for this PoE-HAT: https://www.waveshare.com/wiki/PoE_HAT_(B)

This is a result of adaptation of https://github.com/grootwitbaas/Waveshare-PoE-HAT-B-Home-Assistant-Addon to OpenWRT distro.

It works on Raspberry Pi 4B 64-bit with the dedicated firmware (https://firmware-selector.openwrt.org/?version=24.10.2&target=bcm27xx%2Fbcm2711&id=rpi-4).

## Install ##

1. opkg install git git-http gcc python3-base-src python3-dev python3-dev-src python3-gpiod python3-numpy python3-smbus i2c-tools libi2c kmod-i2c-core kmod-i2c-bcm2835 kmod-i2c-brcmstb kmod-i2c-smbus libtiff6 libjpeg-turbo kmod-i2c-bcm2835 kmod-spi-bcm2835
2. pip install RPi.GPIO
3. git clone https://github.com/gianlucagiacometti/Waveshare-PoE-HAT-B-OpenWRT.git
4. copy /bin /lib /cfg into /opt

## Test ##

Use the command
```
python3 /opt/bin/main.py &
```

## Start at boot ##

insert in rc.local
```
python3 /opt/bin/main.py &
```

or 

create an init script according to this manual: https://openwrt.org/docs/techref/initscripts
