from jianmu import figure_to_datauri

import matplotlib.pyplot as plt
from reactivity import computed, ref

apple_count = ref(40)
plot_title = ref('Fruit supply by kind and color')


def fig_b64_update():
    fig, ax = plt.subplots()

    fruits = ['apple', 'blueberry', 'cherry', 'orange']
    counts = [apple_count.value, 100, 30, 55]
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('fruit supply')
    ax.set_title(plot_title.value)
    ax.legend(title='Fruit color')

    return figure_to_datauri(fig)


fig_b64 = computed(fig_b64_update)
