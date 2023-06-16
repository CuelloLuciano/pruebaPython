import matplotlib.pyplot as pyplot

def generate_pie_chart():
    labels = ['A','B','C','D']
    values = [200,300,120,400]

    fig,ax = pyplot.subplots()

    ax.pie(values,labels=labels)
    pyplot.savefig('pie.png')
    pyplot.close()