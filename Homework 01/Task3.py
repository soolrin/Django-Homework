# Есть два пользователя и множество их знакомых. Нужно найти тех,
# с кем знаком только один из них, но не оба.

user1 = {"Alice", "Bob", "Charlie"}
user2 = {"Bob", "Diana", "Eve"}

result_1 = user1 | user2                # Способ 1
result_2 = set()
result_2.update(user1, user2)           # Способ 2

print(result_1)
print(result_2)