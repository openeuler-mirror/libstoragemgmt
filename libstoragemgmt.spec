%global py2_build_dir %{_builddir}/%{name}-%{version}-%{release}-python2
%define with_python2 0
Name:		libstoragemgmt
Version:	1.9.6
Release:	2
Summary:	Storage array management library
License:	LGPLv2+
URL:		https://github.com/libstorage/libstoragemgmt
Source0:	https://github.com/libstorage/libstoragemgmt/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc gcc-c++ autoconf automake libtool libxml2-devel check-devel perl-interpreter
BuildRequires:  glib2-devel systemd bash-completion libconfig-devel systemd-devel
BuildRequires:  procps sqlite-devel python3-six python3-devel systemd systemd-devel chrpath valgrind
%{?systemd_requires}
	
%if 0%{?with_python2}
BuildRequires:  python2-six python2-devel
%endif

Requires:	python3-libstoragemgmt
Obsoletes:      python2-libstoragemgmt python2-libstoragemgmt-clibs

%description
The libStorageMgmt library will provide a vendor agnostic open source storage
application programming interface (API) that will allow management of storage
arrays.  The library includes a command line interface for interactive use and
scripting (command lsmcli).  The library also has a daemon that is used for
executing plug-ins in a separate process (lsmd).

%package        devel
Summary:        Header files for libstoragemgmt
Requires:       %{name} = %{version}-%{release}

%description    devel
Header files for libstoragemgmt

%if 0%{?with_python2}
%package        -n python2-%{name}
Summary:        python2 for libstoragemgmt
Requires:       %{name} = %{version}-%{release} python2-libstoragemgmt-clibs
BuildArch:      noarch
Provides:       libstoragemgmt-python = %{version}-%{release}
Obsoletes:      libstoragemgmt-python < %{version}-%{release}
%{?python_provide:%python_provide python2-%{name}}

%description -n python2-libstoragemgmt
python2 for libstoragemgmt
	
%package     -n python2-libstoragemgmt-clibs
Summary:        Python2 for libstoragemgmt-clibs
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-python-clibs = %{version}-%{release}
Provides:       %{name}-python-clibs%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-python-clibs < %{version}-%{release}

%{?python_provide:%python_provide python2-%{name}-clibs}

%description -n python2-libstoragemgmt-clibs
Python2 for libstoragemgmt-clibs.

%endif

%package     -n python3-libstoragemgmt
Summary:        python3 for libstoragemgmt
Requires:       %{name} = %{version}-%{release} python3-libstoragemgmt-clibs

%{?python_provide:%python_provide python3-%{name}}

%description -n python3-libstoragemgmt
python3 for libstoragemgmt

%package     -n python3-libstoragemgmt-clibs
Summary:        python3 for libstoragemgmt-clibs
Requires:       %{name} = %{version}-%{release}
	
%{?python_provide:%python_provide python3-%{name}-clibs}

%description -n python3-libstoragemgmt-clibs
python3 for libstoragemgmt-clibs

%package        smis-plugin
Summary:        smis generic aaray for libstoragemgmt
BuildArch:      noarch
BuildRequires:  python3-pywbem	
%if 0%{?with_python2}
BuildRequires:  python2-pywbem
%endif 
Requires:       python3-pywbem python3-%{name} = %{version}-%{release}
Requires(post): python3-%{name} = %{version}
Requires(postun): python3-%{name} = %{version}
Provides:       %{name}-ibm-v7k-plugin = 2:%{version}-%{release}
Obsoletes:      %{name}-ibm-v7k-plugin <= 2:0.1.0-3 

%description    smis-plugin
smis generic aaray for libstoragemgmt.

