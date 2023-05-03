#!/usr/bin/env ruby
# Match a 10 digit phone number 415736483448 without any dash

puts ARGV[0].scan(/^[0-9]{10}$/).join
