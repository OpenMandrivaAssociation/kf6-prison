%define libname %mklibname KF6Prison
%define devname %mklibname KF6Prison -d
%define git 20231022

Name: kf6-prison
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/prison/-/archive/master/prison-master.tar.bz2#/prison-%{git}.tar.bz2
Summary: Barcode api currently offering a nice Qt api to produce QRCode barcodes and DataMatrix barcodes
URL: https://invent.kde.org/frameworks/prison
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: pkgconfig(libqrencode)
BuildRequires: pkgconfig(libdmtx)
BuildRequires: cmake(ZXing)
Requires: %{libname} = %{EVRD}

%description
Barcode api currently offering a nice Qt api to produce QRCode barcodes and DataMatrix barcodes

%package -n %{libname}
Summary: Barcode api currently offering a nice Qt api to produce QRCode barcodes and DataMatrix barcodes
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Barcode api currently offering a nice Qt api to produce QRCode barcodes and DataMatrix barcodes

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Barcode api currently offering a nice Qt api to produce QRCode barcodes and DataMatrix barcodes

%prep
%autosetup -p1 -n prison-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories6/prison.*

%files -n %{devname}
%{_includedir}/KF6/Prison
%{_libdir}/cmake/KF6Prison
%{_qtdir}/doc/KF6Prison.*
# Scanner
%{_includedir}/KF6/PrisonScanner
%{_qtdir}/doc/KF6PrisonScanner.*

%files -n %{libname}
%{_libdir}/libKF6Prison.so*
%dir %{_libdir}/qt6/qml/org/kde/prison
%{_libdir}/qt6/qml/org/kde/prison/qmldir
%{_libdir}/qt6/qml/org/kde/prison/*.version
%{_libdir}/qt6/qml/org/kde/prison/*.qmltypes
%{_libdir}/qt6/qml/org/kde/prison/*.so
# Scanner
%{_libdir}/libKF6PrisonScanner.so*
%{_libdir}/qt6/qml/org/kde/prison/scanner
