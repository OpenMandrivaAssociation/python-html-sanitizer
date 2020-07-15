Name:           python-html-sanitizer
Version:        1.3.6
Release:        1
Group:          Development/Python
Summary:        a list-like type with better asymptotic performance and similar performance on small lists
License:        BSD
URL:            https://pypi.org/project/html-sanitizer/
Source0:        https://pypi.python.org/packages/source/b/html-sanitizer/html-sanitizer-%{version}.tar.gz

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

%description
The blist is a drop-in replacement for the Python list the
provides better performance when modifying large lists.

The blist package also provides sortedlist, sortedset,
weaksortedlist, weaksortedset, sorteddict, and btuple
types.

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
%{python_sitearch}/*
