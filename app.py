import string


password = input("Enter Your password: ")

# Check for different character types
upper_case = any(c in string.ascii_uppercase for c in password)
lower_case = any(c in string.ascii_lowercase for c in password)
special = any(c in string.punctuation for c in password)
digits = any(c in string.digits for c in password)

characters = [upper_case, lower_case, digits, special]
length = len(password)
score = 0

# Check if password is in common passwords list
try:
    with open('common.txt', 'r') as f:
        common = f.read().splitlines()
    if password in common:
        print("❌ Password found in common list! Score: 0/7")
        exit()
except FileNotFoundError:
    print("⚠️ Warning: 'common.txt' file not found, skipping dictionary check.")

# Score calculation based on length
if length >= 8:
    score += 1
if length >= 12:
    score += 1
if length >= 17:
    score += 1
if length >= 20:
    score += 2

# Score calculation based on character variety
if sum(characters) > 1:
    score += 1
if sum(characters) > 2:
    score += 1
if sum(characters) > 3:
    score += 1


print(f"🔢 Password length: {length}, Score: {score} points!")

if length < 4:
    print(f"⚠️ Password is **very weak**! Score: {score}/7")
elif score == 4:
    print(f"✅ Password is **okay**! Score: {score}/7")
elif 4 < score < 6:
    print(f"✅ Password is **decent**! Score: {score}/7")
elif score >= 6:
    print(f"🔥 Password is **strong**! Score: {score}/7")
