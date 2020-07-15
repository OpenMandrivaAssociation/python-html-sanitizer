Name:           python-html-sanitizer
Version:        1.9.1
Release:        1
Group:          Development/Python
Summary:        This is a allowlist-based and very opinionated HTML sanitizer that can be used both for untrusted and trusted sources
License:        BSD
URL:            https://pypi.org/project/html-sanitizer/
Source0:        https://pypi.python.org/packages/source/b/html-sanitizer/html-sanitizer-%{version}.tar.gz

BuildRequires: pkgconfig(python)
BuildRequires: python3dist(setuptools)
BuilsRequires: python3dist(beautifulsoup4)
BuildRequires: python3dist(lxml)

Requires: python3dist(beautifulsoup4)
Requires: python3dist(lxml)

%description
This is a allowlist-based and very opinionated HTML sanitizer that can be used both for untrusted and trusted sources. 
It attempts to clean up the mess made by various rich text editors and or copy-pasting to make styling of webpages simpler and more consistent. 
It builds on the excellent HTML cleaner in lxml to make the result both valid and safe.
HTML sanitizer goes further than e.g. bleach in that it not only ensures that content is safe and tags and attributes conform to a given allowlist, 
but also applies additional transforms to HTML fragments.

%prep
%setup -q -n html-sanitizer-%{version}
%autopatch -p1

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.rst
#{python_sitearch}/*
