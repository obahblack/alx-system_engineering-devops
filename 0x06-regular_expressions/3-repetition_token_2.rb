#!/usr/bin/env ruby
# Match "hbtn, hbttn, hbtttn, hbttttn"

puts ARGV[0].scan(/hbt+n/).join
