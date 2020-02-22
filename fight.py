import os.path

file = input()

if not os.path.isfile(file):
    print ("Файл не существует")
else:

	f = open(file, 'r')
	line = f.readline()
	n = len(line) - 1
	sea = ["*" * n for i in range(n)]
	sea[0] = line[:-1]

	ships = 0

	for i in range(1, n):
		line = f.readline()
		sea[i] = line[:-1]

	for i in range(n):
		for j in range(n):
			el = sea[i][j]
			if el == '#':
				if i == 0 and (j == 0 or sea[i][j-1] != "#"):
					ships += 1
				elif j == 0 and sea[i-1][j] != "#":
					ships += 1
				elif sea[i][j-1] != '#' and sea[i-1][j] != "#":
					ships += 1
	print(ships)


