'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

'''
Plan:
    Look at the first two characters
    Shift the two character window over 1, checking if it is 'th'
        If it is return 1 (this will create a running count), if it isn't return nothing
    Do this recursively,
        At the end, call the method again and move dow the word 1 character
    Base Case:
        When we reach the end of the word
    Recursive Case:
        When we are not at the end, when the input word is at least 2 characters
        Traverse towards the base case by repeatedly taking off the first character every pass
'''
def count_th(word):
    # If the word doesn't contain 2 letters, it can't contain 'th'
    # Return 0
    if len(word) <2:
        return 0

    # Make sure the word is at least two characters long, if not stop running
    while len(word) > 1:
        # Look at the first two characters
        # If it is equal to 'th'
        if word[:2] == 'th':

            # Return 1 and continue to move towards the base case
            # Pass on the word minus the first character to the next call
            return 1 + count_th(word[1:])

        # Otherwise, it is not 'th' and just move towards the base case
        # Pass on the word minus the first character to the next cell
        else:
            return count_th(word[1:])
