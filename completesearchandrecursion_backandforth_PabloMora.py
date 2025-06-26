possible_results = set()

def simulate(day, a_tank, b_tank, a_buckets, b_buckets):
    if day == 4:
        possible_results.add(a_tank)
        return

    if day % 2 == 0:
        for i in range(len(a_buckets)):
            bucket = a_buckets[i]
            new_a = a_buckets[:i] + a_buckets[i+1:]
            new_b = b_buckets + [bucket]
            simulate(day + 1, a_tank - bucket, b_tank + bucket, new_a, new_b)
    else:
        for i in range(len(b_buckets)):
            bucket = b_buckets[i]
            new_b = b_buckets[:i] + b_buckets[i+1:]
            new_a = a_buckets + [bucket]
            simulate(day + 1, a_tank + bucket, b_tank - bucket, new_a, new_b)

a_buckets = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
b_buckets = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

simulate(0, 1000, 1000, a_buckets, b_buckets)

print(len(possible_results))

