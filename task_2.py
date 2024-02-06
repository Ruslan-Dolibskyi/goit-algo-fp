import turtle
import math


def draw_branch(t, length, angle, depth):
    """
    Рекурсивно малює гілки дерева Піфагора.
    :param t: екземпляр Turtle
    :param length: довжина гілки
    :param angle: кут повороту
    :param depth: глибина рекурсії
    """
    if depth == 0:
        return

    t.forward(length)
    t.left(angle)
    draw_branch(t, length * math.sqrt(2)/2, angle, depth-1)
    t.right(angle * 2)
    draw_branch(t, length * math.sqrt(2)/2, angle, depth-1)
    t.left(angle)
    t.backward(length)


def main():
    # Налаштування вікна
    screen = turtle.Screen()
    screen.title("Оголене Дерево Піфагора")

    # Налаштування Turtle
    t = turtle.Turtle()
    t.speed(0)  # найшвидша швидкість
    t.left(90)  # спрямувати Turtle вгору

    # Отримати рівень рекурсії від користувача
    depth = int(input("Введіть рівень рекурсії: "))

    # Початкова довжина гілки
    initial_length = 80

    # Починаємо малювати оголене дерево Піфагора
    draw_branch(t, initial_length, 45, depth)

    # Закінчуємо малювання
    screen.mainloop()


if __name__ == "__main__":
    main()