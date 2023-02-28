#!/usr/bin/env ruby

m = ARGV[0].scan(/from:(\w+)...to:(\W+\d+)...flags:(.+\d)\]/)
puts "#{m.join(',')}"
