from jianmu import ref, computed
from ltp import LTP

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

sentence = ref('他叫汤姆去拿外衣')

sent_split = computed(lambda: ltp.pipeline([str(sentence.value)], tasks = ["cws"], return_dict = False)[0])
