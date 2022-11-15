Name:		texlive-citeref
Version:	47407
Release:	1
Summary:	Add reference-page-list to bibliography-items
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/citeref
License:	bsd4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/citeref.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/citeref.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package does its job without using the indexing facilities,
and needs no special \cite-replacement package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/citeref
%doc %{_texmfdistdir}/doc/latex/citeref

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
