"""
Missing Socks
Given an integer representing the number of pairs of socks you started with, and another integer representing how many wash cycles you have gone through, return the number of complete pairs of socks you currently have using the following constraints:

Every 2 wash cycles, you lose a single sock.
Every 3 wash cycles, you find a single missing sock.
Every 5 wash cycles, a single sock is worn out and must be thrown away.
Every 10 wash cycles, you buy a pair of socks.
You can never have less than zero total socks.
Rules can overlap. For example, on wash cycle 10, you will lose a single sock, throw away a single sock, and buy a new pair of socks.
Return the number of complete pairs of socks.
"""
def sock_pairs(pairs, cycles):
    """
    Calculates the final number of complete sock pairs after a number of wash cycles,
    applying rules for losing, finding, and buying socks. Unmatched socks are discarded.
    """
    no_of_socks = pairs * 2

    # Loop runs for cycles 1 through 'cycles' (inclusive)
    for cycle in range(1, cycles + 1):
        
        # Apply Gains and Losses based on cycle number divisibility (Rules can overlap)
        
        # Every 2 cycles, lose 1 sock. (-1)
        if cycle % 2 == 0:
            no_of_socks -= 1
            
        # Every 3 cycles, find 1 sock. (+1)
        if cycle % 3 == 0:
            no_of_socks += 1
            
        # Every 5 cycles, throw away 1 sock. (-1)
        if cycle % 5 == 0:
            no_of_socks -= 1
            
        # Every 10 cycles, buy a pair of socks. (+2)
        if cycle % 10 == 0:
            no_of_socks += 2
            
        # Enforce Constraint: You can never have less than zero total socks.
        no_of_socks = max(0, no_of_socks)
            
        # Note: The 'pairs' calculation inside the loop is unnecessary for the final result
        # but is kept out of convention if needed for mid-cycle tracking. 
        # For efficiency, it's best to calculate 'pairs' only once at the end.
            
    # Calculate the total number of pairs
    # final_pairs = no_of_socks / 2
    # return int(final_pairs)
    
    
    # Return only the complete pairs by truncating the decimal (e.g., 3.5 becomes 3)
    return no_of_socks / 2 #int(final_pairs)

"""
1. sock_pairs(2, 5) should return 1.
2. sock_pairs(1, 2) should return 0.
3. sock_pairs(5, 11) should return 4.
4. sock_pairs(6, 25) should return 3.
5. sock_pairs(1, 8) should return 0.
"""
