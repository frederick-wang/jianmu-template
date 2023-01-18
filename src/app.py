from reactivity import ref, computed, watch_effect
from ltp import LTP
from utils.p import fig_b64, apple_count, plot_title
import base64
from jianmu import base64_to_bytes
import pandas as pd

ltp = LTP()

count = ref(0)
# 创建一个响应式变量 name，初始值为 'World'
name = ref('World')
# 创建一个响应式变量 result
result = computed(lambda: {
    'message': f'Hello {name.value}',
    'count': count.value,
})


def add_count():
    count.value += 1
    # print(f'count is {count.value} now')


sentence = ref('他叫汤姆去拿外衣')


def getter():
    return ltp.pipeline([sentence.value], tasks=["cws"], return_dict=False)[0]


sent_split = computed(getter)

file_list = ref([])

file_content_list = ref([])


def test():
    print('file_list is updated!')
    tmp = []
    for file in file_list.value:
        data = file['raw']['data']
        if data['type'] == 'text/plain':
            base64_str = base64_to_bytes(data['base64']).decode('utf-8')
            tmp.append(base64_str)
        elif data['type'] == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            df = pd.read_excel(base64_to_bytes(data['base64']))
            tmp.append(df.to_markdown())
    file_content_list.value = tmp
    print()


watch_effect(test)
