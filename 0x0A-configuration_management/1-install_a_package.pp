# installing a package with puppet

exec { 'flask':
  command  => '/usr/bin/apt-get install flask -v 2.1.0',
}
