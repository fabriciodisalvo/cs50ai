from degrees import *

def testing():

    # Load data from files into memory
    print("Loading data...")
    load_data("small")
    print("Data loaded.")
    print()
    print("Test 01: Valeria Golino and Cary Elwes")
    source, target = ("Valeria Golino", "Cary Elwes")
    source = person_id_for_name(source)
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(target)
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")

    print()
    print("Test 02: Valeria Golino and Emma Watson")
    source, target = ("Valeria Golino", "Emma Watson")
    source = person_id_for_name(source)
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(target)
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")

    print()
    print("Test 02: Tom Hanks and Kevin Bacon")
    source, target = ("Tom Hanks", "Kevin Bacon")
    source = person_id_for_name(source)
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(target)
    if target is None:
        sys.exit("Person not found.")
    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")
testing()
