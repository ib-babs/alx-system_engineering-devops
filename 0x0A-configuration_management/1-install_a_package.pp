# install_a_package.pp 'flask' using pip3

package { 'flask':
    ensure   => '2.1.0',
    provider => 'python3-pip'
}