%package        netapp-plugin
Summary:        netapp files for libstoragemgmt
BuildArch:      noarch
Requires:       python3-%{name} = %{version}
Requires(post): python3-%{name} = %{version}
Requires(postun): python3-%{name} = %{version}
Provides:       %{name}-targetd-plugin = %{version}-%{release}
Obsoletes:      %{name}-targetd-plugin < %{version}-%{release}
Provides:       %{name}-nstor-plugin = %{version}-%{release}
Obsoletes:      %{name}-nstor-plugin < %{version}-%{release}
Provides:       %{name}-egaraid-plugin = %{version}-%{release}
Obsoletes:      %{name}-egaraid-plugin < %{version}-%{release}
Provides:       %{name}-hpsa-plugin = %{version}-%{release}
Obsoletes:      %{name}-hpsa-plugin < %{version}-%{release}
Provides:       %{name}-arcconf-plugin = %{version}-%{release}
Obsoletes:      %{name}-arcconf-plugin < %{version}-%{release}
Provides:       %{name}-local-plugin = %{version}-%{release}
Obsoletes:      %{name}-local-plugin < %{version}-%{release}
Provides:       %{name}-megaraid-plugin = %{version}-%{release}
Obsoletes:      %{name}-megaraid-plugin < %{version}-%{release}

%description        netapp-plugin
netapp files for libstoragemgmt

%package        udev
Summary:        Udev files for %{name}

%description    udev
Udev files for %{name}.

%package        nfs-plugin
Summary:        Files for NFS local filesystem support for %{name}
Requires:       python3-%{name} = %{version} nfs-utils 
Requires(post): python3-%{name} = %{version}
Requires(postun): python3-%{name} = %{version}

%description    nfs-plugin
Files for NFS local filesystem support for %{name}

%package        nfs-plugin-clibs
Summary:        clibs package for nfs-plugin
Requires:       %{name} = %{version}-%{release}

%description    nfs-plugin-clibs
clibs package for nfs-plugi

%package_help       

%prep
%autosetup -n %{name}-%{version} -p1

%build
%if "%toolchain" == "clang"
	export CFLAGS="$CFLAGS -Wno-ignored-attributes -Wno-varargs -Wno-string-plus-int -Wno-header-guard"
	export CXXFLAGS="$CXXFLAGS -Wno-ignored-attributes -Wno-varargs -Wno-string-plus-int -Wno-header-guard"
%endif
./autogen.sh
%if 0%{?with_python2}	
rm -fr %{py2_build_dir}
cp -a . %{py2_build_dir}
%endif

%configure --with-python3
%make_build 

%if 0%{?with_python2}	
pushd %{py2_build_dir}
%configure 
%make_build
popd
%endif

%install
%if 0%{?with_python2}	
pushd %{py2_build_dir}
%make_install 
rm -rf %{buildroot}/%{python_sitelib}/lsm/plugin
rm -rf %{buildroot}/%{_bindir}/lsmcli
popd
%endif

%make_install
%delete_la

install -m 0755 -d %{buildroot}/%{_udevrulesdir}
install -m 0644 tools/udev/90-scsi-ua.rules %{buildroot}/%{_udevrulesdir}/90-scsi-ua.rules
install -m 0755 tools/udev/scan-scsi-target %{buildroot}/%{_udevrulesdir}/../scan-scsi-target

%if 0%{with test}
%check
if ! make check
then
  cat test-suite.log || true
  exit 1
fi

%if 0%{?with_python2}	
pushd %{py2_build_dir}
if ! make check
then
  cat test-suite.log || true
  exit 1
fi
popd
%endif
%endif

%pre
getent group libstoragemgmt >/dev/null || groupadd -r libstoragemgmt
	
getent passwd libstoragemgmt >/dev/null || \
    useradd -r -g libstoragemgmt -d /var/run/lsm -s /sbin/nologin \
    -c "daemon account for libstoragemgmt" libstoragemgmt

%post
/sbin/ldconfig
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%systemd_post %{name}.service

	
%preun
%systemd_preun %{name}.service

%postun
/sbin/ldconfig
%systemd_postun %{name}.service
	
%post smis-plugin
if [ $1 -eq 1 ]; then
    # New install.
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi
 
