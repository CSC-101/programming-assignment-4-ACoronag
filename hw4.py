import sys
import build_data

full_data = build_data.get_data()



def percent(line,reduced):
    percent = 0
    code = line[1].split(".")
    if code[0] == "Education":
        if len(reduced) == 0:
            for county in full_data:
                try:
                    percent += county.education[code[1]]
                except KeyError:
                    print("Invalid Key!!")
                    return
        else:
            for county in reduced:
                try:
                    percent += county.education[code[1]]
                except KeyError:
                    print("Invalid Key!!")
                    return
    elif code[0] == "Ethnicities":
        if len(reduced) == 0:
            for county in full_data:
                try:
                    percent += county.ethnicities[code[1]]
                except KeyError:
                    print("Invalid Key!!")
                    return
        else:
            for county in reduced:
                try:
                    percent += county.ethnicities[code[1]]
                except KeyError:
                    print("Invalid Key!!")
                    return
    elif code[0] == "Income":
        if len(reduced) == 0:
            for county in full_data:
                try:
                    percent += county.income[code[1]]
                except KeyError:
                    print("Invalid Key!!")
                    return
        else:
            for county in reduced:
                try:
                    percent += county.income[code[1]]
                except KeyError:
                    print("Invalid Key!!")
                    return
    print(round(percent/len(full_data),2))

def population_total(reduced):
    population = 0
    if len(reduced) == 0:
        for county in full_data:
            population += county.population["2014 Population"]
    else:
        for county in reduced:
            population += county.population["2014 Population"]
    print(population)

def filter_state(line):
    filtered_counties = []
    for county in full_data:
            if county.state == line[1]:
                filtered_counties.append(county)
    print(len(filtered_counties))
    return filtered_counties

def filter_gt(line,reduced):
    filtered_counties = []
    code = line[1].split(".")
    if code[0] == "Education":
        if len(reduced) == 0:
            for county in full_data:
                try:
                    if county.education[code[1]] > float(line[2]):
                        filtered_counties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number!!".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key!!")
                    return
        else:
            for county in reduced:
                try:
                    if county.education[code[1]] > float(line[2]):
                        filtered_counties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number!!".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key!!")
                    return
    elif code[0] == "Income":
        if len(reduced) == 0:
            for county in full_data:
                try:
                    if county.income[code[1]] > float(line[2]):
                        filtered_counties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number!!".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key!!")
                    return
        else:
            for county in reduced:
                try:
                    if county.income[code[1]] > float(line[2]):
                        filtered_counties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number!!".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key!!")
                    return
    elif code[0] == "Ethnicities":
        if len(reduced) == 0:
            for county in full_data:
                try:
                    if county.ethnicities[code[1]] > float(line[2]):
                        filtered_counties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number!!".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key!!")
                    return
        else:
            for county in reduced:
                try:
                    if county.ethnicities[code[1]] > float(line[2]):
                        filtered_counties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number!!".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key!!")
                    return
    print("Filter: {} Greater than {}: {}".format(code[0],line[2],len(filtered_counties)))
    return filtered_counties

def filter_lt(line,reduced):
    filtered_counties = []
    code = line[1].split(".")
    if code[0] == "Education":
        if len(reduced) == 0:
            for county in full_data:
                try:
                    if county.education[code[1]] < float(line[2]):
                        filtered_counties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number!!".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key!!")
                    return
        else:
            for county in reduced:
                try:
                    if county.education[code[1]] < float(line[2]):
                        filtered_counties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number!!".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key!!")
                    return
    elif code[0] == "Income":
        if len(reduced) == 0:
            for county in full_data:
                try:
                    if county.income[code[1]] < float(line[2]):
                        filtered_counties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number!!".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key!!")
                    return
        else:
            for county in reduced:
                try:
                    if county.income[code[1]] < float(line[2]):
                        filtered_counties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number!!".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key!!")
                    return
    elif code[0] == "Ethnicities":
        if len(reduced) == 0:
            for county in full_data:
                try:
                    if county.ethnicities[code[1]] < float(line[2]):
                        filtered_counties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number!!".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key!!")
                    return
        else:
            for county in reduced:
                try:
                    if county.ethnicities[code[1]] < float(line[2]):
                        filtered_counties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number!!".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key!!")
                    return
    print("Filter: {} Less than {}: {}".format(code[0],line[2],len(filtered_counties)))
    return filtered_counties

def display(reduced):
    if len(reduced) == 0:
        for county in full_data:
            print("County: {}\nState: {}\nPopulation: {}\n".format(county.county,county.state,county.population["2014 Population"]))
    else:
        for county in reduced:
            print("County: {}\nState: {}\nPopulation: {}\n".format(county.county, county.state,county.population["2014 Population"]))

def population(line,reduced):
    population = 0
    code = line[1].split(".")
    if code[0] == "Ethnicities":
        if len(reduced) == 0:
            for county in full_data:
                population += round(county.ethnicities[code[1]] * county.population["2014 Population"])
        else:
            for county in reduced:
                population += round(county.ethnicities[code[1]] * county.population["2014 Population"])
    elif code[0] == "Education":
        if len(reduced) == 0:
            for county in full_data:
                population += round(county.education[code[1]] * county.population["2014 Population"])
        else:
            for county in reduced:
                population += round(county.education[code[1]] * county.population["2014 Population"])
    elif code[0] == "Income":
        if len(reduced) == 0:
            for county in full_data:
                population += round(county.income[code[1]] * county.population["2014 Population"])
        else:
            for county in reduced:
                population += round(county.income[code[1]] * county.population["2014 Population"])
    print("Population of {}: {}".format(code[1],population))


file = open(sys.argv[1])
reduced_counties = []
for line in file:
    line = line.split(":")
    for i in range(len(line)):
        if "\n" in line[i]:
            line[i] = line[i][:-1]
    if line[0] == "display":
        display(reduced_counties)
    elif line[0] == "filter-state":
        reduced_counties = filter_state(line)
    elif line[0] == "filter-gt":
        reduced_counties = filter_gt(line,reduced_counties)
    elif line[0] == "filter-lt":
        reduced_counties = filter_lt(line,reduced_counties)
    elif line[0] == "population-total":
        population_total(line)
    elif line[0] == "population":
        population(reduced_counties)
    elif line[0] == "percent":
        percent(line,reduced_counties)
    elif line[0] == "reset":
        reduced_counties = []
    else:
        print("Not a Command!!")
