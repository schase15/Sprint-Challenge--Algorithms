# Sprint challenge egg drop problem

'''
Plan:
    Use binary search to find the first floor that the egg cracks on 
'''

def egg_drop(n):
    # n is the number of floors in the building

    # Set low and high range of search
    high = n -1
    low = 0

    # Continue running until there are only two floors left
    while high - low > 1:   # O(log n)

        # Calculate the midpoint
        mid = (high - low)//2

        # Drop the egg from the midpoint
        egg.drop(mid)

        # See if the egg survives
        # if it does, f is not included
        if egg.crack() == False:
            # Toss out the lower portion of the building
            low = mid +1

        # If the egg cracks
        if egg.crack() == True:
            # Keep the lowest floor it cracks on, that could be f
            high = mid
    
    # After it has been narrowed down to two floors to drop from 
    
    # Drop the egg from the lower floor
    egg.drop(low)

    # If it cracks, that is f
    if egg.crack() == True:
        f = low
        return f

    # If it doesn't crack, it was the floor above it that is f
    if egg.crack() == False:
        f = high
        return f


