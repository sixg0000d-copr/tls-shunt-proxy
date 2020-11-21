MAKEFILE_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
SCM_ROOT := $(abspath $(MAKEFILE_DIR)/..)
# SPECS
SOURCE_URL := https://github.com/liberal-boy/tls-shunt-proxy
NAME := tls-shunt-proxy
TAG := 0.6.1
# ENVIRONMENTS
spec := $(or $(spec), $(SCM_ROOT)/$(NAME).spec)
outdir := $(or $(outdir), $(SCM_ROOT)/outdir)


default: srpm

init:
ifeq ($(shell id -u),0)
	dnf install -y "tar" "golang >= 1.11" "git"
else
	sudo dnf install -y "tar" "golang >= 1.11" "git"
endif

$(outdir):
	[ -d "$(outdir)" ] || mkdir -p $(outdir)

.ONESHELL: sources
sources: $(outdir) init
	cd $(outdir)
	curl -L $(SOURCE_URL)/archive/$(TAG)/$(NAME)-$(TAG).tar.gz -o $(NAME)-$(TAG).tar.gz
	tar -xzf $(NAME)-$(TAG).tar.gz
	cd $(NAME)-$(TAG)
	go mod vendor
	tar -czf ../vendor.tar.gz vendor
	cd .. && rm -rf $(NAME)-$(TAG)

srpm: $(outdir) $(spec) sources
	rpmbuild --define "_sourcedir $(outdir)" --define "_srcrpmdir $(outdir)" -bs $(spec)

clean:
	rm -rf $(outdir)

.PHONY: default init sources srpm clean
