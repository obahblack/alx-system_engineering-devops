#!/usr/bin/env ruby
# Match "hbn hbtn hbttn hbtttn hbtttn not hbon"

puts ARGV[0].scan(/hbt*n/).join
