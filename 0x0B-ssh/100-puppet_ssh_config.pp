# setup your ssh config file with puppet
file_line { 'Turn off password auth':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => '    passwordAuthentication no',
  }
file_line { 'Declare identity file':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/school',
  }
