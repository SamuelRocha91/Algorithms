def is_anagram(first_string, second_string):
    lower_first = first_string.lower()
    lower_second = second_string.lower()
    if len(first_string) == 1:
        return (lower_first, lower_second, lower_second == lower_first)

    first_list = list(lower_first)
    second_list = list(lower_second)
    ordered_list_first = merge_sort(first_list)
    ordered_list_second = merge_sort(second_list)

    if second_string == "" and first_string != "":
        return ("".join(ordered_list_first), second_string, False)
    elif first_string == "" and second_string != "":
        return (first_string, "".join(ordered_list_second), False)
    elif second_string == "" and first_string == "":
        return (first_string, second_string, False)

    isTrue = ordered_list_first == ordered_list_second

    return ("".join(ordered_list_first), "".join(ordered_list_second), isTrue)


def merge_sort(list_of_letters, start=0, end=None):
    if end is None:
        end = len(list_of_letters)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(list_of_letters, start, mid)
        merge_sort(list_of_letters, mid, end)
        return merge(list_of_letters, start, mid, end)


def merge(list_of_letters, start, mid, end):
    left = list_of_letters[start:mid]
    right = list_of_letters[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            list_of_letters[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            list_of_letters[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            list_of_letters[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            list_of_letters[general_index] = right[right_index]
            right_index = right_index + 1

    return list_of_letters

# FUNÇÃO IMPLEMENTADA DE MODO LITERAL CONFORME CONSTA NO COURSE DA TRYBE
#  E NO CANAL PROGRAMAÇÃO DINÂMICA DO YOUTUBE
# APENAS SE ALTERANDO A NOMENCLATURA PARA ADAPTAÇÃO AO CONTEXTO
