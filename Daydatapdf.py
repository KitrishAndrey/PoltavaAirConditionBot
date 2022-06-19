import matplotlib.pyplot as plt
import time

def gen_twin_graf(x, y, y2):
    fig, ax = plt.subplots()
    location =["lower left", "lower right"]
    ax1 = ax.twinx()
    ax.plot(x, y, label="CO2 мкг/м³", marker="o", color="b")
    ax1.plot(x, y2, label="PM2.5 мкг/м³", marker="v", color="orange")
    ax.legend(loc= location[0])
    ax1.legend(loc= location[1])
    ax1.set_ylabel('Покази PM2.5 мкг/м³', rotation=270, labelpad=16)
    ax.set_ylabel('Покази CO2 мкг/м³')
    ax.yaxis.label.set_size(15)
    ax1.yaxis.label.set_size(15)
    fig.set_figheight(9)
    fig.set_figwidth(13)
    plt.tick_params(axis='x', which='major', labelsize=2)
    fig.autofmt_xdate(rotation=45)
    ax.grid(which='major',color = 'k', axis='y')
    ax1.grid(which='major', color='k', axis='y')
    plt.tight_layout()
    name = "{0}_{1}.pdf".format("CO2_PM2_5", time.strftime("%H_%M_%S"))
    fig.savefig(name)
    return name

def gen_pm_graf(x, y2):
    fig, ax = plt.subplots()
    location = ["lower right"]
    ax.plot(x, y2, label="PM2.5 мкг/м³", marker="v", color="orange")
    ax.legend(loc=location[0])
    ax.set_ylabel('Покази PM2.5 мкг/м³', labelpad=16)
    ax.yaxis.label.set_size(12)
    fig.set_figheight(9)
    fig.set_figwidth(13)
    plt.tick_params(axis='x', which='major', labelsize=9)
    ax.grid(which='major', color='k', axis='y')
    fig.autofmt_xdate(rotation=45)
    plt.tight_layout()
    name = "{0}_{1}.pdf".format("PM2_5", time.strftime("%H_%M_%S"))
    fig.savefig(name)
    return name

def gen_co_graf(x, y):
    fig, ax = plt.subplots()
    location = ["lower right"]
    ax.plot(x, y, label="CO2 мкг/м³", marker="o", color="b")
    ax.legend(loc=location[0])
    ax.set_ylabel('Покази CO2 мкг/м³')
    ax.yaxis.label.set_size(12)
    fig.set_figheight(9)
    fig.set_figwidth(13)
    plt.tick_params(axis='x', which='major', labelsize=9)
    ax.grid(which='major', color='k', axis='y')
    fig.autofmt_xdate(rotation=45)
    plt.tight_layout()
    name = "{0}_{1}.pdf".format("CO2", time.strftime("%H_%M_%S"))
    fig.savefig(name)
    return name