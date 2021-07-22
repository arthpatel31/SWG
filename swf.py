import random

i = 0
j = 0
k = 0
while i < 5:
    print("Enter Snake: s\n"
          "Water: w\n"
          "Gun: g"
          )
    a = input()
    # print(a)
    t = ["s", "w", "g"]
    b = random.choice(t)
    while a == b:
        b = random.choice(t)
    print(b)
    if (a == "s" and b == "w") or (a == "w" and b == "g") or (a == "g" and b == "s"):
        j = j + 1
        print("Player 1 wins")
    elif (b == "s" and a == "w") or (b == "w" and a == "g") or (b == "g" and a == "s"):
        k = k + 1
        print("Player 2 wins")
    i = i + 1
if j > k:
    print("\n")
    print("Player 1 is final winner")
else:
    print("\n")
    print("Player 2 is final winner")
print(j, k)
