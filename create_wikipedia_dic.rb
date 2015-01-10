#!/usr/bin/ruby
# original: http://tmp.blogdns.org/archives/2009/12/mecabwikipediah.html
require 'kconv'

open($*[0]).each do |line|
  title = line.strip
  next if title.size < 2
  next if title =~ /^\./
  next if title =~ /,/
  next if title =~ /[0-9]{4}/
  next if title =~ /^[-.0-9]+$/
  score = [-36000, (-400 *(title.size**1.5))].max.to_i
  out = "#{title},0,0,#{score},名詞,一般,*,*,*,*,#{title.downcase},*,*,Wikipediaキーワード,\n"
  print out.toeuc
end

