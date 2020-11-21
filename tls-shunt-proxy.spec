# Generated by go2rpm 1.3

# https://github.com/liberal-boy/tls-shunt-proxy
%global goipath         github.com/liberal-boy/tls-shunt-proxy
Version:                0.6.1
%global tag             0.6.1

%gometa

Name:           tls-shunt-proxy
Release:        1%{?dist}
Summary:        A tool to shunt TLS traffic
License:        None
URL:            %{gourl}

# Source is created by:
# curl -L https://github.com/liberal-boy/tls-shunt-proxy/archive/0.6.1/tls-shunt-proxy-0.6.1.tar.gz -o tls-shunt-proxy-0.6.1.tar.gz
# tar -xzf tls-shunt-proxy-0.6.1.tar.gz
# cd tls-shunt-proxy-0.6.1
# go mod vendor
# tar -czf ../vendor.tar.gz vendor
# cd .. && rm -rf tls-shunt-proxy-0.6.1
Source0:        %{gosource}
Source1:        vendor.tar.gz

BuildRequires:  systemd-rpm-macros
Requires(pre):  shadow-utils
%{?systemd_requires}

%description
A tool to shunt TLS traffic.
User Guide: https://guide.v2fly.org/advanced/tcp_tls_shunt_proxy.html.


%prep
# prep: sources
%setup -q -a 1
%global gobuilddir %{_builddir}/%{archivename}/_build
if [[ ! -e "%{gobuilddir}/bin" ]] ; then
    install -m 0755 -vd %{gobuilddir}/bin
    export GOPATH="%{gobuilddir}"
fi
if [[ ! -e "%{gobuilddir}/src/%{goipath}" ]] ; then
    install -m 0755 -vd $(dirname %{gobuilddir}/src/%{goipath})
    ln -fs %{_builddir}/%{archivename} %{gobuilddir}/src/%{goipath}
fi
cd %{gobuilddir}/src/%{goipath}

# prep: config
install -m 0644 -vp config.simple.yaml            %{gobuilddir}/config.yaml

# prep: systemd unit file
install -m 0644 -vp dist/tls-shunt-proxy.service  %{gobuilddir}/tsp.service


%build
# build: binary
export LDFLAGS="-linkmode=external "
%gobuild -o %{gobuilddir}/bin/tsp %{goipath}
unset LDFLAGS


%install
# install: binary
install -m 0755 -vd                            %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/tsp      %{buildroot}%{_bindir}/tls-shunt-proxy
# install: config
install -m 0755 -vd                            %{buildroot}%{_sysconfdir}/tls-shunt-proxy
install -m 0644 -vp %{gobuilddir}/config.yaml  %{buildroot}%{_sysconfdir}/tls-shunt-proxy/config.yaml
# install: systemd unit file
install -m 0755 -vd                            %{buildroot}%{_unitdir}
install -m 0644 -vp %{gobuilddir}/tsp.service  %{buildroot}%{_unitdir}/tls-shunt-proxy.service
# install: ocsp dir
install -m 0755 -vd                            %{buildroot}%{_sysconfdir}/ssl/tls-shunt-proxy


%files
%doc README.md
# binary
%{_bindir}/tls-shunt-proxy
# config
%dir               %{_sysconfdir}/tls-shunt-proxy
%config(noreplace) %{_sysconfdir}/tls-shunt-proxy/config.yaml
# systemd unit file
%{_unitdir}/tls-shunt-proxy.service
# ocsp dir
%attr(-, %{name}, %{name}) %dir %{_sysconfdir}/ssl/tls-shunt-proxy


# Scriptlets >>
%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    (useradd -r \
    -g %{name} \
    -d %{_localstatedir}/%{name} \
    -s /sbin/nologin \
    -c "User for running %{name}" %{name} && \
    echo "  User %{name} created.")
exit 0

%post
%systemd_post tls-shunt-proxy.service

%preun
%systemd_preun tls-shunt-proxy.service

if [ $1 -eq 0 ] && (getent passwd %{name} >/dev/null); then
    # Package removal, not upgrade
    echo "  You may should remove user %{name} mannually."
fi

%postun
%systemd_postun_with_restart tls-shunt-proxy.service
# << Scriptlets

%changelog
* Sat Nov 21 2020 sixg0000d <sixg0000d@gmail.com> - 0.6.1-1
- Initial package
