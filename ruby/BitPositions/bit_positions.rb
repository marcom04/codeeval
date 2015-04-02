# https://www.codeeval.com/open_challenges/19/

File.open(ARGV[0], 'r').each_line do |line|
	args = line.split(',')
	n = args[0].to_i
	p1 = args[1].to_i - 1
	p2 = args[2].to_i - 1

	puts (n[p1] == n[p2]) ? 'true' : 'false'
end
