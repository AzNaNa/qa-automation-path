def count_levels(logs):
    counts = {}
    for line in logs:
        parts = line.split()
        if len(parts) >= 3:
            level = parts[2].upper()
            counts[level] = counts.get(level, 0) + 1
    return counts

logs = [
    "2026-10-12 14:03:55 ERROR Connection timeout",
    "2026-10-12 14:04:01 INFO User logged in",
    "2026-10-12 14:04:12 ERROR Disk full",
    "2026-10-12 14:05:30 WARNING Slow response",
    "2026-10-12 14:06:44 INFO User logged out",
]

if __name__ == "__main__":
    print(count_levels(logs))
