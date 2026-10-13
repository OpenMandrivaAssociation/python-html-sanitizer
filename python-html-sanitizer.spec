%define module html-sanitizer
%define oname html_sanitizer

Name:		python-html-sanitizer
Version:	2.6.0
Release:	2
Group:		Development/Python
Summary:	Allowlist-based HTML cleaner
License:	BSD-3-Clause
URL:		https://github.com/matthiask/html-sanitizer/
Source0:	https://files.pythonhosted.org/packages/source/h/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(beautifulsoup4)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(lxml)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
This is a allowlist-based and very opinionated HTML sanitizer that can be used
both for untrusted and trusted sources.

It attempts to clean up the mess made by various rich text editors and or
copy-pasting to make styling of webpages simpler and more consistent.

It builds on the excellent HTML cleaner in lxml to make the result both valid
and safe.

HTML sanitizer goes further than e.g. bleach in that it not only ensures that
content is safe and tags and attributes conform to a given allowlist, but also
applies additional transforms to HTML fragments.

%files
%doc README.rst
%license LICENSE
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}*.*-info
