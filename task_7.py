import random
from collections import defaultdict
import matplotlib.pyplot as plt

nums = 1_000_000
counts = defaultdict(int)

# Симуляція кидків кубиків
for _ in range(nums):
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    counts[dice_one + dice_two] += 1

# Обрахунок імовірностей
probabilities = {sum_: count / nums for sum_, count in counts.items()}

# Сортування результатів за ключами (сумами)
sorted_probabilities = dict(sorted(probabilities.items()))

print("Dice Sum | Probability")
print("---------|-------------")
for dice_sum, prob in sorted_probabilities.items():
    print(f"   {dice_sum}    | {prob:.2%}")

# Побудова графіка
plt.bar(sorted_probabilities.keys(), sorted_probabilities.values())
plt.xlabel('Sum of Dice')
plt.ylabel('Probability')
plt.title('Probability Distribution of Dice Sum')
plt.show()