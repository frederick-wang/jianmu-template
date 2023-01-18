import base64
import io

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

    # convert plot to base64
    fig_bytes = io.BytesIO()
    fig.savefig(fig_bytes, format='png')
    fig_bytes.seek(0)
    fig_b64 = 'data:image/png;base64,' + base64.b64encode(fig_bytes.read()).decode('utf-8')
    plt.close()
    return fig_b64


fig_b64 = computed(fig_b64_update)
