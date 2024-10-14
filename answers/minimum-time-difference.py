def findMinDifference(self, timePoints: List[str]) -> int:
    timePoints = sorted([int(time[:2]) * 60 + int(time[3:]) for time in timePoints])
    timePoints.append(timePoints[0] + 1440)
    return min(timePoints[i + 1] - timePoints[i] for i in range(len(timePoints) - 1)
               for i in range(len(timePoints) - 1))