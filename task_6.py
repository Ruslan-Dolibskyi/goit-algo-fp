def greedy_algorithm(items, budget):
    # Спочатку розрахуємо співвідношення калорій до вартості для кожного продукту
    for item in items:
        items[item]["value"] = items[item]["calories"] / items[item]["cost"]

    # Відсортуємо продукти за співвідношенням в спадаючому порядку
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["value"], reverse=True)

    total_calories = 0
    selected_items = []

    # Вибираємо страви, дотримуючись обмеження бюджету
    for item, properties in sorted_items:
        if budget - properties["cost"] >= 0:
            budget -= properties["cost"]
            total_calories += properties["calories"]
            selected_items.append(item)

    return selected_items, total_calories


def dynamic_programming(items, budget):
    N = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(N + 1)]
    item_list = list(items.items())

    # Заповнюємо таблицю dp
    for i in range(1, N + 1):
        item, prop = item_list[i - 1]
        cost = prop["cost"]
        cal = prop["calories"]

        for j in range(1, budget + 1):
            if cost <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + cal)
            else:
                dp[i][j] = dp[i - 1][j]

    # Відновлюємо вибір страв
    selected_items = []
    rem_budget = budget

    for i in range(N, 0, -1):
        if dp[i][rem_budget] != dp[i - 1][rem_budget]:
            item, _ = item_list[i - 1]
            selected_items.append(item)
            rem_budget -= items[item]["cost"]

    total_calories = dp[N][budget]
    return selected_items, total_calories

# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

selected_items, total_calories = greedy_algorithm(items, budget)
print("Greedy algorithm:")
print("Budget:", budget)
print("Selected items:", selected_items)
print("Total calories:", total_calories)

selected_items, total_calories = dynamic_programming(items, budget)
print("Dynamic programming:")
print("Budget:", budget)
print("Selected items:", selected_items)
print("Total calories:", total_calories)