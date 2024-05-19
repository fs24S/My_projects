'''
Game PIG
Rules:
Player one chooses how many times he wants to roll the dice, then Player two chooses how many times he wants to.
All rolled dice are summed up and the player with the most points wins.
But if any of the players roll 1 then all points are deleted and sums of rolled dice equal 0.
'''
import itertools 
import random

print("Welcome to game named: PIG ")

player1: list[int] = []
player2: list[int] = []


while True:
	player_choice = itertools.cycle([1, 2])

	while True:
		current_player = next(player_choice)
		player_decision = int(input(f"Player {current_player} type how many time you want to roll: "))
		if current_player == 1:
			for roll_times in range(player_decision):
				roll = random.randint(1,6)
				player1.append(roll)
				suma = sum(player1)
			
			if 1 in player1:
				print(player1)
				print("0 pkt")
				player1 = []
			else:
				print(player1)
				print(suma)		

		if current_player == 2:
			for roll_times in range(player_decision):
				roll = random.randint(1,6)
				player2.append(roll)
				suma = sum(player2)
			
			if 1 in player2:
				print(player2)
				print("0 pkt")
				player2 = []
			else:
				print(player2)
				print(suma)
			break
	if sum(player1) > sum(player2):
		print("Player1 Win!")
	elif sum(player1) < sum(player2):
		print("Player2 Win!")
	elif sum(player1) == sum(player2):
		print("tie")

	again = input("Do you want to play again? (y/n): ")
	if again.lower() == "y":
		print("Lets play again!!")
		player1 = []
		player2 = []
	elif again.lower() == "n":
		break



