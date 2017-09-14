#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : WebOb
Version  : 1.6.2
Release  : 31
URL      : http://pypi.debian.net/WebOb/WebOb-1.6.2.tar.gz
Source0  : http://pypi.debian.net/WebOb/WebOb-1.6.2.tar.gz
Summary  : WSGI request and response object
Group    : Development/Tools
License  : MIT
Requires: WebOb-legacypython
Requires: WebOb-python
Requires: Sphinx
Requires: coverage
Requires: nose
BuildRequires : nose-python
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

%description legacypython
legacypython components for the WebOb package.


%package python
Summary: python components for the WebOb package.
Group: Default
Requires: WebOb-legacypython
Provides: webob-python

%description python
python components for the WebOb package.


%prep
%setup -q -n WebOb-1.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505411182
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1505411182
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
/usr/lib/python3*/*
