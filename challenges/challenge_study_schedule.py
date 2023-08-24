def study_schedule(permanence_period, target_time):
    if not target_time or type(target_time) != int:
        return None
    count_frequency = 0
    for entry, exit in permanence_period:
        if type(entry) != int or type(exit) != int:
            return None
        if entry <= target_time <= exit:
            count_frequency += 1

    return count_frequency
