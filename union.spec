%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define libname %mklibname Union
%define develname %mklibname Union -d

Summary:	Unified style engine for Plasma
Name:		union
Version:	6.7.5
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/KDE
URL:		https://invent.kde.org/plasma/union
Source0:	http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6ShaderTools)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6ColorScheme)
BuildRequires:	cmake(KF6Kirigami)
BuildRequires:	cmake(KF6KirigamiPlatform)
BuildRequires:	cmake(Plasma)
BuildRequires:	cmake(cxx-rust-cssparser)

BuildSystem:	cmake
BuildOption:	-DBUILD_TESTING:BOOL=OFF
BuildOption:	-DBUILD_EXAMPLES:BOOL=OFF
BuildOption:	-DBUILD_INPUT_PLASMASVG:BOOL=OFF
BuildOption:	-DBUILD_DOCS:BOOL=OFF
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

Requires:	%{libname} = %{EVRD}

%description
Union is a style engine that provides a unified style description to
several output styles (QtQuick, Kirigami, QtWidgets). Applications
can use it by setting QT_QUICK_CONTROLS_STYLE=org.kde.union.

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
Shared library for %{name}.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
Headers and CMake files for developing applications that use %{name}.

%files
%{_qtdir}/qml/org/kde/union
%{_qtdir}/plugins/styles/libUnionWidgetsStyle.so
%{_qtdir}/plugins/kf6/kirigami/platform/org.kde.union.so
%{_qtdir}/plugins/union
%{_datadir}/kstyle/themes/union.themerc
%{_datadir}/union
%{_datadir}/qlogging-categories6/union.categories
%{_bindir}/union-ruleinspector

%files -n %{libname}
%{_libdir}/libUnion.so.*

%files -n %{develname}
%{_includedir}/union
%{_libdir}/libUnion.so
%{_libdir}/cmake/Union
