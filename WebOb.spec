#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : WebOb
Version  : 1.8.6
Release  : 71
URL      : https://files.pythonhosted.org/packages/2a/32/5f3f43d0784bdd9392db0cb98434d7cd23a0d8a420c4d243ad4cb8517f2a/WebOb-1.8.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/2a/32/5f3f43d0784bdd9392db0cb98434d7cd23a0d8a420c4d243ad4cb8517f2a/WebOb-1.8.6.tar.gz
Summary  : WSGI request and response object
Group    : Development/Tools
License  : MIT
Requires: WebOb-license = %{version}-%{release}
Requires: WebOb-python = %{version}-%{release}
Requires: WebOb-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
=====

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
Provides: pypi(webob)

%description python3
python3 components for the WebOb package.


%prep
%setup -q -n WebOb-1.8.6
cd %{_builddir}/WebOb-1.8.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603407684
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/WebOb
cp %{_builddir}/WebOb-1.8.6/docs/license.txt %{buildroot}/usr/share/package-licenses/WebOb/c6186941914c00e75b649dd640adcf534d0cefd6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/WebOb/c6186941914c00e75b649dd640adcf534d0cefd6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
