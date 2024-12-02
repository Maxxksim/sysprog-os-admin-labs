Name: counter
Version: 1.0
Release: 1%{?dist}
Summary: Скрипт для підрахунку файлів в каталозі /etc

License: GPL
Source0: counter.sh

%description
Скрипт для підрахунку файлів у каталозі /etc, виключаючи директорії та символічні посилання.

%prep

%build

%install
mkdir -p %{buildroot}/usr/local/bin
cp %{SOURCE0} %{buildroot}/usr/local/bin/counter.sh

%files
/usr/local/bin/counter.sh

%changelog
Fri Nov 29 2024 Developer <xackiiiii@gmail.com> - 1.0-1
- Initial package


