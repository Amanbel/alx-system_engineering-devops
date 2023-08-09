# installing a package with puppet

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
}
