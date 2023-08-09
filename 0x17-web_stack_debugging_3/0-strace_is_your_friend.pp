# fixes bad php extension in a wordpress bug
exec { 'fix_wordpress':
  command  => 'sed -i "s|.phpp|.php|g" /var/www/html/wp-settings.php',
  path     => ['/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
}
