def process_age(age):
    if not isinstance(age, int) or isinstance(age, bool):
        return None
    return age + 1


def process_name(name):
    if not isinstance(name, str):
        return ""
    return name.strip().title()


def process_scores(scores):
    if not isinstance(scores, list) or len(scores) == 0:
        return 0.0

    if not all(isinstance(x, int) and not isinstance(x, bool) for x in scores):
        return 0.0

    return sum(scores) / len(scores)


if __name__ == "__main__":
    print("Age:", process_age(20))
    print("Name:", process_name(" suhas "))
    print("Average:", process_scores([80, 90, 100]))