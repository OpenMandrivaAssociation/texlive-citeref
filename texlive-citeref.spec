%global tl_name citeref
%global tl_revision 47407

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Add reference-page-list to bibliography-items
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/citeref
License:	bsd4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/citeref.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/citeref.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package does its job without using the indexing facilities, and
needs no special \cite-replacement package.

