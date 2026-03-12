import numpy as np

class NumpyAnalyzer:

    def __init__(self):
        self.array = None

    def create_array(self):
        print("\nArray Creation:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter number of elements: "))
            elements = list(map(int, input("Enter elements separated by space: ").split()))
            self.array = np.array(elements)

        elif choice == 2:
            r = int(input("Enter number of rows: "))
            c = int(input("Enter number of columns: "))
            elements = list(map(int, input(f"Enter {r*c} elements separated by space: ").split()))
            self.array = np.array(elements).reshape(r, c)

        elif choice == 3:
            x = int(input("Enter dimension 1: "))
            y = int(input("Enter dimension 2: "))
            z = int(input("Enter dimension 3: "))
            elements = list(map(int, input(f"Enter {x*y*z} elements: ").split()))
            self.array = np.array(elements).reshape(x, y, z)

        print("Array created successfully:")
        print(self.array)

        self.index_slice()

    def index_slice(self):
        while True:
            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                r = int(input("Enter row index: "))
                c = int(input("Enter column index: "))
                print("Value:", self.array[r][c])

            elif choice == 2:
                row_range = input("Enter row range (start:end): ")
                col_range = input("Enter column range (start:end): ")

                rs, re = map(int, row_range.split(":"))
                cs, ce = map(int, col_range.split(":"))

                print("Sliced Array:")
                print(self.array[rs:re, cs:ce])

            elif choice == 3:
                break

    def math_operations(self):
        if self.array is None:
            print("Create array first.")
            return

        print("\nMathematical Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("Enter your choice: "))

        size = self.array.size
        elements = list(map(int, input(f"Enter {size} elements for second array: ").split()))
        second = np.array(elements).reshape(self.array.shape)

        print("Original Array:")
        print(self.array)
        print("Second Array:")
        print(second)

        if choice == 1:
            result = self.array + second
        elif choice == 2:
            result = self.array - second
        elif choice == 3:
            result = self.array * second
        elif choice == 4:
            result = self.array / second

        print("Result:")
        print(result)

    def combine_split(self):
        if self.array is None:
            print("Create array first.")
            return

        print("\nCombine or Split Arrays:")
        print("1. Combine Arrays")
        print("2. Split Array")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            size = self.array.size
            elements = list(map(int, input(f"Enter {size} elements: ").split()))
            second = np.array(elements).reshape(self.array.shape)

            combined = np.vstack((self.array, second))

            print("Combined Array:")
            print(combined)

        elif choice == 2:
            parts = int(input("Enter number of parts to split: "))
            split_arrays = np.array_split(self.array, parts)

            print("Split Arrays:")
            for arr in split_arrays:
                print(arr)

    def search_sort_filter(self):
        if self.array is None:
            print("Create array first.")
            return

        print("\nSearch, Sort, Filter:")
        print("1. Search value")
        print("2. Sort array")
        print("3. Filter values")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter value to search: "))
            result = np.where(self.array == value)
            print("Found at indices:", result)

        elif choice == 2:
            print("Sorted Array:")
            print(np.sort(self.array))

        elif choice == 3:
            val = int(input("Show values greater than: "))
            print(self.array[self.array > val])

    def statistics(self):
        if self.array is None:
            print("Create array first.")
            return

        print("\nAggregates and Statistics:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Sum:", np.sum(self.array))
        elif choice == 2:
            print("Mean:", np.mean(self.array))
        elif choice == 3:
            print("Median:", np.median(self.array))
        elif choice == 4:
            print("Standard Deviation:", np.std(self.array))
        elif choice == 5:
            print("Variance:", np.var(self.array))


def main():
    analyzer = NumpyAnalyzer()

    while True:
        print("\nWelcome to the NumPy Analyzer")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            analyzer.create_array()
        elif choice == 2:
            analyzer.math_operations()
        elif choice == 3:
            analyzer.combine_split()
        elif choice == 4:
            analyzer.search_sort_filter()
        elif choice == 5:
            analyzer.statistics()
        elif choice == 6:
            print("Thank you for using the NumPy Analyzer! Goodbye!")
            break


if __name__ == "__main__":
    main()
