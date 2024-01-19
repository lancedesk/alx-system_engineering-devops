# Manifest that kills a process named killmenow using Puppet.

exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
  onlyif  => '/usr/bin/pgrep -f killmenow',
  path    => '/usr/bin',
}
