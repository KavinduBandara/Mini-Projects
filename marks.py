import statistics
def main():
    students = {}
    no_students = int(input("How many number of students? "))
    for _ in range(no_students):
        name = input(f"\nWhat's the student {_+1}?")
        while True:
            try:
                score = int(input("what's the score? "))
                if 0<= score <=100:
                    break
                else:
                    print("the score should be between 0 and 100")
                    break
            except ValueError:
                print("Enter a valid number")
        students[name] = score

    print("\n📊 Class Results:")
    for key, value in students.items():
        print(f"- {key}: {value}")
    scores = list(students.values())
    print(f"\n📈 Average score:{average(scores)}")
    max_name,  max_score = top_scorer(students)
    min_name,  min_score = min_scorer(students)
    print(f"🏆 Top Scorer: {max_name} ({max_score})")
    print(f"📉 Lowest Scorer: {min_name} ({min_score})")
    honours = []
    for names, score in students.items():
        if score >= 90:
            honours.append(names)
    if honours:
        print("\nHonours List is:",", ".join(honours))
    else:
        print("\nNot even a singele fucker got honours")








def average(scores):
    avg = sum(scores)/len(scores)
    return round(avg, 1)
def top_scorer(students):
    name = max(students, key=students.get)
    score = students[name]
    return name , score

def min_scorer(students):
    name= min(students, key=students.get)
    score = students[name]
    return name, score







main()
