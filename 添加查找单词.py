dictionary = {}
flag = 'a'
pape = 'a'
off = 'a'
while flag == 'a' or 'c':
    flag = raw_input("添加或查找单词？(a/c)")
    if flag == 'a':
        word = raw_input("输入单词(key):")
        defintion = raw_input('输入定义值(value):')
        dictionary[str(word)] = str(defintion)
        print '添加成功！'
        pape = raw_input('你是否要查找字典？(a/o)')
        if pape == 'a':
            print dictionary
        else:
            continue
    elif flag == 'c':
        check_word=raw_input('要查找的单词：')
        for key in sorted(dictionary.keys()):
            if str(check_word) == key:
                print '该单词存在！',key,dictionary[key]
                break
            else:
                off='b'
        if off == 'b':
            print '抱歉，该值不存在！'
    else:
        print 'error'
        break

