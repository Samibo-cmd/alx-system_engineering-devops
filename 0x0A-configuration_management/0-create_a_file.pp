# Creating a file using Puppet.

file { '/tmp/school':
    content => 'Ilove Puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
}
