# completed
class Virus(object):
    '''Represents the virus that will be used to infect people in the simulation'''
    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate



# Test this class
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming
    # it has the attributes you defined
    virus = Virus("COVID-19", 0.0328, 0.6)
    try:
        assert virus.name == "COVID-19"
        assert virus.repro_rate == 0.0328
        assert virus.mortality_rate == 0.6
        print("completed")
    except AssertionError:
        print("test failed")
