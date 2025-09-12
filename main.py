begin_weight=float(input())
moon_change = 0.165
earth = 0.5
for i in range(1,11):
    earth_weight=begin_weight+earth*i
    moon_weight=earth_weight*moon_change
    print（f"第{i}年，地球体重为{earth_weight:.2f}kg,月球体重为{moon_weight:.2f}kg"）
    
    
  


