# Let consider a list of meetings. Each meeting is a list containing the day, the time of the meeting and the
# name of all the participants.
# Write a program that, given a name, displays all the day and the time of all meetings in which this person
# is involved
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
