import random, sys

random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, initial_vaccinated, initial_infected=1):
        self.logger = Logger("simulation_log.txt")
        self.virus = virus
        self.pop_size = pop_size
        self.initial_vaccinated = initial_vaccinated
        self.initial_infected = initial_infected
        self.population = self._create_population()
        self.step_counter = 0
        self.interaction_counter = 0
        self.newly_infected = set()
        self.new_deaths = 0
        self.new_vaccinations = 0
        self.total_deaths = []
        self.total_vaccinations = [initial_vaccinated + initial_infected]



    def _create_population(self):
        '''creating population, some vaccinated and some infected'''
        population = []
        for i in range(0, self.pop_size):
            person = Person(i, False)
            population.append(person)
        
        newly_infected = 0
        while newly_infected < self.initial_infected:
            random_person = random.choice(population)
            if not random_person.infection:
                random_person.infection = self.virus
                random_person.is_vaccinated = True
                newly_infected += 1

        newly_vaccinated = 0
        while newly_vaccinated < self.initial_vaccinated:
            random_person = random.choice(population)
            if not random_person.is_vaccinated:
                random_person.is_vaccinated = True
                newly_vaccinated += 1

        return population



    def _simulation_should_continue(self):
        '''Checks if simulation should continue or is complete'''
        if sum(self.total_deaths) + sum(self.total_vaccinations) == self.pop_size:
            return False
        else:
            return True



    def run(self):
        '''Starts Simulation'''

        should_continue = True

        self.logger.write_metadata(self.pop_size, self.virus.name, self.initial_infected, self.initial_vaccinated)

        while should_continue:
            self.step_counter += 1
            self.time_step()
            should_continue = self._simulation_should_continue()

        self.logger.log_infection_survival(self.pop_size, self.initial_infected, self.initial_vaccinated, sum(self.total_deaths), sum(self.total_vaccinations))



    def time_step(self):
        '''Logs time step'''
        number_interations = 100
        living_people = [person for person in self.population if person.is_alive]
        living_infected = [person for person in living_people if person.infection]

        for person in living_infected:
            completed_interaction = 0
            while completed_interaction < number_interations:
                random_person = random.choice(living_people)
                self.interaction_counter += 1
                self.interaction(random_person)
                completed_interaction += 1
        self._infect_newly_infected()

        self.logger.log_step(self.step_counter, self.new_deaths, self.new_vaccinations, sum(self.total_deaths), sum(self.total_vaccinations))

        self.new_deaths = 0
        self.new_vaccinations = 0



    def interaction(self, random_person):
        '''Checks for interactions
        if interacts with infected person, uninfected person becomes infected'''
        new_infection = False
        if not random_person.infection and not random_person.is_vaccinated:
            random_number = random.uniform(0.0, 1.0)
            if random_number < self.virus.repro_rate:
                self.newly_infected.add(random_person)
                new_infection = True



    def _infect_newly_infected(self):
        '''Checks if person survived if survived they are vaccinated else they die'''
        living_people = [person for person in self.population if person.is_alive]
        for person in living_people:
            if person in self.newly_infected:
                person.infection = self.virus
                if person.did_survive_infection():
                    self.new_vaccinations +=1
                else:
                    self.new_deaths += 1

        self.total_vaccinations.append(self.new_vaccinations)
        self.total_deaths.append(self.new_deaths)

        self.newly_infected = set()



if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    initial_vaccinated = int(pop_size * 0.01)
    initial_infected = 10

    # Make a new instance of the Simulation
    sim = Simulation(virus, pop_size, initial_vaccinated, initial_infected)

    sim.run()
