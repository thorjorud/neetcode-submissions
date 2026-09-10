class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = []

        for p, s in cars:
            eta = (target - p) / s
            fleets.append(eta)

            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()
        
        return len(fleets)