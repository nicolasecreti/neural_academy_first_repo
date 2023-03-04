import pandas as pd
from matplotlib import pyplot as plt

def main():
    #legge il file csv
    df = pd.read_csv(
        'datasets/OPSD_Germany_all.csv',
        parse_dates=True,
        index_col='Date'
    )
    #produce il grafico
    df['Consumption'].plot(figsize=(15, 6),
                           marker='.',
                           markersize=3,
                           linestyle='')
    plt.title('Consumptions Plot')
    plt.savefig('figure.png')
    
if __name__=='__main__':
    main()