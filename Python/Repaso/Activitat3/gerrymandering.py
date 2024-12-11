def main():
    print("This program allows you to search through data about congressional voting districts")
    print("and determine whether a particular state is gerrymandered.")
    
    state_name = input("Which state do you want to look up? ").strip()
    districts_file = "districts.txt"
    voters_file = "eligible_voters.txt"

    districts_data = read_file(districts_file)
    state_districts = find_state_data(state_name, districts_data)
    
    if not state_districts:
        print(f'"{state_name}" not found.')
        return
    
    voters_data = read_file(voters_file)
    state_voters = find_state_data(state_name, voters_data)

    if not state_voters:
        print(f'Eligible voters data for "{state_name}" not found.')
        return
    
    wasted_dem, wasted_rep, total_votes = calculate_wasted_votes(state_districts)
    eligible_voters = int(state_voters.split(",")[1])
    
    print(f"Total Wasted Democratic votes: {wasted_dem}")
    print(f"Total Wasted Republican votes: {wasted_rep}")
    print(f"{eligible_voters} eligible voters")
    
    advantage = determine_gerrymandering(wasted_dem, wasted_rep, total_votes)
    if advantage:
        print(f"The {advantage} have gained an advantage from gerrymandering in {state_name}.")
    else:
        print(f"There is no significant gerrymandering in {state_name}.")

def read_file(filename):
    with open(filename, "r") as file:
        return file.readlines()

def find_state_data(state_name, data_lines):
    state_name_lower = state_name.lower()
    for line in data_lines:
        if line.split(",")[0].strip().lower() == state_name_lower:
            return line.strip()
    return None

def calculate_wasted_votes(state_data):
    data = state_data.split(",")[1:]
    wasted_dem, wasted_rep, total_votes = 0, 0, 0
    
    for i in range(0, len(data), 3):
        dem_votes = int(data[i + 1])
        rep_votes = int(data[i + 2])
        total_district_votes = dem_votes + rep_votes
        total_votes += total_district_votes

        winning_votes = (total_district_votes // 2) + 1
        if dem_votes > rep_votes:
            wasted_dem += dem_votes - winning_votes
            wasted_rep += rep_votes
        else:
            wasted_rep += rep_votes - winning_votes
            wasted_dem += dem_votes

    return wasted_dem, wasted_rep, total_votes

def determine_gerrymandering(wasted_dem, wasted_rep, total_votes):
    difference = abs(wasted_dem - wasted_rep)
    percentage = (difference / total_votes) * 100

    if percentage >= 7:
        return "Democrats" if wasted_dem > wasted_rep else "Republicans"
    return None

if __name__ == "__main__":
    main()
