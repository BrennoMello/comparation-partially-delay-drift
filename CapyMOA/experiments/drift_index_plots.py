import matplotlib.pyplot as plt
import pandas as pd
import types

def plotline(dataset_name,
              yvalues,
              loc_legend="upper right",
              figure_name=None,
              axis=[0, 1010, 40, 100],
              classifiers=['HoeffdingTree'],
              drifts=None,
              gradual_drift=None,
              xvalues=[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
              xlabel='# instances (thousands)',
              ylabel='accuracy'):

    #plt.title(dataset_name + ' - ' + ylabel)
    plt.title(dataset_name)
    plt.axis(axis)
    plt.ylim(0, 10)
    plt.xticks(ticks=range(0,102,5))

    line_style = ['-o', '-x', '-p', '-1', '-s', '-v', '-d']
    idx = 0
    stream_classifier = []
    for classifier in classifiers:
        #plotted, = plt.plot(xvalues, yvalues[classifier], line_style[idx % len(line_style)], label=classifier)
        plotted = plt.bar(xvalues, yvalues[classifier])
        stream_classifier.append(plotted)
        idx+=1

    #plt.axhline(y=0, xmax=1, color='black', ls='--')

    if drifts is not None:
        for drift in drifts:
            if gradual_drift is not None:
                if isinstance(gradual_drift, list) is False:
                    plt.axvline(x=drift-gradual_drift, ymax=1, color='r', ls='--')
                    plt.axvline(x=drift+gradual_drift, ymax=1, color='r', ls='--')
            plt.axvline(x=drift, ymax=0.1, color='r', linestyle='--')

    if isinstance(gradual_drift, list):
        for i in range(0,len(gradual_drift)):
            if gradual_drift[i] > 0:
                plt.axvline(x=drifts[i]-gradual_drift[i], ymax=1, color='r', ls='--')
                plt.axvline(x=drifts[i]+gradual_drift[i], ymax=1, color='r', ls='--')

    #plt.legend(stream_classifier, classifiers, loc=loc_legend, ncol=2)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)

    if figure_name is None:
        figure_name = 'plot.pdf'

    plt.savefig(figure_name+ '.pdf')
    plt.clf()

def read_file():
    #files_path = glob.glob(f'../results/abrupt_agraw1/trees.HoeffdingTree_ADWIN_100000_95_0_AGRAW1_Abrupt.csv')
    df = pd.read_csv('../results/abrupt_agraw1/trees.HoeffdingTree_ADWIN_100000_99_0_AGRAW1_Abrupt.csv')
    list_value = df['detected changes'].tolist()
    latest_value = list_value[0]
    print(list_value)
    list_index = list()
    list_filter_values = list()
    for index in range(0, len(list_value)-1):
        if list_value[index+1] != latest_value and list_value[index+1] != 0:
            list_index.append(index+1)
            list_filter_values.append(list_value[index+1]-latest_value)
            latest_value = list_value[index+1]
            
       

    return list_filter_values, list_index


def plot_no_delay():
    #list_value, list_index = read_file()
    list_value = [2, 2, 4, 2]
    # list_index = [20032, 20064, 40160, 40224, 60032, 60064, 60096, 60160, 80064, 80096]
    list_index = [20, 40, 60, 80]
    ex1abrupt_yvalues = {'ADWIN': list_value}
    print(ex1abrupt_yvalues)
    print(list_index)
    #ex1abrupt_xvalues = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
    plotline(dataset_name='No delay',
                yvalues=ex1abrupt_yvalues,
                axis=[0, 102, 0, 100],
                classifiers=['ADWIN'],
                xvalues=list_index,
                figure_name='cd_HoffdingTree + ADWIN_no_delay',
                drifts=[20, 40, 60, 80],
                gradual_drift=None,
                ylabel='# drifts detected',
                xlabel='# instances (thousands)')
    
def plot_delay():
    #list_value, list_index = read_file()
    list_value = [2, 2, 4, 2]
    # list_index = [30032, 30064, 50160, 50224, 70032, 70064, 70096, 70160, 90064, 90096]
    list_index = [30, 50, 70, 90]
    ex1abrupt_yvalues = {'ADWIN': list_value}
    print(ex1abrupt_yvalues)
    print(list_index)
    #ex1abrupt_xvalues = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
    plotline(dataset_name='Delayed labelling (10,000)',
                yvalues=ex1abrupt_yvalues,
                axis=[0, 102, 0, 100],
                classifiers=['ADWIN'],
                xvalues=list_index,
                figure_name='cd_HoffdingTree + ADWIN_delayed_10k',
                drifts=[20, 40, 60, 80],
                gradual_drift=None,
                ylabel='# drifts detected',
                xlabel='# instances (thousands)')
if __name__ == "__main__":
    #plot_no_delay()
    plot_delay()


    