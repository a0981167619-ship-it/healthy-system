import tkinter as tk
contain=tk.Tk()
entry_height=tk.Entry(contain)
entry_weight=tk.Entry(contain)
entry_age=tk.Entry(contain)
entry_gender=tk.Entry(contain)
entry_lifestyle=tk.Entry(contain)
entry_waist=tk.Entry(contain)
entry_butt=tk.Entry(contain)
entry_agegroup=tk.Entry(contain)
entry_speed=tk.Entry(contain)
contain.title('健康計算系統')
def BMI_count(height,weight):#BMI計算
       BMI=weight/(height/100)**2#身高單位換算為公尺
       return BMI
def TDEE_count(Height,weight,G,):#每日消耗熱量計算
    height=float(entry_height.get())
    weight=float(entry_weight.get())
    BMI=weight/(height/100)**2
    G=str(entry_gender.get())#輸入性別
    age=int(entry_age.get())#輸入年齡
    Height=int(entry_height.get())#身高單位為公分
    TDEE=str(entry_lifestyle.get())#輸入生活型態
    if G=='男':
       man=1.2*BMI+0.23*age-16.2#男性體脂率
       Man=(10*weight+6.25*Height-5*age+5)#男性基礎代謝率
       if TDEE=='靜態生活型態':
          TDEE=Man*1.2
       elif TDEE=='輕度活動生活型態':
           TDEE=Man*1.375
       elif TDEE=='中度活動生活型態':
            TDEE=Man*1.55
       elif TDEE=='高度活動生活型態':
            TDEE=Man*1.725
       elif TDEE=='極高度活動生活型態':
            TDEE=Man*1.9
    elif G=='女':
        woman=(1.2*BMI+0.23*age)-5.4#女性體脂率
        Woman=(10*weight+6.25*Height-5*age-161)#女性基礎代謝率
        if TDEE=='靜態生活型態':
           TDEE=Woman*1.2
        elif TDEE=='輕度活動生活型態':
           TDEE=Woman*1.375
        elif TDEE=='中度活動生活型態':
           TDEE=Woman*1.55
        elif TDEE=='高度活動生活型態':
            TDEE=Woman*1.725
        elif TDEE=='極高度活動生活型態':
            TDEE=Woman*1.9

def WHR_calculate(waist,butt):#腰臀比計算
    WHR=float(waist/butt)
    return WHR
        
def normal_weight(G,height):#標準體重計算
    G=str(entry_gender.get())
    height=float(entry_height.get())#身高單位公分
    if G=='男':
        normal=(height-80)*0.7#男性標準體重計算
    elif G=='女':
        normal=(height-70)*0.6#女性標準體重計算
    return normal
    

def water_day(life,weight):#每日喝水量計算:
    life=str(entry_lifestyle.get())#輸入生活型態
    weight=float(entry_weight.get())#體重單位為公斤
    if life=='一般人':
        water=weight*30
    elif life=='有減重需求'or life=='運動量大':
        water=weight*40 

    return water

def big_heart(well_age,age):#最大心跳率計算:
    well_age=str(entry_agegroup.get())#輸入年齡層
    age=int(entry_age.get())#輸入年齡
    if well_age=='中年人' or '老年人':
        heart=208-(0.7*age)
        return heart
    else:
        heart=220-age
    return heart

def lose_weight(height,weight,G,age):#去脂體重計算:
    height=float(entry_height.get())
    weight=float(entry_weight.get())
    BMI=weight/(height/100)**2
    G=str(entry_gender.get())#輸入性別
    age=int(entry_age.get())#輸入年齡
    if G=='男':
       man=1.2*BMI+0.23*age-16.2#男性體脂率
       lose_w=weight-(weight*man)#男性去脂體重計算
       return lose_w
    elif G=='女':
        woman=(1.2*BMI+0.23*age)-5.4#女性體脂率
        lose_w=weight-(weight*woman)#女性去脂體重計算
        return lose_w

def everyday_feetlose(weight,height,speed):#每日步數消耗熱量
    weight=float(entry_weight.get())
    height=float(entry_height.get())
    height=height/100
    speed=float(entry_speed.get())
    Height=height/100#身高單位換算為公尺
    Lcalor=0.035*weight+(speed**2/Height)*0.029*weight#計算消耗熱量
    return Lcalor

