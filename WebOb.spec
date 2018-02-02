#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : WebOb
Version  : 1.7.4
Release  : 36
URL      : http://pypi.debian.net/WebOb/WebOb-1.7.4.tar.gz
Source0  : http://pypi.debian.net/WebOb/WebOb-1.7.4.tar.gz
Summary  : WSGI request and response object
Group    : Development/Tools
License  : MIT
Requires: WebOb-legacypython
Requires: WebOb-python3
Requires: WebOb-python
Requires: Sphinx
Requires: coverage
Requires: pytest
Requires: pytest-cov
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
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


%package python
Summary: python components for the WebOb package.
Group: Default
Requires: WebOb-legacypython
Requires: WebOb-python3
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
%setup -q -n WebOb-1.7.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1511277974
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1511277974
rm -rf %{buildroot}
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

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
