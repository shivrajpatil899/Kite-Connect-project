import matplotlib.pyplot as plt
import pandas as pd

PATH = 'output_excel/BANKNIFTY/41 DTE/'
FILE = '2023-06-02-0dte'


def plot_graph(df1=None, df2=None):
    if df1 is None:
        var1 = pd.read_excel('{}{}.xlsx'.format(PATH, FILE), sheet_name=0)
    else:
        var1 = pd.DataFrame(df1)

    # var1['ConvertedDate'] = var1['date'].dt.strftime('%d/%s').astype(str)
    if df2 is None:
        var2 = pd.read_excel('{}{}.xlsx'.format(PATH, FILE), sheet_name=1)
    else:
        var2 = pd.DataFrame(df2)
    premium_collected = var1['close'][0]+var2['close'][0]
    plt.plot((premium_collected - (var1['close']+var2['close']))*100/premium_collected)
    plt.savefig('{}.png'.format(FILE))
    # plt.gcf().autofmt_xdate()
    # plt.xticks(ticks=)
    plt.show()
