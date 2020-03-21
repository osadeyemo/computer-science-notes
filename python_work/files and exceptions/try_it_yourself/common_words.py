filenames = ['the_good_work.txt', 'virgin_ground.txt', 'growing_season.txt']

for filename in filenames:
	try:
		with open(filename) as f:
			contents = f.read()
			word_count = (contents.lower().count('the '))
			print(f"The word 'the' appreaded in {filename} {word_count} times.")
	except FileNotFoundError:
		print(f"Sorry, I can't find {filename} file.")