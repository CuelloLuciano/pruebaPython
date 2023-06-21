import utils
import read_csv
import charts
def run():
    data = read_csv.read_csv('data.csv')
    countries = list(map(lambda x: x['Country/Territory'], data))
    percents = list(map(lambda x: float(x['World Population Percentage']), data))

    charts.generate_pie_chart(countries,percents)

    country = input('Type Country => ')
    countrydata = utils.population_by_country(data,country)
    if(len(countrydata)>0):
        print(country)
        keys, values =utils.get_population(countrydata[0])
        charts.generate_bar_chart(country,keys, values)
    else:
        print('no habia data')


if __name__ == '__main__':
  run()