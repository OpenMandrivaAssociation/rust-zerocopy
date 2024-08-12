# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
%bcond_with check
%global debug_package %{nil}

%global crate zerocopy

Name:           rust-zerocopy
Version:        0.7.35
Release:        1
Summary:        Utilities for zero-copy parsing and serialization
Group:          Development/Rust

License:        BSD-2-Clause OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/zerocopy
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  (crate(byteorder) >= 1.3.0 with crate(byteorder) < 2.0.0~)
BuildRequires:  crate(zerocopy-derive/default) = 0.7.35
BuildRequires:  rust >= 1.60.0
%if %{with check}
BuildRequires:  (crate(assert_matches/default) >= 1.5.0 with crate(assert_matches/default) < 2.0.0~)
BuildRequires:  (crate(elain/default) >= 0.3.0 with crate(elain/default) < 0.4.0~)
BuildRequires:  (crate(itertools/default) >= 0.11.0 with crate(itertools/default) < 0.12.0~)
BuildRequires:  (crate(rand/default) >= 0.8.5 with crate(rand/default) < 0.9.0~)
BuildRequires:  (crate(rand/small_rng) >= 0.8.5 with crate(rand/small_rng) < 0.9.0~)
BuildRequires:  (crate(rustversion/default) >= 1.0.0 with crate(rustversion/default) < 2.0.0~)
BuildRequires:  (crate(static_assertions/default) >= 1.1.0 with crate(static_assertions/default) < 2.0.0~)
BuildRequires:  crate(trybuild/default) = 1.0.85
BuildRequires:  crate(trybuild/diff) = 1.0.85
%endif

%global _description %{expand:
Utilities for zero-copy parsing and serialization.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(zerocopy) = 0.7.35
Requires:       cargo
Requires:       crate(zerocopy-derive/default) = 0.7.35
Requires:       rust >= 1.60.0

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-BSD
%license %{crate_instdir}/LICENSE-MIT
%license %{crate_instdir}/src/third_party/rust/LICENSE-APACHE
%license %{crate_instdir}/src/third_party/rust/LICENSE-MIT
%doc %{crate_instdir}/CONTRIBUTING.md
%doc %{crate_instdir}/INTERNAL.md
%doc %{crate_instdir}/POLICIES.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(zerocopy/default) = 0.7.35
Requires:       cargo
Requires:       crate(zerocopy) = 0.7.35
Requires:       crate(zerocopy/byteorder) = 0.7.35

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+__internal_use_only_features_that_work_on_stable-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(zerocopy/__internal_use_only_features_that_work_on_stable) = 0.7.35
Requires:       cargo
Requires:       crate(zerocopy) = 0.7.35
Requires:       crate(zerocopy/alloc) = 0.7.35
Requires:       crate(zerocopy/derive) = 0.7.35
Requires:       crate(zerocopy/simd) = 0.7.35

%description -n %{name}+__internal_use_only_features_that_work_on_stable-devel %{_description}

This package contains library source intended for building other packages which
use the "__internal_use_only_features_that_work_on_stable" feature of the "%{crate}" crate.

%files       -n %{name}+__internal_use_only_features_that_work_on_stable-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(zerocopy/alloc) = 0.7.35
Requires:       cargo
Requires:       crate(zerocopy) = 0.7.35

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+byteorder-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(zerocopy/byteorder) = 0.7.35
Requires:       (crate(byteorder) >= 1.3.0 with crate(byteorder) < 2.0.0~)
Requires:       cargo
Requires:       crate(zerocopy) = 0.7.35

%description -n %{name}+byteorder-devel %{_description}

This package contains library source intended for building other packages which
use the "byteorder" feature of the "%{crate}" crate.

%files       -n %{name}+byteorder-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+derive-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(zerocopy/derive) = 0.7.35
Requires:       cargo
Requires:       crate(zerocopy) = 0.7.35
Requires:       crate(zerocopy/zerocopy-derive) = 0.7.35

%description -n %{name}+derive-devel %{_description}

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%files       -n %{name}+derive-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+simd-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(zerocopy/simd) = 0.7.35
Requires:       cargo
Requires:       crate(zerocopy) = 0.7.35

%description -n %{name}+simd-devel %{_description}

This package contains library source intended for building other packages which
use the "simd" feature of the "%{crate}" crate.

%files       -n %{name}+simd-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+simd-nightly-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(zerocopy/simd-nightly) = 0.7.35
Requires:       cargo
Requires:       crate(zerocopy) = 0.7.35
Requires:       crate(zerocopy/simd) = 0.7.35

%description -n %{name}+simd-nightly-devel %{_description}

This package contains library source intended for building other packages which
use the "simd-nightly" feature of the "%{crate}" crate.

%files       -n %{name}+simd-nightly-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+zerocopy-derive-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(zerocopy/zerocopy-derive) = 0.7.35
Requires:       cargo
Requires:       crate(zerocopy) = 0.7.35
Requires:       crate(zerocopy-derive/default) = 0.7.35

%description -n %{name}+zerocopy-derive-devel %{_description}

This package contains library source intended for building other packages which
use the "zerocopy-derive" feature of the "%{crate}" crate.

%files       -n %{name}+zerocopy-derive-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
