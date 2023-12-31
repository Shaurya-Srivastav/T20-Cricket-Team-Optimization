# Fantasy Cricket Team Selection using Genetic Algorithm

Welcome to the Fantasy Cricket Team Selection program! This project utilizes a powerful genetic algorithm to help you build your ideal cricket dream team for fantasy leagues. By considering player scores, demand levels, and budget constraints, this algorithm aims to optimize your team's overall performance while satisfying specific category requirements.

## Table of Contents

- [Introduction](#introduction)
- [How the Program Works](#how-the-program-works)
- [Mathematical Insights](#mathematical-insights)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration](#configuration)
- [Results](#results)
- [License](#license)

## Introduction

Fantasy cricket is an engaging pastime that allows you to create a virtual team of real cricket players. This project introduces a data-driven approach to help you select players for your fantasy team using a genetic algorithm. The algorithm optimizes player selection based on their past performance, demand levels, and your budget.

## How the Program Works

1. **Data Gathering:** The program starts by collecting player data from a CSV file named `Data.csv`. This dataset comprises crucial details about each player, including their name, category, player score, demand level, and last bid price.
2. **Player Scoring:** A sophisticated scoring function is designed to compute a player's score. This score takes into account the player's individual score, demand level, and last bid price. A higher calculated score reflects a player's potential to make a significant impact on the team's performance.
3. **Evaluating Team Performance:** An evaluation function is employed to assess the overall performance of a team. This function factors in various criteria, including the total team score, adherence to the budget, and fulfillment of category requirements.
4. **Genetic Algorithm Framework:** The core of the program revolves around a genetic algorithm. This algorithm searches for the best combination of players that maximizes the team's score while respecting budget constraints and category mandates. The algorithm continuously evolves a group of possible solutions (teams) over multiple generations.
5. **Genetic Operators:** The genetic algorithm employs two primary operators:

   - Crossover (`mate`): This operation merges the traits of two individuals (teams) to create new ones.
   - Mutation (`mutate`): Random modifications to an individual's traits introduce variety within the population.
6. **Selecting the Optimal Individuals:** After numerous generations, the genetic algorithm identifies the most promising individuals (teams) based on their fitness scores. These scores are determined using the evaluation function, which encompasses player scores, budget, and category stipulations.
7. **Final Team Selection:** The best individual from the final generation is deemed the optimal team. The program retrieves the player data for the selected players and computes the total amount spent on their bids.

## Mathematical Insights

- **Player Scoring Formula:** Player score = PlayerScore * DemandScore * (1 / LastBidPrice)
  This formula combines a player's skill (PlayerScore), demand level (DemandScore), and budget efficiency (1 / LastBidPrice) into a unified score.
- **Evaluation Function:** The evaluation function evaluates team performance by considering:

  - Total team score
  - Penalties for exceeding the budget
  - Penalties for failing to meet category requirements
    The objective is to maximize the team's score while minimizing penalties.
- **Genetic Algorithm:** The algorithm leverages crossover and mutation operations to generate new teams. Selection privileges individuals with higher fitness scores. Over successive iterations, the algorithm fine-tunes teams for better scores and greater compliance with constraints.

## Getting Started

1. **Install Required Libraries: pip install deap**
2. **Prepare Player Data:** Create a CSV file (`Data.csv`) containing player information, including PlayerName, Category, PlayerScore, Demand, DemandScore, and LastBidPrice.
3. **Set Budget:** Adjust the `budget` variable in the code to your desired budget.
4. **Run the Program:**
5. **View Selected Players:** The program will display the selected players, their categories, demand scores, and bid prices.

## Usage

1. **Installing Dependencies:** Before running the program, install the required `deap` library using the command: Pip install deap
2. **Prepare Player Data:** Create a CSV file named `Data.csv` with player information, including:

- PlayerName
- Category
- PlayerScore
- Demand
- DemandScore
- LastBidPrice

3. **Configure Your Budget:** Open the program file and adjust the `budget` variable to match your available budget.
4. **Run the Program:** Open your terminal/command prompt and execute the program using the command:

   python your_program_name.py
5. **View Selected Players:** The program will display the selected players, their categories, demand scores, and bid prices.

   ## Usage


   1. **Installing Dependencies:** Before running the program, install the required `deap` library using the command:
      Pip install deap
   2. **Prepare Player Data:** Create a CSV file named `Data.csv` with player information, including:

   - PlayerName
   - Category
   - PlayerScore
   - Demand
   - DemandScore
   - LastBidPrice

   3. **Configure Your Budget:** Open the program file and adjust the `budget` variable to match your available budget.
   4. **Run the Program:** Open your terminal/command prompt and execute the program using the command: python your_program_name.py
