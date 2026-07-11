%global tl_name pst-support
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Assorted support files for use with PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/pst-support
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-support.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-support.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An appropriate set of job options, together with process scripts for use
with TeXnicCenter/

