#Initial ELO
elo_a = int(input("Enter Player A's ELO: "))
while elo_a<1000:
    elo_a = int(input("ELO Must be above 1000. Enter Player A's ELO: "))
elo_b = int(input("Enter Player B's ELO: "))
while elo_b<1000:
    elo_b = int(input("ELO Must be above 1000. Enter Player B's ELO: "))

#Determine k

k = 64

#Determine result
games_a = int(input("How many games did A win: "))
while games_a<0 or games_a>3:
    games_a = int(input("How many games did A win: "))

games_b = int(input("How many games did B win: "))
while games_b<0 or games_b>3:
    games_b = int(input("How many games did B win: "))

while games_a+games_b > 5 or games_a != 3 and games_b != 3:
    games_a = int(input("How many games did A win: "))
    while games_a<0 or games_a>3:
        games_a = int(input("How many games did A win: "))
    games_b = int(input("How many games did B win: "))
    while games_b<0 or games_b>3:
        games_b = int(input("How many games did B win: "))


s_a = games_a/(games_b+games_a)
s_b = games_b/(games_a+games_b)

#Update Elo
expected_a = 1/(1+10**((elo_b-elo_a)/400))
expected_b = 1/(1+10**((elo_a-elo_b)/400))

elo_a = max(round(elo_a + k*(s_a-expected_a)),1000)
elo_b = max(round(elo_b + k*(s_b-expected_b)),1000)
print("A's new ELO is ", elo_a, " and B's new ELO is ",elo_b)