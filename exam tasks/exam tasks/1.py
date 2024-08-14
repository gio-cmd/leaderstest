# Determine if a walk (given as an array of directions) takes exactly 10 minutes 
# and returns you to the starting point.

# Args:
# walk (list of str): List of one-letter direction strings ('n', 's', 'e', 'w').
# Each direction takes 1 minute (so list with length of 10 elements takes 10 minutes)

# Returns:
# bool: True if the walk is exactly 10 minutes and returns to start, False otherwise.

# Test Cases:
# ['w','e','w','e','w','e','w','e','w','e','w','e'] -> False
# ['n','s','n','s','n','s','n','s','n','s'] -> True
# ['n','n','n','s','n','s','n','s','n','s'] -> False
# ['e', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'] -> False
# ['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'] -> True


def walk_min(step):
    if len(step) != 10:
        return False
    
    south = 0
    north = 0
    east = 0
    west = 0

    
  
    for i in step:
        if i == 'n':
            north += 1
        elif i == 's':
            south += 1
        elif i == 'e':
            east += 1
        elif i == 'w':
            west += 1

    if south - north == 0 and east - west == 0:
        return True
    return False


print(walk_min(['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w']))