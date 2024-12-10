"""
Advent of Code 2024 - Day 1

This script solves the "Historian Hysteria" challenge for Day 1 of Advent
of Code 2024.

The input data is provided in a tab-separated values (TSV) format,
and the script reads this data, processes it according to the challenges
requirements, and outputs the results.

For more details, see the README.md file in the same directory as this script.
"""
import heapq


def read_and_split_data(file_path):
    """
    Read data from a file and split each line into two separate lists.
    """
    left_values = []
    right_values = []

    with open(file_path, "r") as file:
        for line in file:
            left_value, right_value = map(int, line.split())
            left_values.append(left_value)
            right_values.append(right_value)

    return left_values, right_values


def total_distance_between_lists(list1, list2):
    """
    Calculate the total distance between two lists of integers where the
    distance is calculated from the smallest value in one list to the smallest
    value in the other list.
    """
    total_distance = 0

    # Convert lists to heaps
    heapq.heapify(list1)
    heapq.heapify(list2)

    while list1 and list2:
        list1_min = heapq.heappop(list1)
        list2_min = heapq.heappop(list2)

        total_distance += abs(list1_min - list2_min)

    return total_distance


def remove_all_occurrences_in_place(input_list, value_to_remove):
    """
    Remove all occurrences of a specific value from a list in-place.
    """
    while value_to_remove in input_list:
        input_list.remove(value_to_remove)


def similarity_score(list1, list2):
    """
    Calculate the similarity score between two lists of integers. By adding
    up each number in the left list after multiplying it by the number
    of times that number appears in the right list.
    """
    similarity_score = 0

    while list1:
        list1_current = list1.pop()

        if list1_current in list2:
            similarity_score += list1_current * list2.count(list1_current)
            remove_all_occurrences_in_place(list2, list1_current)

    return similarity_score


if __name__ == "__main__":
    # Read the input data
    left_values, right_values = read_and_split_data("day_1/input.txt")

    # Process the data
    print(f"Left values: {left_values}")
    print(f"Right values: {right_values}")

    # total_distance = total_distance_between_lists(left_values, right_values)
    # print(f"Total distance between lists: {total_distance}")

    similarity = similarity_score(left_values, right_values)
    print(f"Similarity score: {similarity}")
