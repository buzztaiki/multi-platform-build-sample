VERSION=0.5.7
TGZ=msgpack-$(VERSION).tar.gz
SPEC=libmsgpack-devel.spec
TOPDIR=$(shell pwd)
DEFINES=--define '_topdir $(TOPDIR)' --define 'version $(VERSION)'

$(TGZ):
	wget http://msgpack.org/releases/cpp/msgpack-$(VERSION).tar.gz -O $(TGZ)

prepare: $(SPEC) $(TGZ)
	mkdir -p BUILD SOURCES SPECS SRPMS RPMS tmp
	cp $(TGZ) SOURCES
	cp $(SPEC) SPECS

build: prepare
	rpmbuild -bb $(DEFINES) SPECS/$(SPEC)

clean:
	rm -rf SOURCES SPECS RPMS SRPMS BUILD tmp

distclean: clean
	rm -f $(TGZ)
