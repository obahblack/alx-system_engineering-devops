# Creates a manifest that kills a process
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin',
  returns => [0, 1],  # Allow exit status 0 and 1
}
