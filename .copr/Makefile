MAKEFILE_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
SCM_ROOT := $(abspath $(MAKEFILE_DIR)/..)
# SPECS
SOURCE_URL := https://github.com/liberal-boy/tls-shunt-proxy
TAG := 0.7.0
RELEASE := 1
# ENVIRONMENTS
spec := $(or $(spec), $(SCM_ROOT)/tls-shunt-proxy.spec)
outdir := $(or $(outdir), $(SCM_ROOT)/outdir)
# PACKAGE MANAGER INSTALL COMMAND
ifeq ($(shell id -u),0)
pm_install := dnf -y install
else
pm_install := sudo dnf -y install
endif


all: srpm

init:
	$(pm_install) "@RPM Development Tools" "tar" "git" "sed" "golang >= 1.11"

$(outdir):
	[ -d "$(outdir)" ] || mkdir -p $(outdir)

spec: $(outdir) init
	sed \
	-e "s|@SOURCE_URL@|$(SOURCE_URL)|g" \
	-e "s|@TAG@|$(TAG)|g" \
	-e "s|@RELEASE@|$(RELEASE)|g" \
	$(spec).in > $(outdir)/tls-shunt-proxy.spec

.ONESHELL: sources
sources: $(outdir) init
	cd $(outdir)
	curl -L $(SOURCE_URL)/archive/$(TAG)/tls-shunt-proxy-$(TAG).tar.gz -o tls-shunt-proxy-$(TAG).tar.gz
	tar -xzf tls-shunt-proxy-$(TAG).tar.gz
	cd tls-shunt-proxy-$(TAG)
	go mod vendor
	tar -czf ../vendor.tar.gz vendor
	cd .. && rm -rf tls-shunt-proxy-$(TAG)
	cp $(SCM_ROOT)/tls-shunt-proxy.service $(outdir)/tls-shunt-proxy.service

srpm: $(outdir) spec sources
	rpmbuild \
	--define "_sourcedir $(outdir)" \
	--define "_srcrpmdir $(outdir)" \
	-bs $(outdir)/tls-shunt-proxy.spec

clean:
	rm -rf $(outdir)

.PHONY: all init sources srpm clean
