ADULT_AGE = 19


def get_adults(people):
    adults = []
    for person in people:
        if person.age > ADULT_AGE:
            adults.append(person)
    return adults
