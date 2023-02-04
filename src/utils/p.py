from jianmu import figure_to_datauri

import matplotlib.pyplot as plt
from reactivity import computed, ref

plot_cnt = ref(40)
plot_title = ref('Fruit supply by kind and color')


def fig_getter():
    fig, ax = plt.subplots()

    fruits = ['apple', 'blueberry', 'cherry', 'orange']
    counts = [plot_cnt.value, 100, 30, 55]
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('fruit supply')
    ax.set_title(plot_title.value)
    ax.legend(title='Fruit color')

    return figure_to_datauri(fig)


fig = computed(fig_getter)
