# Generated from rspec-expectations-3.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rspec-expectations

Name:           rubygem-%{gem_name}
Version:        3.4.0
Release:        1%{?dist}
Summary:        rspec-expectations-3.4.0
Group:          Development/Languages
License:        MIT
URL:            http://github.com/rspec/rspec-expectations
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby >= 1.8.7

BuildArch: noarch
%if 0%{?rhel} > 0
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
rspec-expectations provides a simple, readable API to express expected
outcomes of a code example.


%package doc
Summary:        Documentation for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/.document
%doc %{gem_instdir}/Changelog.md
%doc %{gem_instdir}/README.md

%changelog
* Tue Dec 20 2016 Martin Mágr <mmagr@redhat.com> - 3.4.0-1
- Initial package
