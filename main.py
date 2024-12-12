def detecter():
    # Open the file and read the team data
    file = open("list1.txt", "r")
    team_data = {}

    for line in file:
        team_name, years_str = line.strip().split(" =")
        # Remove brackets, split by commas, and convert to integers
        years = [int(year) for year in years_str[1:-1].split(',')]
        team_data[team_name] = years

    file.close()
    return team_data


def main():
    team_data = detecter()
    team_name = input("Enter the team name: ").strip()

    if team_name in team_data:
        years_won = team_data[team_name]
        print(f"{team_name} won in the following years: {years_won}")
        print(f"Total number of wins: {len(years_won)}")
    else:
        print("Team not found.")


# Run the program
main()


def main():
    detecter()

main()



