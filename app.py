import csv
from pulp import LpProblem, LpVariable, LpMaximize, lpSum

def read_data(filename):
    player_data = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player_data.append(row)
    return player_data

def calculate_player_score(player):
    player_score = float(player['PlayerScore'])
    demand_score = float(player['DemandScore'])
    last_bid_price = float(player['LastBidPrice'])
    
    return player_score * demand_score * (1 / last_bid_price)

def select_players(player_data, budget):
    selected_players = []
    total_price_paid = 0
    
    target_utilization = 0.9  # Adjust this as needed
    
    prob = LpProblem("PlayerSelection", LpMaximize)
    
    player_vars = LpVariable.dicts("Player", range(len(player_data)), cat="Binary")
    budget_constraint = budget >= lpSum(player_vars[p] * float(player_data[p]['LastBidPrice']) for p in range(len(player_data)))
    
    batsmen_count = 2
    all_rounder_count = 1
    wicketkeeper_count = 1
    pacers_count = 2
    spinners_count = 1
    
    prob += lpSum(player_vars[p] for p in range(len(player_data)) if player_data[p]['Category'] == 'Batsmen') == batsmen_count
    prob += lpSum(player_vars[p] for p in range(len(player_data)) if player_data[p]['Category'] == 'All rounders') == all_rounder_count
    prob += lpSum(player_vars[p] for p in range(len(player_data)) if player_data[p]['Category'] == 'Wicketkeeper') == wicketkeeper_count  # Corrected category name
    prob += lpSum(player_vars[p] for p in range(len(player_data)) if player_data[p]['Category'] == 'Pacers') == pacers_count
    prob += lpSum(player_vars[p] for p in range(len(player_data)) if player_data[p]['Category'] == 'Spinners') == spinners_count
    
    prob += lpSum(player_vars[p] * calculate_player_score(player_data[p]) for p in range(len(player_data)))
    prob += budget_constraint
    
    # Set a constraint for budget utilization
    prob += lpSum(player_vars[p] * float(player_data[p]['LastBidPrice']) for p in range(len(player_data))) <= budget * target_utilization
    
    prob.solve()
    
    for player_index, var in player_vars.items():
        if var.varValue == 1:
            selected_player = player_data[player_index]
            selected_players.append(selected_player)
            total_price_paid += float(selected_player['LastBidPrice'])
    
    return selected_players, total_price_paid

def main():
    filename = 'Data.csv'
    budget = 35.0  # Set the budget to 35
    
    player_data = read_data(filename)
    selected_players, total_price_paid = select_players(player_data, budget)
    
    print("\nSelected Players:")
    for player in selected_players:
        print(f"{player['PlayerName']} - {player['Category']} (Bid: ${float(player['LastBidPrice']):.2f})")
    
    print(f"\nTotal Price Paid for Selected Players: ${total_price_paid:.2f}")

if __name__ == "__main__":
    main()
