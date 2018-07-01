File.open('test.txt', "w") do |file|
    200_000.times{ |i| file.write("Line number #{i}\n") }
end
