draw = {
	'P':'♙',
	'T':'♖',
	'H':'♘',
	'B':'♗',
	'Q':'♕',
	'K':'♔',
	'_':' '
}

class ChessBoard:
	def __init__(self,pieces):
		self.positions = {}
		for i in pieces:
			strPos = str(i[0])+str(i[1])			
			self.positions[strPos] = i[2]
	def print(self):
		print("________________")
		for j in range(8):
			for i in range(8):
				keyPos = str(i)+str(j)
				print("|"+draw[self.positions.get(keyPos,"_")],end="")
			print("|")


def generatePieces():
	pieces = []
	for i in range(8):
		pieces.append([i,1,"P"])
		pieces.append([i,6,"P"])
	pieces.append([0,7,"T"])
	pieces.append([7,7,"T"])
	pieces.append([7,0,"T"])
	pieces.append([0,0,"T"])
	pieces.append([1,0,"H"])
	pieces.append([6,0,"H"])
	pieces.append([1,7,"H"])
	pieces.append([6,7,"H"])
	pieces.append([2,0,"B"])
	pieces.append([5,0,"B"])
	pieces.append([2,7,"B"])
	pieces.append([5,7,"B"])
	pieces.append([3,0,"K"])
	pieces.append([4,7,"K"])
	pieces.append([4,0,"Q"])
	pieces.append([3,7,"Q"])
	return pieces

CB = ChessBoard(generatePieces())
CB.print()
