class BuildingWithFloor:
    def __init__(self):
        self.buildingInfo = {}
        self.floorPlans = []

    def loadUp(self,buildingIn, floorPlansIn):
        self.buildingInfo = buildingIn
        self.floorPlans = floorPlansIn
        return self
