# install_a_package.pp
package {'python3-pip':
ensure => installed
}

exec {'1-install_a_package':
    command => '/usr/bin/pip3 install Flask==2.1.0',
    path    => '/usr/bin/',
    require => Package['python3-pip'],
}