---
title: Chrome Setup
---

## General Browsing Extensions ##

* [uBlock Origin](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm?hl=en)
* [Privacy Badger](https://chrome.google.com/webstore/detail/privacy-badger/pkehgijcmpdhfbdbbnkijodmdjhbjlgp?hl=en-US)
* [HTTPS Everywhere](https://chrome.google.com/webstore/detail/https-everywhere/gcbommkclmclpchllfjekcdonpmejbdp?hl=en)

## Security Testing Extensions ##

* [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg)
* [Proxy SwitchyOmega](https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif)
* [JSON Viewer Awesome](https://chrome.google.com/webstore/detail/json-viewer-awesome/iemadiahhbebdklepanmkjenfdebfpfe)
* [EXIF Viewer Pro](https://chrome.google.com/webstore/detail/exif-viewer-pro/mmbhfeiddhndihdjeganjggkmjapkffm)
* [Burp Suite Navigation](https://chrome.google.com/webstore/detail/burp-suite-navigation-rec/anpapjclbjicacakeoggghfldppbkepg)

## Run Chrome for Burp ##

```
/usr/bin/google-chrome-beta --ignore-certificate-errors \
    --user-data-dir=${HOME}/.config/chrome-pentest \
    --proxy-server=127.0.0.1:8080
```
