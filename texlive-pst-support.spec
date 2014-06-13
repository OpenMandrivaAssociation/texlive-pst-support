# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/pst-support
# catalog-date 2009-02-07 21:39:27 +0100
# catalog-license lppl
# catalog-version 2009-02-05
Name:		texlive-pst-support
Version:	20090205
Release:	7
Summary:	Assorted support files for use with PStricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/pst-support
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-support.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-support.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090205-2
+ Revision: 755482
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090205-1
+ Revision: 719400
- texlive-pst-support
- texlive-pst-support
- texlive-pst-support
- texlive-pst-support

