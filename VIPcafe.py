from collections import deque


def when_friend_served(n, priorities, K):
    # Create a queue with (priority, index) pairs
    queue = deque([(priorities[i], i) for i in range(n)])

    # Variable to count how many orders have been served
    served_count = 0

    while queue:
        # Find the maximum priority in the current queue
        max_priority = max(queue, key=lambda x: x[0])[0]

        # Pop the front order from the queue
        priority, index = queue.popleft()

        # If this order has the highest priority, serve it
        if priority == max_priority:
            served_count += 1  # Increment the count of served orders

            # If the served order is Raj's friend's order, return the count
            if index == K:
                return served_count
        else:
            # Reinsert the order at the end of the queue
            queue.append((priority, index))

            # Increment the priority of all orders before the served order
            for i in range(len(queue)):
                queue[i] = (queue[i][0] + 1, queue[i][1])


# Input
n = int(input())  # Total number of orders
priorities = list(map(int, input().split()))  # Priorities of the orders
K = int(input())  # The position of Raj's friend's order


print(when_friend_served(n, priorities, K))
