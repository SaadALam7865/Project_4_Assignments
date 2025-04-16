# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.
# Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:
# the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)
# the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)
# the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)
# Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.
# Here's a sample run of the program (user input is in blue):
# How old are you? 20 You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.

# The program should be able to handle invalid input (e.g. negative numbers, non-numeric input) gracefully. If the user enters an invalid age, the program should print an error message and ask for the age again.

def get_age():
    while True:
        try:
            age = int(input('How old are you? '))
            if age < 0:
                print('Age cannot be negative. Please enter a valid age.')
                continue
            return age
        except ValueError:
            print('Invalid input. Please enter a numeric value for age.')
        except KeyboardInterrupt:
            print('\nProgram terminated.')
            exit(0)


def check_voting_eligibility(age):
    voting_ages = {
        'Peturksbouipo': 16,
        'Stanlau': 25,
        'Mayengua': 48
    }

    eligible_countries = []
    ineligible_countries = []

    for country, voting_age in voting_ages.items():
        if age >= voting_age:
            eligible_countries.append(country)
            print(f'You can vote in {country} where the voting age is {voting_age}.')
        else:
            ineligible_countries.append(country)
            print(f'You cannot vote in {country} where the voting age is {voting_age}.')

    return eligible_countries, ineligible_countries


# Run the program
age = get_age()
eligible_countries, ineligible_countries = check_voting_eligibility(age)

# Summary Output
print(f'\nSummary:')
print(f'✅ You can vote in: {", ".join(eligible_countries) if eligible_countries else "None"}')
print(f'❌ You cannot vote in: {", ".join(ineligible_countries) if ineligible_countries else "None"}')

         