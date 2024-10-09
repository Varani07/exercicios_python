class Emotion():
    def __init__(self, positivity, negativity):
        self._positivity = positivity
        self._negativity = negativity
    def __bool__(self):
        return self._positivity > self._negativity
    
my_emotional_state = Emotion(positivity=50, negativity=75)

if my_emotional_state:
    print("This will not print!")

my_emotional_state._positivity = 100

if my_emotional_state:
    print("This will print!")