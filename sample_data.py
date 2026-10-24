
result = input("Enter your result: ")
result = int(result)

if result >= 90:
    print("The result", result, "is of grade A+")
elif result >= 85:
    print("The result", result, "is of grade A")
elif result >= 83:
    print("The result", result, "is of grade A-")
elif result >= 75:
    print("The result", result, "is of grade B+")
elif result >= 70:
    print("The result", result, "is of grade B")
elif result >= 68:
    print("The result", result, "is of grade B-")
elif result >= 50:
    print("The result", result, "is of grade C+")
elif result >= 45:
    print("The result", result, "is of grade C-")
elif result >= 30:
    print("The result", result, "is of grade D")
else:
    print("The result", result, "is of grade F")
