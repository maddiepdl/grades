grade = int(input("Enter final grade: "))

if grade >= 90:
    print("Status: Honors")
elif grade >= 60:
    print("Status: Passed")
else:
    print("Status: Failed - Please contact the advisor.")