def add_match(results):
  match = input("Enter match result in following format - Team1 3:1 Team2 : ")
  
  try:
    team1, score, team2 = match.split()
    goals1, goals2 = score.split(":")
    
    if team1 not in results:
      results[team1] = {"wins":0, "losses": 0, "draws":0, "points":0}
    if team2 not in results:
      results[team2] = {"wins":0, "losses": 0, "draws":0, "points":0}
    
    if goals1>goals2:
      results[team1]["wins"] += 1
      results[team1]["points"] += 3
      results[team2]["losses"] += 1
    elif goals1<goals2:
      results[team2]["wins"] += 1
      results[team2]["points"] += 3
      results[team1]["losses"] += 1
    else:
      results[team1]["draws"] += 1
      results[team1]["points"] += 1
      results[team2]["draws"] += 1
      results[team2]["points"] += 1
  except ValueError:
    print("Invalid input format. Please try again. ")


def show_table(results):
    print("\nLeague Table:")
    print(f"{'Team':<15}{'Wins':<6}{'Losses':<8}{'Draws':<7}{'Points':<7}")
    for team, stats in sorted(results.items(), key=lambda x: x[1]['points'], reverse=True):
        print(f"{team:<15}{stats['wins']:<6}{stats['losses']:<8}{stats['draws']:<7}{stats['points']:<7}")

def main():
  results = {}
  while True:
    print("\n Menu: ")
    print("1. Add match result")
    print("2. Show league table")
    print("3. Exit")
    choice = input("Choose an option 1-3: ")
    
    if choice == "1":
      add_match(results)
    elif choice == "2":
      show_table(results)
    elif choice == "3":
      print('Exiting analyzer. Bye !')
      break
    else:
      print("Please choose valid option.")

if __name__ == "__main__":
  main()