marks = {
    "Aditi": 91,
    "Anshul": 83,
    "Juhi": 89,
    "Yashi": 90,
    "Garima": 75,
    "Shipra": 76
}
name = input("Enter the student's name: ")
if name in marks:
    print(f"{name}'s marks: {marks[name]}")
else:
    print(f"Student not found")