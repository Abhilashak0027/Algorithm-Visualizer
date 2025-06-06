from algorithms.bubble_sort import bubble_sort
from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from algorithms.linear_search import linear_search
from algorithms.binary_search import binary_search

def main():
    print("🔢 Algorithm Visualizer")
    print("======================")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Linear Search")
    print("7. Binary Search")

    choice = int(input("Enter your choice (1–7): "))
    arr = list(map(int, input("Enter array elements (space-separated): ").split()))

    steps = []

    if choice == 1:
        bubble_sort(arr, steps)
    elif choice == 2:
        selection_sort(arr, steps)
    elif choice == 3:
        insertion_sort(arr, steps)
    elif choice == 4:
        merge_sort(arr, steps)
    elif choice == 5:
        quick_sort(arr, 0, len(arr) - 1, steps)
    elif choice == 6:
        target = int(input("Enter element to search: "))
        index = linear_search(arr, target)
        print("Found at index:" if index != -1 else "Not found", index)
        return
    elif choice == 7:
        arr.sort()
        target = int(input("Enter element to search: "))
        index = binary_search(arr, target)
        print("Found at index:" if index != -1 else "Not found", index)
        return
    else:
        print("Invalid choice")
        return

    print("Sorted Array:", arr)
    print("\n🪄 Steps:")
    for i, step in enumerate(steps):
        print(f"Step {i+1}: {step}")

if __name__ == "__main__":
    main()
