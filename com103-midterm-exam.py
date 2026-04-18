# Step 1: Player info
ign = input("Enter your IGN: ")

# Validate rank input
valid_rank = False
while valid_rank == False:
    rank = input("Enter your current rank (Epic, Legend, Mythic): ").lower()

    if rank == "epic" or rank == "legend" or rank == "mythic":
        rank = rank.capitalize()
        valid_rank = True
    else:
        print("Invalid rank. Try again (Epic, Legend, Mythic only).")

# Step 2: Hero roster
heroes = [
    ("Layla", "Marksman"),
    ("Tigreal", "Tank"),
    ("Gusion", "Assassin"),
    ("Kagura", "Mage"),
    ("Chou", "Fighter")
]

print("\nHero Roster:")
print("+----+----------+-----------+")
print("| No | Hero     | Role      |")
print("+----+----------+-----------+")

for i in range(len(heroes)):
    print(f"| {i+1:<2} | {heroes[i][0]:<8} | {heroes[i][1]:<9} |")

print("+----+----------+-----------+")

# Function to check numeric input (no isdigit)
def is_number(text):
    if text == "":
        return False

    for ch in text:
        if ch < '0' or ch > '9':
            return False
    return True

matches = []

# Step 3–4: Match entries
for match_num in range(1, 5):
    print(f"\nMatch {match_num}:")

    # HERO INPUT
    hero_valid = False
    while hero_valid == False:
        hero_input = input("Enter hero number (1–5) or 0 to skip: ")

        if is_number(hero_input):
            hero_num = int(hero_input)

            if hero_num >= 0 and hero_num <= 5:
                hero_valid = True
            else:
                print("Invalid number. Try again.")
        else:
            print("Invalid input. Numbers only. Try again.")

    if hero_num == 0:
        print("Match skipped.")
    else:
        hero_name = heroes[hero_num - 1][0]

        # KILLS
        kills_valid = False
        while kills_valid == False:
            kills_input = input("Kills: ")

            if is_number(kills_input):
                kills = int(kills_input)
                kills_valid = True
            else:
                print("Invalid input. Try again.")

        # DEATHS
        deaths_valid = False
        while deaths_valid == False:
            deaths_input = input("Deaths: ")

            if is_number(deaths_input):
                deaths = int(deaths_input)
                deaths_valid = True
            else:
                print("Invalid input. Try again.")

        # ASSISTS
        assists_valid = False
        while assists_valid == False:
            assists_input = input("Assists: ")

            if is_number(assists_input):
                assists = int(assists_input)
                assists_valid = True
            else:
                print("Invalid input. Try again.")

        # RESULT
        result_valid = False
        while result_valid == False:
            result_input = input("Result (W/L): ").lower()

            if result_input == "w" or result_input == "l":
                result = result_input.upper()
                result_valid = True
            else:
                print("Invalid input. Enter W or L only.")

        # KDA CALCULATION
        if deaths == 0:
            kda = (kills + assists) / 1
        else:
            kda = (kills + assists) / deaths

        # TAGGING
        if kda >= 5 and result == "W":
            tag = "DOMINATION!"
        elif kda >= 5 and result == "L":
            tag = "Carried Hard"
        elif kda < 5 and result == "W":
            tag = "Team Effort"
        else:
            tag = "Better Luck Next Game"

        matches.append({
            "hero": hero_name,
            "kda": kda,
            "result": result,
            "tag": tag
        })

        print(f"KDA: {kda:.2f} | {tag}")

# Step 5: Stats
wins = 0
losses = 0

for m in matches:
    if m["result"] == "W":
        wins = wins + 1
    else:
        losses = losses + 1

matches_played = len(matches)

if matches_played > 0:
    win_rate = int((wins / matches_played) * 100)
else:
    win_rate = 0

# Best match
best_index = -1
best_kda = 0

for i in range(len(matches)):
    if matches[i]["kda"] > best_kda:
        best_kda = matches[i]["kda"]
        best_index = i

# FINAL OUTPUT
print("\n===== MATCH LOG =====")
print(f"IGN: {ign}")
print(f"Rank: {rank}")

print("\n+--------+----------+--------+--------+------------------------+")
print("| Match  | Hero     | KDA    | Result | Tag                    |")
print("+--------+----------+--------+--------+------------------------+")

for i in range(len(matches)):
    m = matches[i]
    print(f"| {i+1:<6} | {m['hero']:<8} | {m['kda']:<6.2f} | {m['result']:<6} | {m['tag']:<22} |")

print("+--------+----------+--------+--------+------------------------+")

print(f"\nRecord: {wins} Wins - {losses} Losses")
print(f"Win Rate: {win_rate}%")

if best_index != -1:
    print(f"Best Match: Match {best_index + 1} with KDA {best_kda:.2f}")
else:
    print("No matches recorded.")