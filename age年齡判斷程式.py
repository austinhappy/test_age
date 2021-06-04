# age年齡判斷程式
# 問是否開車及年齡，並給予建議，最後通過驗證

drive_or_not = input("Do you ever drive a car?")
if drive_or_not != "yes" and drive_or_not != "no":
	print("you just can enter yes or no.")
	raise SystemExit

age = int(input("How old are you?"))

if drive_or_not == "yes":
	if age >= 18:
		print("You pass the test!")
	else:
		print("Sound strange?")
elif drive_or_not == "no":
	if age >= 18:
		print("You can get the drive license and go on the road.")
	else:
		print("You are a good kid.")
else:
	print("you just can enter yes or no.")