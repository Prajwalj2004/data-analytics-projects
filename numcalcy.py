import numpy as np

print("\n========= NUMPY MATHEMATICAL CALCULATOR =========")
ele = list(map(int, input("Enter elements: ").split()))
arr = np.array(ele)
while True:
    print("\n========= CHOOSE THE OPTIONS BELOW FOR CALCULATIONS =========")
    print("1. Basic Arithmetic Operations")
    print("2. Statistical Operations")
    print("3. Array Manipulation")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\n--- BASIC ARITHMETIC OPERATIONS ---")
        arr2 =list(map(int, input("Enter another arr elements: ").split()))    
    
        print("Addition:", arr + arr2)
        print("Subtraction:", arr - arr2)
        print("Multiplication:", arr * arr2)
        print("Division:", arr / arr2)
        print("Power:", arr ** 2)

    elif choice == 2:
        print("\n--- STATISTICAL OPERATIONS ---")

        print("Mean:", np.mean(arr))
        print("Median:", np.median(arr))
        print("Standard Deviation:", np.std(arr))
        print("Variance:", np.var(arr))
        print("Minimum:", np.min(arr))
        print("Maximum:", np.max(arr))
        print("Sum:", np.sum(arr))
        print("Product:", np.prod(arr))
        print("Shape:", arr.shape)
        print("Size:", arr.size)
        print("Data Type:", arr.dtype)

    elif choice == 3:
        print("\n--- ARRAY MANIPULATION ---")

        print("Original Array (1D):", arr)
        print("Sorted Array:", np.sort(arr))
        print("Reverse Sorted:", np.sort(arr)[::-1])

        print("Unique Values:", np.unique(arr))
        print("First Element:", arr[0])
        print("Last Element:", arr[-1])

        mean_val = np.mean(arr)
        print("Values Greater Than Mean:", arr[arr > mean_val])

        size = arr.size

        for i in range(2, size + 1):
            if size % i == 0:
                print("\n2D Reshape:")
                print(arr.reshape(i, size // i))
                break

        reshaped = False
        for i in range(2, size + 1):
            for j in range(2, size + 1):
                if size % (i * j) == 0:
                    k = size // (i * j)
                    print("\n3D Reshape:")
                    print(arr.reshape(i, j, k))
                    reshaped = True
                    break
            if reshaped:
                break

        if not reshaped:
            print("\n3D Reshape not possible")

    elif choice == 4:
        print("\nExiting Calculator... Thank you!")
        break

    elif choice not in range(1,5):
        print("\nInvalid Choice Choose from 1 to 4 Options.")
    
    else:
        print('Choose Any 1 Operation')
