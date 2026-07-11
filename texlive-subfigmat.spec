%global tl_name subfigmat
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Automates layout when using the subfigure package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/subfigmat
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subfigmat.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subfigmat.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Defines an array/matrix-type environment that is used with the subfigure
package to automate the placement of subfigures (or tables or text). The
subfigures are placed left-to-right, top-to-bottom.

