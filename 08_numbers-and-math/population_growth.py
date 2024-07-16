# Write the necessary code to display the total population count for the next 3 years (without a leap year).

# Here are the specifications:

# In the country we want to investigate:

# The current population is 380,123,456
# One person is born every 6 seconds
# One person dies every 12 seconds
# One person immigrates every 40 seconds


current_population = 380_123_456
birth_rate_in_seconds = 6
death_rate_in_seconds = 12
immigration_rate_in_seconds = 40

seconds_in_three_years = 3 * 365 * 24 * 60 * 60

total_birthed_in_three_years = seconds_in_three_years / birth_rate_in_seconds
total_deaths_in_three_years = seconds_in_three_years / death_rate_in_seconds
total_immigrated_in_three_years = seconds_in_three_years / immigration_rate_in_seconds

population_increase_in_three_years = total_birthed_in_three_years - total_deaths_in_three_years + total_immigrated_in_three_years

total_population_after_three_years = current_population + int(population_increase_in_three_years)

print('Total population after 3 years = ' + str(total_population_after_three_years))
