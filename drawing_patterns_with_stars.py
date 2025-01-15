# 🖼️ Python Pattern Drawing Project

# Step 1: Display a menu to the user
print("🌟 Welcome to the Python Pattern Drawing Program!")
print("Choose a pattern type:")
print("1. Right-angled Triangle")
print("2. Square with Hollow Center")
print("3. Diamond")
print("4. Left-angled Triangle")
print("5. Hollow Square")
print("6. Pyramid")
print("7. Reverse Pyramid")
print("8. Rectangle with Hollow Center")

# Step 2: Get the user's choice
choice = int(input("Enter the number corresponding to your choice: "))


# Additional step, if user's choice is invalid and not part of the pre-set choices
# TODO: make it work more than once
if choice > 8 or choice < 1:
    print("❌ Invalid choice! Please restart the program, or exit.")
    print('1. Restart the Program')
    print('2. Exit')

    sub_choice = int(input('Enter the number of your choice:'))

    if sub_choice == 1:
        print("🌟 Welcome to the Python Pattern Drawing Program!")
        print("Choose a pattern type:")
        print("1. Right-angled Triangle")
        print("2. Square with Hollow Center")
        print("3. Diamond")
        print("4. Left-angled Triangle")
        print("5. Hollow Square")
        print("6. Pyramid")
        print("7. Reverse Pyramid")
        print("8. Rectangle with Hollow Center")

        # Step 2: Get the user's choice
        choice = int(input("Enter the number corresponding to your choice: "))
    else:
        print('Program exited')

# Step 3: Get dimensions based on choice
if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
    rows = int(input("Enter the number of rows: "))
elif choice in [2, 5, 8]:  # Patterns that need size
    size = int(input("Enter the size of the square/rectangle: "))

# Step 4: Generate the selected pattern
if choice == 1:  # Right-angled Triangle
    # TODO: Loop through rows and print increasing stars: CHECK!
    for i in range(1, rows + 1):
        print('*' * i)

elif choice == 2:  # Square with Hollow Center
    # TODO: Create a square with a hollow center: CHECK!
    for i in range(size):

        for k in range(size):

            if i == 0 or i == size - 1 or k == 0 or k == size - 1:
                print('*', end='')

            else:
                print(' ', end='')
        print(' ')

elif choice == 3:  # Diamond
    # TODO: Create a diamond shape using loops: CHECK!
    n = rows

    for i in range(1, n):

        for j in range(n - i):
            print('', end=' ')

        for j in range(1, i):
            print('*', end='')

        for i in range(i, 0, -1):
            print('*', end='')

        print()

    for k in range(n, 0, -1):

        for j in range(n - k):
            print('', end=' ')

        for j in range(1, k):
            print('*', end='')

        for i in range(0, k):
            print('*', end='')

        print()

elif choice == 4:  # Left-angled Triangle
    # TODO: Print decreasing stars for each row: CHECK!
    for i in range(rows, 0, -1):
        print('*' * i)

elif choice == 5:  # Hollow Square
    # TODO: Similar to choice 2 but ensure perfect square logic: CHECK!
    for i in range(size):

        for k in range(size):

            if i == 0 or i == size - 1 or k == 0 or k == size - 1:
                print('*', end=' ')

            else:
                print(' ', end=' ')
        print('')

elif choice == 6:  # Pyramid
    # TODO: Center-align stars to form a pyramid: CHECK!

    for i in range(1, rows):

        for j in range(rows - i):
            print('', end=' ')

        for j in range(1, i):
            print('*', end='')

        for i in range(i, 0, -1):
            print('*', end='')

        print()

elif choice == 7:  # Reverse Pyramid
    # TODO: Create an upside-down pyramid: CHECK!

    for i in range(rows, 0, - 1):

        for j in range(rows - i):
            print('', end=' ')

        for j in range(1, i):
            print('*', end='')

        for i in range(0, i):
            print('*', end='')

        print()

elif choice == 8:  # Rectangle with Hollow Center
    # TODO: Handle separate width and height inputs for rectangle: CHECK!
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))

    w = width
    h = height

    for i in range(h):

        for j in range(w):

            if i == 0 or i == h - 1 or j == 0 or j == w - 1:

                print('*', end='')

            else:
                print('', end=' ')

        print()



# Step 5: Optional - Allow the user to restart or exit
