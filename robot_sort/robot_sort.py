'''
Understand:
    Use the pre-defined methods and robot class
    Finish the sort method using the pre-defined methods
        Return a sorted list in ascending order
    Can not save any variables or call attribute directly, just use method calls
    Can create helper methods if needed, as long as they follow the rules
'''


class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    '''
    Plan:
        Utilize the logic of bubble sort
        Start at the front, have the robot pick up the first item
            Move to the next item
            Compare the item in his hand to the item in front of him
            If it is greater than what he's holding, pick it up. Put the one he's holding down. 
            Continue down the line until he reaches the end.

        Use the light to indicate when the list has been completely sorted, turn the light on when swaps occur

        Stop the sorting when the robot reaches the end of the list and his light hasn't been turned on (no swaps have occured)

        ** To cut time in half, have the robot sort as he traverses back down the list moving left

        ** Picking up an item leaves a blank spot. As the list gets sorted from the front, the blank spot gets
        moved up. Creating a boundary, everything to the left of the blank spot has been sorted.
            Use that logic to stop the robot from having to traverse all the way back to the front everytime
    '''

    def sort(self):
        """
        Sort the robot's list.
        """
        # Base Case
        # If the robot has reached the end of the list and his light is off (no swaps have occurred),
        if self.can_move_right() == False and self.light_is_on() == False:
            return

        # Grab the first card
        self.swap_item()

        # While the robot is still able to move right,
        while self.can_move_right():

            # Move right
            self.move_right()

            # Compare the item in his hand to that in front of him
            # If the item in front of him is greater than what he is holding (-1), swap items
            if self.compare_item() == -1:
                # Swap the item
                self.swap_item()
                # Turn his light on to indicate that a swap has occured
                self.set_light_on()
            
        # Once the robot can no longer move right, he is at the end of the list and holding the largest value
        # Swap items
        self.swap_item()

        # Now the robot needs to traverse back to index 0, grabbing the smallest value as he goes
            # Follow the same logic as when he moved right with the largest value

        # If he hits a empty slot in the list, everything in front of it has been sorted
        # He doesn't need to sort anymore, he is holding the smallest value left to be sorted. 
        # Put it in the blank spot and turn to move back in the other direction

        while self.compare_item() is not None:

            # Move left
            self.move_left()

            # Compare the item in his hand to that in front of him
            # If the item in front of him is less than what he is holding (1), swap items
            if self.compare_item() == 1:
                # Swap the item
                self.swap_item()
                # Turn his light on to indicate that a swap has occured
                self.set_light_on()
            
        # Once self.compare_item() is None, that means he is in front of a blank space
            #  - everything to the left of the blank space has already been sorted
        # Deposit what he is holding
        self.swap_item()

        # Reset the light to the off position
        self.set_light_off()

        # Move one spot over to the right
        self.move_right()

        # Re-run the process all over again
        self.sort()        


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)