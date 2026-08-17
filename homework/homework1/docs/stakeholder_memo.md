# Stock Market Leverage Trading Model
**Stage:** Problem Framing & Scoping (Stage 01) 
## Problem Statement 
Leverage can be used to amplify returns but can also lead to severe losses. This project examines whether recent market price movements and expected volatility can be used to determine an appropriate amount of leverage to maximize risk-adjusted returns. 
## Stakeholder & User
The stakeholders and users are active traders or portfolio managers. 
## Useful Answer & Decision 
The answer is predictive, as the model outputs the optimal amount of leverage to use. 
## Assumptions & Constraints 
- The project assumes historical data is available for the S&P 500 and VIX
- Trading is done using the S&P 500 index, with leverage between 0-2
- The model's strategy should account for transaction costs and trading costs
## Known Unknowns / Risks 
- Relationship between recent price data, VIX, and expected return may not be constant
- Overfitting should be avoided using out-of-sample testing

## Lifecycle Mapping 
Goal → Stage → Deliverable 
- Define the problem and objective -> Framing & Scoping (Stage 01) -> Stakeholder memo
## Repo Plan 
data/ - historical stock market data
src/ - trading model
notebooks/ - data analysis
docs/ - documentation
Weekly updates