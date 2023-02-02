from reactivity import ref, computed, watch_effect
from ltp import LTP
from utils.p import fig_b64, apple_count, plot_title
from jianmu import File, show_save_dialog
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
    return ltp.pipeline([sentence.value], tasks=["cws"])


sent_split = computed(getter)

file_list = ref([])

file_content_list = ref([])


def test():
    tmp = []
    for file in file_list.value:
        raw: File = file['raw']
        if raw.type == 'text/plain':
            text = raw.bytes.decode('utf-8')
            tmp.append(text)
        elif raw.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            df = pd.read_excel(raw.bytes)
            tmp.append(df.to_markdown())
    file_content_list.value = tmp


watch_effect(test)


def clear_file():
    file_list.value = []


test_bytes = ref(b'123456')


def test_save():
    show_save_dialog({}, lambda x: print(x))
