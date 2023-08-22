

```markdown
# Fantasy Cricket Team Selection using Genetic Algorithm

Welcome to the Fantasy Cricket Team Selection program! This project uses a powerful genetic algorithm to build your ideal cricket dream team for fantasy leagues. It optimizes team performance based on player scores, demand levels, and budget constraints while satisfying category requirements.

## How the Program Works

1. **Data Gathering:** Read player data from `Data.csv`, including name, category, player score, demand level, and last bid price.

2. **Player Scoring:** Calculate player score considering individual score, demand level, and bid price.

3. **Evaluating Team:** Assess team performance using total score, budget adherence, and category fulfillment.

4. **Genetic Algorithm:** Optimize team using crossover and mutation across generations.

5. **Best Individuals:** Select top teams based on fitness scores.

6. **Final Team Selection:** Choose best team, show selected players, categories, demand scores, and bid prices.

## Mathematical Insights

- **Player Score Formula:** Player score = PlayerScore * DemandScore * (1 / LastBidPrice).

- **Evaluation Function:** Maximize team score while minimizing penalties for budget and category deviations.

- **Genetic Algorithm:** Evolve teams using crossover and mutation to improve fitness scores.

## Getting Started

1. **Install Required Libraries:**
```

   pip install deap

```

2. **Prepare Player Data:** Create `Data.csv` with PlayerName, Category, PlayerScore, Demand, DemandScore, and LastBidPrice.

3. **Set Budget:** Modify `budget` variable in the code to your budget.

4. **Run the Program:**
```
