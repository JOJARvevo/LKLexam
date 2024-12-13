contest_table = {}
teams_table = {}


def contest(name, year, count_tasks):
    global contest_table
    contest_table[name] = {"year": year, "count_tasks": count_tasks}
    return "Successes!"


def submit(team_name, contest_name, result):
    global teams_table
    if contest_name not in contest_table:
        return "Contest undetected, try again"
    accepted = []
    result = result.split()
    if len(result) > contest_table[contest_name]["count_tasks"]:
        return "Too many results, try again"
    if len(result) < contest_table[contest_name]["count_tasks"]:
        return "Too few results, try again"
    for i in range(len(result)):
        if len(result[i].strip("+").strip("-")) != 0:
            try:
                int(result[i].strip("+").strip("-"))
            except TypeError:
                return f"Wrong type of {chr(i + ord('A'))} task, try again"
        if result[i][0] == '+':
            accepted.append(i)
    if team_name not in teams_table:
        teams_table[team_name] = {"contests": {contest_name: {"result": result, "accepted": accepted}},
                                  "total_res": len(accepted)}
    else:
        teams_table[team_name]["contests"][contest_name] = {"result": result}
        teams_table[team_name]["total_res"] += len(accepted)
    return "Successes!"


def solved_amount(team_name):
    return teams_table[team_name]["total_res"]


def top(n, year_from, year_to):
    from_team_to_res = {}
    for contest_name in contest_table:
        if year_from <= contest_table[contest_name]["year"] <= year_to:
            for team_name in teams_table:
                if team_name not in from_team_to_res:
                    from_team_to_res[team_name] = len(teams_table[team_name]["contests"][contest_name]["accepted"])
                else:
                    from_team_to_res[team_name] += len(teams_table[team_name]["contests"][contest_name]["accepted"])
    answer = dict(sorted(from_team_to_res.items(), key=lambda x: [x[1], x[0]])).keys()[:n]
    if len(answer) < n:
        return "Too many teams to select! Try again please"
    return answer


def most_difficult(n, contest_name):
    if contest_name not in contest_table:
        return "Contest undetected, try again"
    from_id_to_total_count = {}
    for team_name in teams_table:
        for task_id in teams_table[team_name][contest_name]["accepted"]:
            if chr(task_id + ord('A')) not in from_id_to_total_count:
                from_id_to_total_count[chr(task_id + ord('A'))] = 1
            else:
                from_id_to_total_count[chr(task_id + ord('A'))] += 1
    answer = dict(sorted(from_id_to_total_count.items(), key=lambda x: [-x[1], x[0]])).keys()[:n]
    if len(answer) < n:
        return "Too many tasks to select! Try again please"
    return answer


def main():
    command = input().strip()
    while command != 'exit':
        content = command.split()
        command, values = content[0], content[1:]
        try:
            if command == "contest":
                print(contest(values[0], int(values[1]), int(values[2])))
            elif command == "submit":
                print(submit(values[0], values[1], " ".join(values[2:])))
            elif command == "statistic":
                if values[0] == "solved_amount":
                    print(solved_amount(values[1]))
                elif values[0] == "top":
                    print(*top(int(values[1]), int(values[2]), int(values[3])))
                elif values[0] == "most_difficult":
                    print(*most_difficult(int(values[1]), values[2]))
                else:
                    print("Unknown statistic command, please try again!")
            else:
                print("Unknown command, please try again!")
        except IndexError or TypeError:
            print("Wrong format of command")
        command = input()

    print("Goodbye!")


if __name__ == '__main__':
    main()
