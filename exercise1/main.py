
from kidnaping import kidnaping, generateEntries

if __name__ == "__main__":

    target, schedule, ammount, cops = generateEntries(182)
    print("The target is " + target)

    kidnapingAttend = kidnaping(target)

    kidnapingAttend.analyzeTarget(schedule)

    kidnapingAttend.kidnap()

    if kidnapingAttend.result == "Failure":
        print("Kidnaping failure")
        exit()

    print("Kidnaping success")

    kidnapingAttend.askPayment(ammount)
    print("${} requested for target".format(ammount))

    print(kidnapingAttend.returnTarget(cops))