%postun smis-plugin
if [ $1 -eq 0 ]; then
    # Remove
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

%post netapp-plugin
if [ $1 -eq 1 ]; then
    # New install.
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

%postun netapp-plugin
if [ $1 -eq 0 ]; then
    # Remove
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

%post nfs-plugin
if [ $1 -eq 1 ]; then
    # New install.
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi
%postun nfs-plugin
if [ $1 -eq 0 ]; then
    # Remove
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

	
%files
%defattr(-,root,root)
%license COPYING.LIB
%dir %{_sysconfdir}/lsm/pluginconf.d
%config(noreplace) %{_sysconfdir}/lsm/lsmd.conf
%attr(0644, root, root) %{_tmpfilesdir}/%{name}.conf
%{_bindir}/lsmd
%{_bindir}/lsmcli
%{_bindir}/simc_lsmplugin
%{_libdir}/*.so.*
%{_unitdir}/%{name}.service
%{_datadir}/bash-completion/completions/lsmcli
%ghost %dir %attr(0775, root, libstoragemgmt) /run/lsm/
%ghost %dir %attr(0775, root, libstoragemgmt) /run/lsm/ipc

%files           devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%if 0%{?with_python2}	
%files        -n python2-%{name}
%defattr(-,root,root)	
%dir %{python_sitelib}/lsm
%{python2_sitelib}/lsm/*.py*
%{python_sitelib}/lsm/external/*
%{python_sitelib}/lsm/lsmcli/*

%files        -n python2-%{name}-clibs
%defattr(-,root,root)
%{python2_sitelib}/lsm/_clib.*

%endif

%files        -n python3-%{name}
%defattr(-,root,root)
%dir %{_libexecdir}/lsm.d
%{_libexecdir}/lsm.d/*.py*
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/sim.conf
%{_bindir}/sim_lsmplugin
%dir %{python3_sitearch}/lsm
%{python3_sitearch}/lsm/*.py
%{python3_sitearch}/lsm/__pycache__/
%{python3_sitearch}/lsm/lsmcli/*
%dir %{python3_sitearch}/sim_plugin
%{python3_sitearch}/sim_plugin/__pycache__/
%{python3_sitearch}/sim_plugin/__init__.*
%{python3_sitearch}/sim_plugin/simulator.*
%{python3_sitearch}/sim_plugin/simarray.*

%files        -n python3-%{name}-clibs
%defattr(-,root,root)
%{python3_sitearch}/lsm/_clib.*

%files           smis-plugin
%defattr(-,root,root)
%dir %{python3_sitelib}/smispy_plugin
%dir %{python3_sitelib}/smispy_plugin/__pycache__
%{python3_sitelib}/smispy_plugin/__pycache__/*
%{python3_sitelib}/smispy_plugin/__init__.*
%{python3_sitelib}/smispy_plugin/smis.*
%{python3_sitelib}/smispy_plugin/dmtf.*
%{python3_sitelib}/smispy_plugin/utils.*
%{python3_sitelib}/smispy_plugin/smis_common.*
%{python3_sitelib}/smispy_plugin/smis_cap.*
%{python3_sitelib}/smispy_plugin/smis_sys.*
%{python3_sitelib}/smispy_plugin/smis_pool.*
%{python3_sitelib}/smispy_plugin/smis_disk.*
%{python3_sitelib}/smispy_plugin/smis_vol.*
%{python3_sitelib}/smispy_plugin/smis_ag.*
%{_bindir}/smispy_lsmplugin
%{_mandir}/man1/smispy_lsmplugin.1*

%files           netapp-plugin
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/megaraid.conf
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/hpsa.conf
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/arcconf.conf
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/local.conf
%{_bindir}/targetd_lsmplugin
%{_bindir}/megaraid_lsmplugin
%{_bindir}/hpsa_lsmplugin
%{_bindir}/arcconf_lsmplugin
%{_bindir}/local_lsmplugin
%{python3_sitelib}/hpsa_plugin/__pycache__/*
%{python3_sitelib}/hpsa_plugin/__init__.*
%{python3_sitelib}/hpsa_plugin/hpsa.*
%{python3_sitelib}/hpsa_plugin/utils.*
%{_mandir}/man1/hpsa_lsmplugin.1*
%dir %{python3_sitelib}/arcconf_plugin
%dir %{python3_sitelib}/arcconf_plugin/__pycache__
%{python3_sitelib}/arcconf_plugin/__pycache__/*
%{python3_sitelib}/arcconf_plugin/__init__.*
%{python3_sitelib}/arcconf_plugin/arcconf.*
%{python3_sitelib}/arcconf_plugin/utils.*
%dir %{python3_sitelib}/local_plugin
%dir %{python3_sitelib}/local_plugin/__pycache__
%{python3_sitelib}/local_plugin/__pycache__/*
%{python3_sitelib}/local_plugin/__init__.*
%{python3_sitelib}/local_plugin/local.*
%{_mandir}/man1/local_lsmplugin.1*
%dir %{python3_sitelib}/megaraid_plugin
%dir %{python3_sitelib}/megaraid_plugin/__pycache__
%{python3_sitelib}/megaraid_plugin/__pycache__/*
%{python3_sitelib}/megaraid_plugin/__init__.*
%{python3_sitelib}/megaraid_plugin/megaraid.*
%{python3_sitelib}/megaraid_plugin/utils.*
%{_mandir}/man1/megaraid_lsmplugin.1*
%dir %{python3_sitelib}/targetd_plugin
%dir %{python3_sitelib}/targetd_plugin/__pycache__
%{python3_sitelib}/targetd_plugin/__pycache__/*
%{python3_sitelib}/targetd_plugin/__init__.*
%{python3_sitelib}/targetd_plugin/targetd.*
%{_mandir}/man1/targetd_lsmplugin.1*

%files           udev
%defattr(-,root,root)
%{_udevrulesdir}/90-scsi-ua.rules
%{_udevrulesdir}/../scan-scsi-target
	
%files           nfs-plugin
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/nfs.conf
%{_bindir}/nfs_lsmplugin
%dir %{python3_sitearch}/nfs_plugin
%dir %{python3_sitearch}/nfs_plugin/__pycache__
%{python3_sitearch}/nfs_plugin/__pycache__/*
%{python3_sitearch}/nfs_plugin/__init__.*
%{python3_sitearch}/nfs_plugin/nfs.*
%{_mandir}/man1/nfs_lsmplugin.1*

%files          nfs-plugin-clibs
%{python3_sitearch}/nfs_plugin/nfs_clib.*

%files           help
%defattr(-,root,root)
%doc README NEWS
%{_mandir}/man*/*

%changelog
* Sat May 06 2023 yoo <sunyuechi@iscas.ac.cn> - 1.9.6-2
- fix clang build error

* Tue Feb 7 2023 xu_ping <xuping33@h-partners.com> - 1.9.6-1
- Upgrade 1.9.6

* Sat Jan 7 2023 mengwenhua <mengwenhua@xfusion.com> - 1.8.0-7
- Sim fs resize

* Fri Jan 28 2022 wulei <wulei80@huawei.com> - 1.8.0-6
- fix too many argument for format

* Mon Apr 25 2022 xigaoxinyan <xigaoxinyan@h-partners.com> - 1.8.0-5
- fix too many argument for format and libstoragemgmt: Upstream patch to avoid char usage in libstoragemgmt.

* Tue Sep 29 2020 baizhonggui <baizhonggui@huawei.com> - 1.8.0-4
- Modify source0

* Sat Mar 21 2020 songshuaishuai <songshuaishuai2@huawei.com> - 1.8.0-3
- fix update error 

* Mon Mar 16 2020 gulining<gulining1@huawei.com> - 1.8.0-2
- remove python2

* Sat Nov 9 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.8.0-1
- Package init
