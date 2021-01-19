
import random

class plan:

    def __init__(self, kpi):
        self._kpi = kpi
        self._old = float("Inf")
        self.risk = float("Inf")
        self.security = float("Inf")
        self.score = float("Inf")
        self.schedule = {
            "day" : "",
            "hour" : -1
        }

    def _getScore(self, schedule_kpi):
        return (schedule_kpi["risk"] + schedule_kpi["security"]) / 2

    def update(self, schedule_kpi, schedule):
        if self._kpi == "score":
            new = self._getScore(schedule_kpi)
        else:
            new =  schedule_kpi[self._kpi]

        if new < self._old:
            self.score = self._getScore(schedule_kpi)
            self.risk = schedule_kpi["risk"]
            self.security = schedule_kpi["security"]
            self.schedule["day"] = schedule[0]
            self.schedule["hour"] = schedule[1]
            self._old = new

    def _getTotalRisk(self, team):
        return self.risk

    def _getTotalSecurity(self, team):
        return self.security

    def execute(self, team):
        totalRisk = self._getTotalRisk(team)
        totalSecurity = self._getTotalSecurity(team)
        if totalSecurity > random.random():
            return "Failed"
        if totalRisk > random.random():
            return "Exposed"
        return "Success"

    def __repr__(self):
        return "The kidnaping will be the {} at {} hours with a risk of {} and security of {}".format(self.schedule["day"], self.schedule["hour"], self.risk, self.security)

class member:

    def __init__(self, data):
        self.name = data["name"]
        self.skills = {
            "driving": data["driving"],
            "strength": data["stregth"],
            "firearms": data["firearms"],
            "agility": data["agility"]
        }

class kidnaping:

    def __init__(self, targetName):
        # Arguments:
        #   + targetName: Text with the name of the person to kidnap.
        self.targetName = targetName

    def analyzeTarget(self, targetSchedule, prioritize = "score"):
        # Arguments:
        #   + targetschedule: Dictionarty with all days and hours and a KPI of
        #     risk of get sposed during the kidnaping and the target security
        #   + prioritize: Text with the factor to prioritize, may bi risk,
        #     security or score (a score between both KPIs).
        self.plan = plan(prioritize)
        for day in targetSchedule.keys():
            for hour in targetSchedule[day].keys():
                self.plan.update(targetSchedule[day][hour], [day, hour])
        print(self.plan)

    def getTeam(self, members):
        self.team = []
        for m in members:
            self.team.append(member(m))

    def kidnap(self):
        self.result = self.plan.execute(None)

    def askPayment(self, ammount):
        self.ammount = ammount

    def returnTarget(self, cops, riskTol = 0.5):
        newRisk = max(self.plan.risk * (2 if self.result == "Success" else 4) + (self.ammount / 100000000), 1)
        if newRisk >= riskTol or (cops and newRisk >= (riskTol/2)):
            return "target Killed"
        if newRisk < random.random():
            if cops and 0.5 < random.random():
                return "Failure"
            else:
                return "Success"
        return "Failure"

def generateEntries(seed = 1):
    random.seed(seed)
    target = "Nicolas Maduro"
    schedule = {}
    for day in ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]:
        schedule[day] = {}
        for hour in range(24):
            schedule[day][hour] = {
                "risk": random.random(),
                "security": random.random()
            }
    ammount = random.random() * 100000000
    cops = random.random() < 0.5

    return (target, schedule, ammount, cops)
