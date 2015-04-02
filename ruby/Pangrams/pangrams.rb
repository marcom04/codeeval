# https://www.codeeval.com/open_challenges/37/

File.open(ARGV[0], 'r').each_line do |line|
	alphabet = Hash[('a'..'z').map { |letter| [letter, 0] }]
	line.each_char do |letter|
		if letter =~ /[[:alpha:]]/
			alphabet[letter.downcase] = 1
		end
	end
	sum = alphabet.values.inject(0) { |a, b| a + b }
	if sum == 26
		puts "NULL"
	else
		puts alphabet.select{ |k, v| v == 0 }.keys.join
	end
end
