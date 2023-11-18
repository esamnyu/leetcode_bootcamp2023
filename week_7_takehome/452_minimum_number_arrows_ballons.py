class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort the balloons based on their ending x-coordinate
        points.sort(key=lambda x: x[1])

        # Initialize the count of arrows and the position of the first arrow
        arrows = 1
        arrow_pos = points[0][1]

        # Iterate through the sorted balloons
        for x_start, x_end in points:
            # Check if the current balloon overlaps with the arrow
            if x_start > arrow_pos:
                # If it does not overlap, shoot a new arrow and update its position
                arrows += 1
                arrow_pos = x_end

        return arrows
