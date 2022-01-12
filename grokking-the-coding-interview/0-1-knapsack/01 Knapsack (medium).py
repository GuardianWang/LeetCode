"""
Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack which has a capacity ‘C’. 
The goal is to get the maximum profit out of the items in the knapsack. 
Each item can only be selected once, as we don’t have multiple quantities of any item.
Let’s take the example of Merry, who wants to carry some fruits in the knapsack to get maximum profit. 
    Here are the weights and profits of the fruits:
Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5
Let’s try to put various combinations of fruits in the knapsack, such that their total weight is not more than 5:
Apple + Orange (total weight 5) => 9 profit
Apple + Banana (total weight 3) => 7 profit
Orange + Banana (total weight 4) => 8 profit
Banana + Melon (total weight 5) => 10 profit
This shows that Banana + Melon is the best combination as it gives us the maximum profit and the total weight does not exceed the capacity.
"""
def solve_knapsack(profits, weights, capacity):
  ans = -1
  # only allow 1 item, 0-C capacity
  prev = [0] * (capacity + 1)
  cur = prev.copy()
  # allow one more item
  for p, w in zip(profits, weights):
    if w > capacity:
      continue
    for i in range(w, len(cur)):  # starting from index w, we can add this item
      # w/ or w/o this item
      cur[i] = max(prev[i], prev[i - w] + p)
    print(cur)
    ans = max(ans, cur[-1])  # cur is increasing
    prev = cur.copy()

  return ans 


def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()


"""
Time O(NC): don't need to sort by weight 
Space O(C)
"""

