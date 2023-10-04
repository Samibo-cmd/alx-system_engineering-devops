#!/usr/bin/env bash
#Connects without password using Puppet

file { '/etc/ssh/ssh_config':
     ensure => present,
}

file_line { 'Turn off password auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => '^#PasswordAuthentication',
}

file_line { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^#IdentityFile',
}
