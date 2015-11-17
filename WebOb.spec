#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : WebOb
Version  : 1.5.1
Release  : 16
URL      : https://pypi.python.org/packages/source/W/WebOb/WebOb-1.5.1.tar.gz
Source0  : https://pypi.python.org/packages/source/W/WebOb/WebOb-1.5.1.tar.gz
Summary  : WSGI request and response object
Group    : Development/Tools
License  : MIT
Requires: WebOb-python
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
WebOb
=====
.. image:: https://travis-ci.org/Pylons/webob.png?branch=master
:target: https://travis-ci.org/Pylons/webob

%package python
Summary: python components for the WebOb package.
Group: Default
Provides: webob-python
Requires: nose-python

%description python
python components for the WebOb package.


%prep
%setup -q -n WebOb-1.5.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
