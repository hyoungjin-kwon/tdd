import time


def going_to_work(person, bus):
    if not time.localtime() < time.localtime("07:00"):
        return

    get_up_and_wash(person)
    get_ready_to_go_out(person)
    take_the_bus_and_go_to_the_company(bus, person)


def get_up_and_wash(person):
    person.wake_up_from_the_bed()
    person.go_to_bathroom()
    person.turn_on_the_water()
    person.wash_face()
    if not person.already_shower_yesterday():
        person.take_a_shower()


def get_ready_to_go_out(person):
    if person.gender == "woman":
        person.pull_on("클로니더블자켓")
        if person.like("화장"):
            person.make_up()
    elif person.gender == "man":
        person.pull_on("맨투맨")
        person.shave()

        
def take_the_bus_and_go_to_the_company(bus, person):
    person.walk_to(person.near_bus_stop)
    while bus.location is person.near_bus_stop:
        person.wait()
    person.ride(bus)
    if not person.type == "DISABLED" and not person.type == "NATIONAL_MERIT":
        person.pay_fee(bus)
    while bus.location is person.company_near_bus_stop:
        person.wait()
    person.walk_to(person.company)





