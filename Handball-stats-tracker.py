def track_match():
 playername="Malek"
 match_count=0

 
 
 while True:
 
 
  match_count=match_count+1
  assists=int(input("How many assists do you have"))
  turnovers=int(input("How many turnovers did you commit"))
  shots_taken=int(input("How many shots did you take"))
  goals_scored=int(input("how many goals did you score"))
  shooting_pct=round((goals_scored/shots_taken*100))
  print(f"{playername}'s shooting percentage is {shooting_pct}%")
  if shooting_pct>70:
     print("Excellent work")
  else:
          print("You need to sharpen your aim")
  print (f"{playername}'s match count is {match_count}")
  print(f"{playername}'s assist count is {assists}")
  print(f"{playername}'s turnovers count is {turnovers}")
  choice=input("Do you want to log another match? log/quit")
  if choice=="quit":
   break
  
    
track_match()
