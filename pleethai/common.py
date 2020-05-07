class Common:
    # Check value in list or not
    def contains(list, value, match_condition):
        if list is not None:
            for item in list:
                if match_condition(item, value):
                    return True
        return False
