def madlib():
    name1 = input("person: ")
    name2 = input("person: ")
    day1 = input("date: ")
    day2 = input("date: ")
    place = input("destination: ")
    activity1 = input("verb: ")
    activity2 = input("verb: ")
    adj1 = input("adjective: ")
    adj2 = input("adjective: ")

    madlib = f"I want to go with {name1} and {name2} to {place} from {day1} to {day2}.\
    We will {activity1} and {activity2}. I feel so {adj1} and {adj2}."

    print(madlib)
