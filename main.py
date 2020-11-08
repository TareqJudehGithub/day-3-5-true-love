# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print("")

your_name = name1.lower()
print("")
their_name = name2.lower()
print("")
total_strings = your_name + their_name

#TRUE count calculation:
t_count = total_strings.count("t") 
print(f"T occurs {t_count} times.")
print("")

r_count = total_strings.count("r")
print(f"R occurs {r_count} times.")
print("")

u_count = total_strings.count("u")
print(f"U occurs {u_count} times.")
print("")

e_count = total_strings.count("e")
print(f"E occurs {e_count} times.")
print("")

true_count = t_count + r_count + u_count + e_count
print("")
print(f"Total = {true_count}")
print("")
print("")

#LOVE count calculation:
l_count = total_strings.count("l")
print(f"L occurs {l_count} times.")
print("")

o_count = total_strings.count("o")
print(f"O occurs {o_count} times.")
print("")

v_count = total_strings.count("v")
print(f"V occurs {u_count} times.")
print("")

e_count = total_strings.count("e")
print(f"E occurs {e_count} times.")
print("")

love_count = l_count + o_count + v_count + e_count
print("")

print(f"Total = {love_count}")
print("")
print("")

# Final count combining true and love totals:
love_score = str(true_count) + str(love_count)

print(f"Your score is: {love_score}")

print("")
print("")

# Building condtionals based on score:
score = int(love_score)
print("")
if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")  
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")


