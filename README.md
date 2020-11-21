# tls-shunt-proxy

Build tls-shunt-proxy on Fedora Copr

[![tls-shunt-proxy Copr Build](https://copr.fedorainfracloud.org/coprs/sixg0000d/v2ray/package/tls-shunt-proxy/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/sixg0000d/v2ray/package/tls-shunt-proxy/)

## Installation
```sh
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
```sh
systemctl enable tls-shunt-proxy.service --now
```

## Build for your self
1. Follow the [guide](https://docs.fedoraproject.org/en-US/quick-docs/create-hello-world-rpm/#_development_environment) to install `rpmbuild`, `mock`.
2. Make srpm:
```sh
git clone https://github.com/sixg0000d-copr/tls-shunt-proxy.git
cd tls-shunt-proxy
make -f .copr/Makefile srpm
```
3. Run build on mock:
```sh
mock outdir/tls-shunt-proxy-*.srpm
```
