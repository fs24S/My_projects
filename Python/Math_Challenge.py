# Math Challenge
# Choose how many numbers you want to calculate 
# The program choose random numbers that many times that you provided and random choose + , - , *
# You need provide correct answer

import random
import time

numbers: list[int] = []
operators: list[str] = ["+","-","*"]
operator = random.randint(0,len(operators)-1)
calcu: list[int,str] = []

def random_number(numbers,how_many):
	for i in range(0, how_many):
		number: int = random.randint(1,10)
		numbers.append(number)

def addition():
	if operators[operator] == "+":
		print(*numbers, sep=" + ")
		suma: int = int(sum(numbers))
		correct_answer = suma
		correct(correct_answer)
		numbers.clear()

def subtraction():
	if operators[operator] == "-":
		odd: int = numbers[0]
		print(*numbers, sep=" - ")
		for i in range(1,len(numbers)):
			odd: int = int(odd - numbers[i])
		correct_answer = odd
		correct(correct_answer)
		numbers.clear()

def multiplication():
	if operators[operator] == "*":
		print(*numbers, sep=" * ")
		multi = 1
		for i in numbers:
			multi: int = int(multi * i)
		correct_answer = multi
		correct(correct_answer)
		numbers.clear()

def correct(correct_answer):
	while True:
		start = time.time()
		answer = input("= ")
		end = time.time()
		try:
			answer = int(answer)
			if int(answer) == int(correct_answer):
				print(f"You are correct! Correct answer is: {correct_answer} ")
				print(f"It took you {end - start:0.2f}s")
				break
			else:
				print(f"You are wrong! Correct answer is: {correct_answer} ")
				print(f"It took you {end - start:0.2f}s")
				break
		except ValueError:
			print("Please enter a valid integer.")

def decision():
	while True:
		how_many: int = input("How many number you want: ")
		try:
			how_many = int(how_many)
			if how_many > 1:
				return how_many
			else:
				print("Number must be greater than 1")
		except ValueError:
			print("Please enter a valid integer.")

def play_again():
	while True:
		choose = input("Do you want to play (y/n): ")
		if choose.lower() == "y":
			how_many = decision()
			random_number(numbers, how_many)
			addition()
			subtraction()
			multiplication()
		elif choose.lower() == "n":
			break

def main() -> None:
	play_again()

if __name__ == "__main__":
	main()
	