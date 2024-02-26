import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    # Налаштування екрану
    window = turtle.Screen()
    window.bgcolor("sky blue")

    # Створення та налаштування об'єкта turtle
    flake = turtle.Turtle()
    flake.speed(0)  # Найвища швидкість
    flake.color("white")

    # Визначення рівня рекурсії
    order = int(input("Будь ласка, введіть рівень рекурсії для сніжинки Коха: "))

    # Початкова позиція
    flake.penup()
    flake.goto(-150, 90)
    flake.pendown()

    # Малювання трьох сторін сніжинки
    for i in range(3):
        koch_snowflake(flake, order, 300)
        flake.right(120)

    # Завершення
    window.mainloop()

if __name__ == "__main__":
    main()