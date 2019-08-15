import keyboard

FILENAME = "/home/pi/rfid/test_output"


def log(item):
    with open(FILENAME, 'a') as f:
        f.write(item)


def get_permissions(rfid):
    return {"Permission1": True}


def read_id():
    events = keyboard.record(until="\n")
    rfid = "".join(k.name for k in events if k.name != "enter")
    log(rfid)
    if get_permissions(rfid)['Permission1']:
        log("{}: accessed {}\n".format(rfid, 'Permission1'))


def main():
    while True:
        read_id()


if __name__ == "__main__":
    main()
