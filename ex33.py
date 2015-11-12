def count(number, add):
	i = 0
	numbers = []

	while i < number:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + add
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i


	print "The numbers: "

	for num in numbers:
		print num

# count(15,3)
# $ python -c 'import ex33; print ex33.count(15,3)'