def circle_body(waist,height):#計算身體圓形指數(BRI)
    waist=int(entry_waist.get())#輸入腰圍
    height=float(entry_height.get())
    BRI=364.2-365.5*((1-waist/2*3.14159)**2/(0.5*height)**2)**(1/2)#計算身體圓形指數(BRI)
    return BRI

def muscle_mass(height,weight,age,G):#計算肌肉量:
      height=float(entry_height.get())
      weight=float(entry_weight.get())
      BMI=weight/(height/100)**2#身高單位換算為公尺
      age=int(entry_age.get())#輸入年齡
      G=str(entry_gender.get())#輸入性別
      if G=='男':
          man=1.2*BMI+0.23*age-16.2#男性體脂率
          not_fat=weight-(weight*man)#計算無脂肪體重
          FFMI=not_fat/(height/100)#計算肌肉量
          return FFMI
      elif G=='女':
          woman=(1.2*BMI+0.23*age)-5.4#女性體脂率
          not_fat=weight-(weight*woman)#計算無脂肪體重
          FFMI=not_fat/(height/100)#計算肌肉量
          return FFMI

def run():#輸出BMI
    try:
        height=float(entry_height.get())
        weight=float(entry_weight.get())
        bmi=BMI_count(height,weight)
        if bmi<18.5:
          text='體重過輕'
        elif 18.5<=bmi<24:
         text='健康體重'
        elif 24<=bmi<27:
         text='過重'
        elif 27<=bmi<30:
         text='輕度肥胖'
        elif 30<=bmi<35:
         text='中度肥胖'
        else:
         text='重度肥胖'
       

        BMI_result.config(text='BMI值為:'+'  '+str(round(bmi,2)))
        bmi_result.config(text=text)
        
    except :
        BMI_result.config(text='請輸入正確數值')

tk.Label(contain,text='身高').pack()
entry_height=tk.Entry(contain)
entry_height.pack()

tk.Label(contain,text='體重').pack()
entry_weight=tk.Entry(contain)
entry_weight.pack()

BMI_result=tk.Label(contain,text='BMI')
BMI_result.pack()

bmi_result=tk.Label(contain,text='BMI')
bmi_result.pack()

tk.Button(contain,text='計算BMI',command=run).pack()


def ramble():#輸出腰臀比
    try:
       G=str(entry_gender.get())#輸入性別
       waist=float(entry_waist.get())#輸入腰圍
       butt=float(entry_butt.get())#輸入臀圍
       WHR=WHR_calculate(waist,butt)
       if G=='女':
         if WHR<=0.80:
            text='健康風險低'
         elif 0.81<=WHR<=0.85:
            text='健康風險適中'
         elif WHR>=0.86:
            text='健康風險高'

         if G=='男':
          if WHR<=0.95:
            text='健康風險低'
         elif 0.96<=WHR<=1.0:
            text='健康風險適中'
         elif WHR>=1.0:
            text='健康風險高'
        
         WHR_result.config(text='腰臀比為:'+ '  '+str(round(WHR,2)))
         whr_result.config(text=text)
    except:
         WHR_result.config(text='請輸入正確數值')

tk.Label(contain,text='性別').pack()
entry_gender=tk.Entry(contain)
entry_gender.pack()
tk.Label(contain,text='腰圍').pack()
entry_waist=tk.Entry(contain)
entry_waist.pack()
tk.Label(contain,text='臀圍').pack()
entry_butt=tk.Entry(contain)
entry_butt.pack()
WHR_result=tk.Label(contain,text='腰臀比')
WHR_result.pack()
whr_result=tk.Label(contain,text='腰臀比')
whr_result.pack()
tk.Button(contain,text='計算腰臀比',command=ramble).pack()


def correct():#輸出每日喝水量
    try:
      life=str(entry_lifestyle.get())#輸入生活型態
      weight=float(entry_weight.get())#體重單位為公斤
      water1=water_day(life,weight)
      if life=='一般人':
        water=weight*30
        water_result.config(text='每日喝水量為:'+str(round(water1,2)))
      elif life=='有減重需求'or life=='運動量大':
        water=weight*40
        water_result.config(text='每日喝水量為:'+str(round(water1,2)))
    except :
       water_result.config(text='請輸入正確數值')

