def get_event_date(event):
    return event.date
# this will get the date of each event and we will
# use this as a parameter for the sort function next

def current_users(events):
    events.sort(key = get_event_date)
    # take the event date from the event date function and sorts by date
    machines = {}
    # create dictionary that stores names and users of a machine
    for event in events:
    # for each event in events
        if event.machine not in machines:
            machines[event.machine] = set()
        # if event is not in the machine, add empty set as value
        if event.type = "login":
            machines[event.machine].add(event.user)
        # check the event type, if it is login, add the user to the dictionary
        elif event.type = "logout":
            machines[event.machine].remove(event.user)
        # check the event type, if it is logout, remove the user from the dictionary
    return machines
# first sorts events by date, then for each event checks if the event is
# in the machine or not. if it is not in the machine, add an empty set.
# next check the event type. if it is a login, add the event user to the
# dictionary, if it is a logout, remove the event user from the dictionary

def generate_report(machines):
    for machine, users in machines.items():
    # sets variable machine to the keys in the dictionary machines and
    # sets variable users to the values in the dictionary machines.
        if len(users) > 0:
        # ensures that we don't print any machines where nobody is currently logged in
            user_list = ", ".join(users)
            # puts a comma between every element in the list of users
            print("{}: {}".format(machine, user_list))
            # prints the users under each machine
