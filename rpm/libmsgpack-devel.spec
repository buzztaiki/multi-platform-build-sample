%define debug_package %{nil}    # Suppress debuginfo package.

%{!?rhel:BuildRequires:buildsys-macros}
%define dist .el%{rhel}.buzztaiki

Name:           libmsgpack-devel
Version:        %{version}
Release:        1%{?dist}
Summary:        Binary-based efficient object serialization library.
Packager:       Taiki Sugawara

Group:          Development/Libraries
License:        Apache License
URL:            http://msgpack.org/
Source0:        http://msgpack.org/releases/cpp/msgpack-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  gcc-c++
#Requires:      

%description
Binary-based efficient object serialization library.


%prep
%setup -q -n msgpack-%{version}


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%{_includedir}/msgpack.h
%{_includedir}/msgpack.hpp
%{_includedir}/msgpack/*
%{_libdir}/libmsgpack.*
%{_libdir}/libmsgpackc.*


%changelog

