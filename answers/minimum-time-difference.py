def findMinDifference(self, timePoints: List[str]) -> int:
    timePoints = sorted([int(time[:2]) * 60 + int(time[3:]) for time in timePoints])
        
