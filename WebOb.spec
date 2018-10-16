#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : WebOb
Version  : 1.8.3
Release  : 51
URL      : https://files.pythonhosted.org/packages/79/f1/81d397e07ef799794f81aee8ef48ccb942fd77324aee8b0f423deda2b40f/WebOb-1.8.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/79/f1/81d397e07ef799794f81aee8ef48ccb942fd77324aee8b0f423deda2b40f/WebOb-1.8.3.tar.gz
Summary  : WSGI request and response object
Group    : Development/Tools
License  : MIT
Requires: WebOb-license = %{version}-%{release}
Requires: WebOb-python = %{version}-%{release}
Requires: WebOb-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils23
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools-legacypython
BuildRequires : tox
BuildRequires : virtualenv

%description
=====

%package legacypython
Summary: legacypython components for the WebOb package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the WebOb package.


%package license
Summary: license components for the WebOb package.
Group: Default

%description license
license components for the WebOb package.


%package python
Summary: python components for the WebOb package.
Group: Default
Requires: WebOb-python3 = %{version}-%{release}
Provides: webob-python

%description python
python components for the WebOb package.


%package python3
Summary: python3 components for the WebOb package.
Group: Default
Requires: python3-core

%description python3
python3 components for the WebOb package.


%prep
%setup -q -n WebOb-1.8.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539663631
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1539663631
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/WebOb
cp docs/license.txt %{buildroot}/usr/share/package-licenses/WebOb/docs_license.txt
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/WebOb/docs_license.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
