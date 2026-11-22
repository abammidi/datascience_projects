# Los Angeles Dodgers Attendance Analysis (2022)

Status: Completed (DSC 630 Week 3 assignment). The analysis covers one team and one season. See limitations below.

## Overview

This project uses the 2022 home-game data for the Los Angeles Dodgers (81 games) to look at what goes with attendance: day of week, month, opponent, temperature, sky conditions, day or night games, and giveaway promotions (cap, shirt, bobblehead, fireworks). It was written as a recommendation to team management.

## Contents

- `dodgers_attendance_analysis.ipynb`: the analysis notebook (descriptive summaries, promotion comparison, multiple linear regression). Outputs from the original run are included.
- `data/dodgers-2022.csv`: the game-level data (81 rows, 12 columns) provided with the assignment.

## Results

- Average attendance: about 41,000 (standard deviation about 8,300).
- Average attendance is lowest on Mondays (about 35,000) and Wednesdays (about 37,600), and highest on Tuesdays (about 47,700).
- Bobblehead games (11) averaged about 53,100, versus about 39,100 for the other 70 games.
- The multiple regression explains about 10% of attendance variation on the test set (R² ≈ 0.10; mean absolute error about 7,300).

## Recommendation

Test bobblehead promotions on weekday games with a controlled comparison before committing more of the promotion budget. The data does not show what bobbleheads would do on Mondays or Wednesdays, because none were held on those days.

## Known limitations

- **One team, one season.** The results describe the 2022 Dodgers home schedule, not MLB attendance in general. The data does not cover other teams, seasons, or away games.
- **Small samples.** Bobblehead games number 11, cap games 2, and shirt games 3. These estimates are not stable.
- **Weak model.** The regression explains about 10% of attendance variation, so its coefficients are directional only. Bobbleheads are not the largest coefficient in the model.
- **Confounding.** Promotions were not assigned at random. Promotions may have been scheduled for games that were expected to draw well.
- **Missing factors.** Ticket prices, marketing spend, team performance, and passenger-independent factors such as weather beyond temperature and sky conditions are not in the data.

<!-- CONTACT -->
## Contact

Anil Bammidi
Email: anil.bammidi@yahoo.com
LinkedIn: https://www.linkedin.com/in/anil-bammidi-43938357/
GitHub: https://github.com/abammidi
