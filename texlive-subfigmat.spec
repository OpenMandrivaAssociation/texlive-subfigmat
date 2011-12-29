# revision 20308
# category Package
# catalog-ctan /macros/latex/contrib/subfigmat
# catalog-date 2010-11-03 11:56:13 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-subfigmat
Version:	1.0
Release:	1
Summary:	Automates layout when using the subfigure package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/subfigmat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subfigmat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subfigmat.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines an array/matrix-type environment that is used with the
subfigure package to automate the placement of subfigures (or
tables or text). The subfigures are placed left-to-right, top-
to-bottom.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/subfigmat/subfigmat.sty
%doc %{_texmfdistdir}/doc/latex/subfigmat/subfigmat-doc.pdf
%doc %{_texmfdistdir}/doc/latex/subfigmat/subfigmat-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
