'''key的判断'''
scores={'张三':100,'莉丝':98,'王五':94}
print('张三' in scores)
print('张三' not in scores)

del scores['张三']
print(scores)
scores.clear() #清空列表
print(scores)

scores['溜溜']=98 #新增元素
print(scores)
scores['溜溜']=100 #修改元素
print(scores)