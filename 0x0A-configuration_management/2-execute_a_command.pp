# 2-execute_a_command.pp
exec {'kill_killmenow_process':
    command => '/usr/bin/pkill -TERM -f "killmenow"',
    path    => ['/bin', '/usr/bin'],
}