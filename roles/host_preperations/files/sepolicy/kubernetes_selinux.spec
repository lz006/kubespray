# vim: sw=4:ts=4:et


%define selinux_policyver 3.13.1-229

Name:   kubernetes_selinux
Version:	1.0
Release:	1%{?dist}
Summary:	SELinux policy module extending container_t for kubernetes usage

Group:	System Environment/Base		
License:	GPLv2+	
# This is an example. You will need to change it.
URL:		http://HOSTNAME
Source0:	kubernetes.pp


Requires: policycoreutils, libselinux-utils
Requires(post): selinux-policy-base >= %{selinux_policyver}, policycoreutils
Requires(postun): policycoreutils
BuildArch: noarch

%description
This package installs and sets up the  SELinux policy security module for kubernetes.

%install
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}%{_datadir}/selinux/devel/include/contrib


%post
semodule -n -i %{_datadir}/selinux/packages/kubernetes.pp
if /usr/sbin/selinuxenabled ; then
    /usr/sbin/load_policy

fi;
exit 0

%postun
if [ $1 -eq 0 ]; then
    semodule -n -r kubernetes
    if /usr/sbin/selinuxenabled ; then
       /usr/sbin/load_policy

    fi;
fi;
exit 0

%files
%attr(0600,root,root) %{_datadir}/selinux/packages/kubernetes.pp


%changelog
* Mon Jan 13 2020 Lucas Zanella <lucas.zanella@sulzer.de> 1.0-1
- Initial version

