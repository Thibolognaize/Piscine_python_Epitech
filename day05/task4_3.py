meetings = [
    ["Monday", "3:30 PM", "Joe", "Sam"],
    ["Monday", "4:30 PM", "Bob", "Alice"],
    ["Tuesday", "3:30 PM", "Joe", "Bob", "Alice", "Sam"],
    ["Tuesday", "9:30 AM", "Joe", "Bob"],
]

usr_name = input("Give me your name to know your meetings:\n").capitalize()
for meeting in meetings:
    day = meeting[0]
    time = meeting[1]
    names = meeting[2::]
    if usr_name in names:
        print(f"You have a meeting the {day} at {time}")
