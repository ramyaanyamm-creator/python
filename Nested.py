if __name__ == '__main__':
    students=
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        students.append([name, score])

    grades = sorted(set([score for name, score in students]))
    second_lowest = grades[1]

    names = []

    for name, score in students:
        if score == second_lowest:
            names.append(name)

    names.sort()

    for name in names:
        print(name)
