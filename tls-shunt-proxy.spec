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

%description
A tool to shunt TLS traffic.
User Guide: https://guide.v2fly.org/advanced/tcp_tls_shunt_proxy.html.


%prep
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


%build
export LDFLAGS="-linkmode=external "
%gobuild -o %{gobuilddir}/bin/tls-shunt-proxy %{goipath}
unset LDFLAGS


%install
install -m 0755 -vd                                    %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/tls-shunt-proxy  %{buildroot}%{_bindir}/


%files
%doc README.md
%{_bindir}/tls-shunt-proxy


%changelog
* Sat Nov 21 2020 sixg0000d <sixg0000d@gmail.com> - 0.6.1-1
- Initial package