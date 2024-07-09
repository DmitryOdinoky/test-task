# task2.py

def implied_probability(payout):
    """Calculate implied probability from payout."""
    return 1 / payout

def calculate_probabilities_and_margin(payouts):
    """Calculate the expected probabilities and the betting site's profit margin."""
    # Calculate implied probabilities
    implied_probs = {outcome: implied_probability(payout) for outcome, payout in payouts.items()}
    
    # Calculate total implied probability
    total_implied_prob = sum(implied_probs.values())
    
    # Normalize probabilities
    normalized_probs = {outcome: prob / total_implied_prob for outcome, prob in implied_probs.items()}
    
    # Calculate profit margin
    profit_margin = total_implied_prob - 1
    
    return normalized_probs, profit_margin

def main():
    # Given payouts
    payouts = {
        "TeamA_win": 1.2,
        "Draw": 19.2,
        "TeamB_win": 6.4
    }
    
    # Calculate probabilities and profit margin
    probabilities, margin = calculate_probabilities_and_margin(payouts)
    
    # Print the results
    print('=== Task 2 ===')
    print(f"Betting Site's Profit Margin: {margin:.4f}")
    print("Expected Probabilities:")
    for outcome, prob in probabilities.items():
        print(f"{outcome}: {prob:.4f}")
    
    
    print(" ")

if __name__ == "__main__":
    main()
