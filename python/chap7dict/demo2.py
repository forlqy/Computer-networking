#获取字典的元素
scores={'张三':100,'莉丝':98,'王五':94}
'''使用[],会抛出异常'''
print(scores['张三'])

'''使用get()方法'''
print(scores.get('张三'))
print(scores.get('羊羊')) #默认为None
print(scores.get('学学',99)) #指定提供默认值，在学学不存在是用get()返回