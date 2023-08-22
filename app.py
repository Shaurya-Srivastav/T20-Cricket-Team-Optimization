# Import necessary libraries
import csv
import random
from deap import base, creator, tools, algorithms

# Function to read player data from a CSV file
def read_data(filename):
    player_data = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player_data.append(row)
    return player_data

# Function to calculate the player score based on various factors
def calculate_player_score(player):
    player_score = float(player['PlayerScore'])
    demand_score = float(player['DemandScore'])
    last_bid_price = float(player['LastBidPrice'])
    
    return player_score * demand_score * (1 / last_bid_price)

# Function to evaluate the performance of a team
def evaluate_team(individual, player_data, budget):
    total_price = 0
    total_score = 0
    category_counts = {'Batsmen': 0, 'All rounders': 0, 'Wicketkeeper': 0, 'Pacers': 0, 'Spinners': 0}
    
    # Calculate total price, score, and count players in each category
    for i, selected in enumerate(individual):
        if selected:
            player = player_data[i]
            total_price += float(player['LastBidPrice'])
            total_score += calculate_player_score(player)
            category_counts[player['Category']] += 1
            
    # Calculate penalties for exceeding budget and category count
    penalty = max(0, total_price - budget)
    
    category_penalty = 0
    for category, count in category_counts.items():
        diff = abs(count - CATEGORY_REQUIREMENTS[category])
        category_penalty += diff
    
    # Combine total score, penalty, and category penalty
    return total_score - penalty - category_penalty * 100,  # Adjusted penalty weight

# Function to use a genetic algorithm to select players based on performance and budget
def select_players_genetic(player_data, budget):
    # Define the fitness function to be maximized (higher is better)
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)
    
    toolbox = base.Toolbox()
    
    # Create the individual representation (binary representation)
    n_players = len(player_data)
    toolbox.register("attr_bool", random.randint, 0, 1)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n_players)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    
    # Define genetic operators
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("evaluate", evaluate_team, player_data=player_data, budget=budget)
    
    # Set genetic algorithm parameters
    population_size = 100
    generations = 50
    
    # Initialize the population of individuals
    population = toolbox.population(n=population_size)
    
    # Apply the genetic algorithm to evolve the population
    algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=generations, verbose=False)
    
    # Select the best individual from the evolved population
    best_individual = tools.selBest(population, k=1)[0]
    selected_players = [player_data[i] for i, selected in enumerate(best_individual) if selected]
    total_price_paid = sum(float(player['LastBidPrice']) for player in selected_players)
    
    return selected_players, total_price_paid

# Define the required number of players in each category
CATEGORY_REQUIREMENTS = {'Batsmen': 2, 'All rounders': 1, 'Wicketkeeper': 1, 'Pacers': 2, 'Spinners': 1}

# Main function to run the player selection process
def main():
    filename = 'Data.csv'
    budget = 35.0  # Set the budget to 35
    
    # Read player data from the CSV file
    player_data = read_data(filename)
    
    # Select the best players using the genetic algorithm
    selected_players, total_price_paid = select_players_genetic(player_data, budget)
    
    # Display the selected players and total price paid
    print("\nSelected Players:")
    for player in selected_players:
        print(f"{player['PlayerName']} - {player['Category']} (Demand: {player['DemandScore']}, Bid: ${float(player['LastBidPrice']):.2f})")
    
    print(f"\nTotal Price Paid for Selected Players: ${total_price_paid:.2f}")

# Execute the main function if this script is run as the main module
if __name__ == "__main__":
    main()
