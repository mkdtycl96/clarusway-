age = input("Are you a cigarette addict older than 75 years old?: ").title()
chronic = input("Dou you have a severe chronic disease?: ").title()
immune = input("Is your immune system too weak: ").title()
if age == "Yes" and chronic == "Yes" and immune == "Yes":
    print("very high risk of death")
elif age == "Yes" or chronic == "Yes" or immune == "Yes":
    print("You are in risky group")
elif age == "No" and chronic == "No" and immune == "No":
    print("you are not in risky group")       