contest_table = {}
teams_table = {}


def contest(name, year, count_tasks):
    global contest_table
    contest_table[name] = {"year": year, "count_tasks": count_tasks}
    return "Successes!"


def submit(team_name, contest_name, result):
    global teams_table
    if team_name not in teams_table:
        teams_table[team_name] = {"contests": {contest_name: {"result": result}},
                                  "total_res": result.count("+")}
    else:
        teams_table[team_name]["contests"][contest_name] = {"result": result}
        teams_table[team_name]["total_res"] += result.count("+")
    return "Successes!"


def solved_amount(team_name):
    return teams_table[team_name]["total_res"]


def top(n, year_from, year_to):
    pass


def most_difficult(n, contest_name):
    pass


def main():
    command = input().strip()
    while command != 'exit':
        content = command.split()
        command, values = content[0], content[1:]
        if command == "contest":
            print(contest(values[0], int(values[1]), int(values[2])))
        elif command == "submit":
            print(submit(values[0], values[1], " ".join(values[2:])))
        elif command == "statistic":
            if values[0] == "solved_amount":
                print(solved_amount(values[1]))
            elif values[0] == "top":
                print(top(int(values[1]), int(values[2]), int(values[3])))
            elif values[0] == "most_difficult":
                print(most_difficult(int(values[1]), values[2]))
            else:
                print("Unknown statistic command, please try again!")
        else:
            print("Unknown command, please try again!")
        command = input()
    print("Goodbye!")


if __name__ == '__main__':
    main()
