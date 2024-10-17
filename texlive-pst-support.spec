Name:		texlive-pst-support
Version:	15878
Release:	2
Summary:	Assorted support files for use with PStricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/pst-support
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-support.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-support.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
An appropriate set of job options, together with process
scripts for use with TeXnicCenter/.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/generic/pst-support/README
%doc %{_texmfdistdir}/doc/generic/pst-support/Standard_transparency.joboptions
%doc %{_texmfdistdir}/doc/generic/pst-support/latex-ps-pdf.tco
%doc %{_texmfdistdir}/doc/generic/pst-support/latex-pstpdf-pdf.tco
%doc %{_texmfdistdir}/doc/generic/pst-support/pdflatex-autopstpdf.tco

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
