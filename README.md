# tls-shunt-proxy

Build tls-shunt-proxy on Fedora Copr

[![tls-shunt-proxy Copr Build](https://copr.fedorainfracloud.org/coprs/sixg0000d/v2ray/package/tls-shunt-proxy/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/sixg0000d/v2ray/package/tls-shunt-proxy/)

## Installation
```shell
# You may need to run the following commands with sudo
dnf copr enable sixg0000d/v2ray
dnf install tls-shunt-proxy
```

## Usage
1. Configure `tls-shunt-proxy` in:
```
/etc/tls-shunt-proxy/config.yaml
```
2. Start the service:
```shell
systemctl enable tls-shunt-proxy.service --now
```
