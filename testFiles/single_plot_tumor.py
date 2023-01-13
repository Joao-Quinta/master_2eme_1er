import sys
import ast
import numpy as np
from matplotlib import pyplot as plt
import os
from os import path

import scipy


def replication_time(directory):
    file = directory
    plt.rcParams["figure.figsize"] = (12,9)
    figname = "Plot_replication_time/" + directory + ".png"
    # print(figname)
    if os.path.exists(file) == True:
        nb_n = []
        nb_c = []
        l_ds = []
        sum = 0
        print(file, "exists")
        with open(file, "r") as f:

            allines = f.readlines()  # create a list of line
            # print(allines)
            # print("allines ", len(allines))
            for i in range(len(allines)):  # liste où chaque element correspond à une itération
                l_nb_c = []
                line = allines[i].split()  # on prend une ligne = une itération
                # print(line)
                n = 0
                c = 0
                density_sentinelle = line[0]
                l_ds.append(density_sentinelle)
                for j in range(1, len(line)):  # on parcourt cette ligne
                    cell_data = float(line[j])
                    # print(len(cell_data))
                    l_nb_c.append(cell_data)
                # print(l_nb_c)

                t = np.linspace(0, (len(l_nb_c)) - 1, len(l_nb_c))
                plt.plot(t, l_nb_c)

    plt.ylim([0, 7000])

    plt.title("Cellules cancéreuses en fonction de la densité de sentinelles dans le tissu")
    plt.legend(l_ds, fontsize=9, bbox_to_anchor=(0.5, -0.12), ncol=len(l_ds), loc="lower center")

    plt.ylabel("nombre de cellules cancéreuses")
    plt.xlabel("jours")
    plt.show()
    # plt.savefig(figname)


replication_time('write_sentinelle')
