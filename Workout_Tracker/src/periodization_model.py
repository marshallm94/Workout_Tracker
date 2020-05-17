class Macrocycle(object):

    def __init__(self):

        pass

# aka "Block"
class Mesocycle(object):

    def __init__(self, duration):

        # the "units" of duration should be understood as "microcycles"
        # AKA "splits"). I.e. if duration = 4, the user will go through their
        # microcycle/split 4 complete times
        self.duration = duration
        self.periodization_model = PeriodizationModel()


class PeriodizationModel(object):

    def __init__(self, duration):

        # target_reps and target_sets should be the same length
        # TODO: should target_rpe be optional? - no

        self.target_reps = [] 
        self.target_sets = [] 
        self.target_rpe = [] 
