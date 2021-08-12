import random

question = input('你有什么要问你对象的？（退出输入“臣告退”）')
Answer = ['你有没有考虑过我的感受?',
          '你变了，以前你很宠我的',
          '你再说一遍试试',
          '没想到你是这样的人',
          '你确定',
          '应该辩证地来看',
          '哦 这样啊',
          '哈哈哈哈'
          '很好',
          '没问题']
while question != '臣告退':
    answer0=list(question)
    answer1=answer0[:]
    for i in range(len(answer1)):
        try:
            if answer1[i]=='我' and answer1[i+1]!='们':
                answer0[i]='你'
            elif answer1[i]=='你' and answer1[i+1]!='们':
                answer0[i] = '我'
        except:
            if answer1[i]=='我':
                answer0[i]='你'
            elif answer1[i]=='你' :
                answer0[i] = '我'
    answer =''.join(answer0)
    # answer0 = question.replace('我们', '312bca')
    # answer0 = answer0.replace('你', '312xyz你')
    # answer0 = answer0.replace('我', '312xyz我')
    # answer0 = answer0.replace('312xyz你', '我')
    # answer0 = answer0.replace('312xyz我', '你')
    # answer = answer0.replace('312bca', '我们')

    if '是不是' in question:
        answer = answer.replace('是不是', '不')
        if '了' in question:
            answer = answer.replace('了', '')
    elif '要不要' in question:
        answer = answer.replace('要不要', '不要')
    elif '好不好' in question:
        answer = answer.replace('好不好', '不好')
    elif '用不用' in question:
        answer = answer.replace('用不用', '不用')
    elif '还' in question:
        answer = answer.replace('还', '怎么不')
        if '了吗' in question:
            answer = answer.replace('了吗', '')
        elif '吗' in question:
            if '有' in question:
                answer = answer.replace('有', '没有')
            else:
                answer = answer.replace('吗', '')
    elif '了吗' in question:
        answer = answer.replace('了吗', '')
        answer = '没' + answer
    elif '能' in question and '能不能'not in question:
        answer = answer.replace('能', '不能')
    elif '行' in question:
        answer = answer.replace('行', '不行')
        if '了吗' in question:
            answer = answer.replace('了吗', '')
    elif '吗' in question:
        if '有' in question:
            answer = answer.replace('有', '没有')
        else:
            answer = answer.replace('吗', '')
            answer = '不' + answer
    elif '为什么' in question:
        answer = answer.replace('为什么', '为什么不能')
    elif '怎么' in question:
        if '回事' in question or '啦' in question or '了' in question:
            answer = '我愿意'
        else:
            answer = answer.replace('怎么', '怎么不能')
    elif '没' in question:
        if '有没有' in question:
            answer = '没有'
        else:
            answer = answer.replace('没', '')
    elif '什么' in question or '谁' in question or '啥' in question:
        answer = '我就不想说'
    elif '呢' in question:
        answer = '也一样'
    elif '吧' in question or '呗' in question or '哪' in question:
        answer = '你说呢'
    else:
        i = random.randint(0, 9)
        answer = Answer[i]

    if '不我' in answer and '不我' not in question:
        answer = answer.replace('不我', '我不')
    if '不你' in answer and '不你' not in question:
        answer = answer.replace('不你', '你不')
    if '不没' in answer and '不没' not in question:
        answer = answer.replace('不没', '')
    if '没我' in answer and '没我' not in question:
        answer = answer.replace('没我', '我没')
    if '没你' in answer and '没你' not in question:
        answer = answer.replace('没你', '你没')
    if '不不' in answer and '不不' not in question:
        answer = answer.replace('不不', '')

    print('你对象：', answer)

    question = input('还有什么要问的？不聊了就输入“臣告退”')