# completed
class Logger(object):
    '''Logging information'''
    def __init__(self, file_name):
        # passing file name in
        self.file_name = file_name



    def write_metadata(self, pop_size, virus_name, initial_infected, initial_vaccinated):
        '''Stores all logs'''
        write_meta = f'''
        Population: {pop_size} 
        Virus name: {virus_name} 
        Initially Infected: {initial_infected} 
        Initially Vaccinated: {initial_vaccinated}
        -------------------------------'''

        with open(self.file_name, 'w', encoding='utf-8') as file:
            file.write(write_meta)
        print(write_meta)



    def log_step(self, step_counter, new_deaths, new_vaccination, total_deaths, total_vaccinations):
        '''Logs each step'''
        log_step = f'''
        Step Counter: {step_counter} 
        New Deaths: {new_deaths} 
        New Vaccinations: {new_vaccination} 
        Total Simulation Deaths: {total_deaths} 
        Total Simulation Vaccination: {total_vaccinations}
        -------------------------------'''

        with open(self.file_name, 'a', encoding='utf-8') as file:
            file.write(log_step)
        print(log_step)



    def log_interactions(self, step_counter, interaction_counter, new_infection, newly_infected):
        '''Loggs interactions, new infections, newly infected'''

        log_interaction = f'''
        Step Counter: {step_counter} 
        Interaction Counter: {interaction_counter} 
        New Infection: {new_infection} 
        Newly Infected during round: {newly_infected}
        -------------------------------'''

        with open(self.file_name, 'a', encoding='utf-8') as file:
            file.write(log_interaction)
        print(log_interaction)



    def log_infection_survival(self, pop_size, initial_infected, initial_vaccinated, total_deaths, total_vaccinations):
        '''Log new deaths/survivals'''

        infected_survival = f'''
        Population Size: {pop_size} 
        Initially Infected: {initial_infected} 
        Initially Vaccinated: {initial_vaccinated} 
        Total Deaths: {total_deaths} 
        Total Vaccinations: {total_vaccinations}
        --------------------------------'''

        with open(self.file_name, 'a', encoding='utf-8') as file:
            file.write(infected_survival)
        print(infected_survival)





# test:
if __name__ == "__main__":
    # Create a Logger instance with a specific file name
    logger = Logger("simulation_log.txt")

    # Test write_metadata
    logger.write_metadata(1000, "Influenza", 50, 10)

    # Test log_interactions
    logger.log_interactions(1, 50, 90, 100)

    # Test log_infection_survival
    logger.log_infection_survival(1, 40, 50, 100, 90)


    # Check the content of the log file
    with open("simulation_log.txt", 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