tk.Label(contain,text='生活型態').pack()
entry_lifestyle=tk.Entry(contain)
entry_lifestyle.pack()

water_result=tk.Label(contain,text='每日喝水量')
water_result.pack()

tk.Button(contain,text='計算每日喝水量',command=correct).pack()

def feet_runoutof():#輸出每日步數消耗熱量
   try:
      weight=float(entry_weight.get())
      height=float(entry_height.get())
      speed=float(entry_speed.get())
      feet=everyday_feetlose(weight,height,speed)
      feet_result.config(text='每日步數消耗熱量為:'+str(round(feet,2)))
      Feet_result.config(text='每日步數消耗熱量為:')
   except:
       feet_result.config(text='請輸入正確數值')
       
tk.Label(contain,text='速度').pack()
entry_speed=tk.Entry(contain)
entry_speed.pack()

feet_result=tk.Label(contain,text='feet')
feet_result.pack()

Feet_result=tk.Label(contain,text='feet')
Feet_result.pack()

tk.Button(contain,text='計算每日步數消耗熱量',command=feet_runoutof).pack()

def circle():#輸出身體圓形指數
   try:
     waist=int(entry_waist.get())
     height=float(entry_height.get())
     circle=circle_body(waist,height)
     if circle<3.41:
        text='最不圓'
     elif 3.41<circle<4.5:
        text='偏瘦'
     elif 4.5<circle<5.5:
        text='正常範圍'
     elif 5.5<circle<6.9:
        text='偏圓'
     else:
        text='身體最圓'

     circle_result.config(text='身體圓形指數為:'+str(round(circle,2)))
     Circle_result.config(text=text)
   except:
       circle_result.config(text='請輸入正確數值')

circle_result=tk.Label(contain,text='身體圓形指數')
circle_result.pack()

Circle_result=tk.Label(contain,text='身體圓形指數')
Circle_result.pack()

tk.Button(contain,text='計算身體圓形指數',command=circle).pack()

def large_heart():#輸出最大心率
    try:
       well_age=str(entry_agegroup.get())#輸入年齡層
       age=int(entry_age.get())#輸入年齡
       largeheart=big_heart(well_age,age)
       if well_age=='中年人' or well_age=='老年人':
        heart=208-(0.7*age)
        text=heart
       else:
         heart=220-age
         text=heart

       large_heart_result.config(text='最大心率為:'+str(largeheart))
       
    except:
       large_heart_result.config(text='請輸入正確數值')

tk.Label(contain,text='年齡層').pack()
entry_agegroup=tk.Entry(contain)
entry_agegroup.pack()

tk.Label(contain,text='年齡').pack()
entry_age=tk.Entry(contain)
entry_age.pack()

large_heart_result=tk.Label(contain,text='最大心率')
large_heart_result.pack()

tk.Button(contain,text='計算最大心率',command=large_heart).pack()

def standard():#輸出標準體重
   try:
      G=str(entry_gender.get())
      height=float(entry_height.get())
      normal1=normal_weight(G,height)
      if G=='男':
        normal=(height-80)*0.7
        text=normal
      elif G=='女':
        normal=(height-70)*0.6
        text=normal
      normal_weight_result.config(text='標準體重為:'+str(round(normal1,2)))

   except:
      normal_weight_result.config(text='請輸入正確數值')

normal_weight_result=tk.Label(contain,text='標準體重')
normal_weight_result.pack()

tk.Button(contain,text='計算標準體重',command=standard).pack()

def lost_weight():
   try:
      height=float(entry_height.get())
      weight=float(entry_weight.get())
      G=str(entry_gender.get())
      age=int(entry_age.get())
      BMI=weight/(height/100)**2
      lost1=lose_weight(height,weight,G,age)
      if G=='男':
       lost=1.2*BMI+0.23*age-16.2
       text=weight-(weight*lost)
      elif G=='女':
        lost=(1.2*BMI+0.23*age)-5.4
        text=weight-(weight*lost)
        lost_weight_result.config(text='去脂體重為:'+str(round(lost1,2)))

   except:
      lost_weight_result.config(text='請輸入正確數值')

lost_weight_result=tk.Label(contain,text='去脂體重')
lost_weight_result.pack()

tk.Button(contain,text='計算去脂體重',command=lost_weight).pack()

def