sudoku = [

[0,0,0,2,6,0,7,0,1],
[6,8,0,0,7,0,0,9,0],
[1,9,0,0,0,4,5,0,0],
[8,2,0,1,0,0,0,4,0],
[0,0,4,6,0,2,9,0,0],
[0,5,0,0,0,3,0,2,8],
[0,0,9,3,0,0,0,7,4],
[0,4,0,0,5,0,0,3,6],
[7,0,3,0,1,8,0,0,0],

]


def blank(puz):
	for i in range(len(puz)):
		for j in range(len(puz[0])):
			if puz[i][j]==0:
				return(i, j)
	return None

def check(puz, piece, position):
	
	for i in range(len(puz)):
		if puz[i][position[1]]==piece and position[0]!=i:
			return False


	for i in range(len(puz[0])):
		if puz[position[0]][i]== piece and position[1]!=i :
			return False


	s = position[1]//3
	t = position[0]//3

	for i in range(t*3,(t*3+3)):
		for j in range(s*3,(s*3+3)):
			if puz[i][j]==piece and (i,j) != position:
				return False

	return True


def solve(puz):

	got = blank(puz)
	#print(got)
	if not got:
		return True
	else:
		row,col=got
	for i in range(1,10):
		if check(puz, i, (row,col)):
			puz[row][col]=i


			if solve(puz):
				return True

			puz[row][col]=0

	return False



def display(puz):
	for i in range(len(puz)):
		if (i%3)==0 and i!=0:
			print("__________________________")
			print("                          ")

		for j in range(len(puz[0])):
			if (j%3)==0:
				print(" | ",end="")

			if j==8:
				print(puz[i][j])
			else:
				t = str(puz[i][j])
				print(t+" ",end="")



display(sudoku)
print("                                                             "
		"                                                            ")
solve(sudoku)
print("\n\n*************Solved Sudoku*************\n\n")
display(sudoku)
