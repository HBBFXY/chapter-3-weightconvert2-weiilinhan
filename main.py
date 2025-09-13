begin_weight = float(input('请输入你当前在地球上的体重:'))
print('未来10年地球和月球体重变化：')
for i in range(1,11):
  earth_weight = begin_weight + 0.5 * i
  moon_weight = earth_weight * 0.165
  print（f'第{i}年:地球上的体重{earth_weight:.2f}kg,月球上的体重{moon_weight:.2f}kg'）
    
    
  


