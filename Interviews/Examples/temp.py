def merge_meeting(meetings):
    meetings.sort()
    size = len(meetings)
    result = [meetings[0]]
    for i in range(1, size):
        start = meetings[i][0]
        end = meetings[i][1]
        previous = result[-1]
        if start in range(previous[0], previous[1] + 1):
            new_start = min(previous[0], start)
            new_end = max(previous[1], end)
            result[-1] = (new_start, new_end)
        else:
            result.append(meetings[i])
    return result


x = merge_meeting([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
print(x)
