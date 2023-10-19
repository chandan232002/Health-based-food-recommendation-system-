from tkinter  import *
from tkinter import ttk
from PIL import ImageFilter,Image
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def getvals():
      
      
      for i,j in my_dict.items():
        if(j==e6.get()):
          print("Selected Region:- ","(",i,")",e6.get())
          Region_para = i




      height=float(e1.get())
      weight=float(e2.get())
      age=int(e3.get())
      gender=StringVar(e4)
      activity_level = StringVar(e5)


     
      isVegpara = var.get()

      
      
      height_m = height / 100
      bmi = weight / (height_m ** 2)
      bmi = round(bmi, 2)
      activity_factor = 1.2
      # Calculate BMR
      if gender == 'male':
        desired_calorie_intake = 2500
        bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    
      else:
        desired_calorie_intake = 2000
        bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)

       
      print("welcome User", e0.get())
      #conditions
      print("Your body mass index is: ", bmi)
      if ( bmi < 16):
        print("Acoording to your BMI, you are Severely Underweight")
         
      elif ( bmi >= 16 and bmi < 18.5):
        print("Acoording to your BMI, you are Underweight")
        
      elif ( bmi >= 18.5 and bmi < 25):
        print("Acoording to your BMI, you are Healthy")
        
      elif ( bmi >= 25 and bmi < 30):
        print("Acoording to your BMI, you are Overweight")
        
      elif ( bmi >=30):
        print("Acoording to your BMI, you are Severely Overweight")
        


# Calculate calories
      if activity_level == 'sedentary':
       calories = bmr * 1.2
      elif activity_level == 'lightly_active':
       calories = bmr * 1.375
      elif activity_level == 'moderately_active':
        calories = bmr * 1.55
      elif activity_level == 'very_active':
       calories = bmr * 1.725
      else:
       calories = bmr * 1.9
       
    
   

      df = pd.read_csv(r"IndianFoodDatasetXLSFinal (3).csv", encoding='unicode_escape')
      tdee = bmr * activity_factor
      print("calories requirementfor your body",tdee)
      calories_to_burn= tdee-desired_calorie_intake
      calories_to_burn= calories_to_burn * (-1)

      calorie_difference = desired_calorie_intake 


      print("calories should be (-)burned/(+)gain","{:.2f}".format(calories_to_burn))
      num_predictions = 6  
      predictions = []

      for _ in range(num_predictions):
        df_filtered = df[(df['isVeg'] == isVegpara) & (df['Regions'] == Region_para) &(df['totalCaloriesInCal'] <= calorie_difference) ]
        
    
        if df_filtered.empty:
          print("No more suitable food items available.")
          break
    
        features = df_filtered[['totalCaloriesInCal' , 'Regions' , 'isVeg' ]]
        target = df_filtered[['name', 'cuisine', 'course']]
        dt = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=0)
        dt.fit(features, target)

        prediction = dt.predict(features.iloc[[0]])
        food_name = prediction[0][0]
        food_calories = df[df['name'] == food_name]['totalCaloriesInCal'].values[0]
        food_cuisine = df[df['name'] == food_name]['cuisine'].values[0]
        food_time = df[df['name'] == food_name]['course'].values[0]
        food_isVeg = df[df['name'] == food_name]['isVeg'].values[0]
        food_Regpara = df[df['name'] == food_name]['Regions'].values[0]
        predictions.append((food_name, food_calories, food_cuisine, food_time, food_isVeg , food_Regpara))


        df = df[df['name'] != food_name]

        calorie_difference -= food_calories

      print("Recommended Food:")
        
      for food_name, food_calories, food_cuisine, food_time ,food_isVeg , food_Regpara in predictions:  
          
         print("Dish name-",food_name, ",food calories-", food_calories, ",Food Type-", food_cuisine, ",Food Time-", food_time,",veg(1)/non-veg(0)", food_isVeg, ",Region parameter-", food_Regpara)
        
      quit()   #exit 
    


def quit():  #for quit button
    quit
      

if __name__ == '__main__':
    main_win = Tk()
    
    Label(main_win,text="Enter your Name").grid(row=0,column=0,sticky=W,pady=4)
    Label(main_win,text="Enter your Height (in cm)").grid(row=1,column=0,sticky=W,pady=4)
    Label(main_win,text="Enter your Weight (in kg)").grid(row=2,column=0,sticky=W,pady=4)
    Label(main_win,text="Age").grid(row=3,column=0,sticky=W,pady=4)
    Label(main_win,text="gender(male/female)").grid(row=4,column=0,sticky=W,pady=4)
    Label(main_win,text="activity level :").grid(row=5,column=0,sticky=W,pady=4)
    Label(main_win,text="what type of food you likes to eat ?:").grid(row=6,column=0,sticky=W,pady=0)
    Label(main_win,text="Are you vegeterian ?:").grid(row=7,column=0,sticky=W,pady=0)

    e0 = Entry(main_win, textvariable= StringVar())  #user name
    e1 = Entry(main_win)
    e2 = Entry(main_win)
    e3 = Entry(main_win)
    e4 = Entry(main_win, textvariable= StringVar())
    e5 = Entry(main_win, textvariable= StringVar())
    e6 = StringVar()

    var =IntVar()  #for radio button


     # dropdown box  1
    my_dict={0:'Indian', 1:'South Indian', 2:'Andhra',3: 'Udupi', 4:'Mexican', 5:'Fusion', 6:'Continental', 7:'Bengali', 8:'Punjabi', 9:'Chettinad', 10:'Tamil Nadu', 11:'Maharashtrian', 12:'North Indian', 13:'Italian', 14:'Sindhi', 15:'Thai', 16:'Chinese', 17:'kerala', 18:'Gujarati ', 19:'Coorg', 20:'Rajasthani', 21:'Asian', 22:'Middle Eastern', 23:'Coastal Karnataka', 24:'European', 25:'Kashmiri', 26:'Karnataka', 27:'Lucknowi', 28:'Hyderabadi', 29:'Andaman', 30:'Goan', 31:'Assamese', 32:'Bihari', 33:'Malabar', 34:'Himachal', 35:'Awadhi', 35:'Cantonese', 36:'North East India', 37:'Pakistani', 38:'Mughlai', 39:'Japanese', 40:'Mangalorean', 41:'Vietnamese', 42:'British', 43:'North Karnataka', 44:'Parsi', 45:'Greek',46: 'Nepalese', 47:'oriya',+ 48:'French', 49:'Sichuan', 50:'Indo Chinese', 51:'Konkan', 52:'Mediterranean',53: 'Sri Lankan', 54:'Haryana', 55:'Gujarati', 56:'Uttar Pradesh', 57:'Malvani Indonesian', 58:'African', 59:'Shandong', 60:'Korean', 61:'American', 62:'Kongunadu', 63:'Caribbean', 64:'South Karnataka', 65:'Arab' }
    cuisine=list(my_dict.values())       # options region
    c1 = ttk.Combobox(main_win, values=cuisine,width=17, textvariable=e6) # Combobox
    c1.grid(row=6,column=1,sticky=W,pady=4) # adding to grid
    c1.set('select anyone') # default selected option



     # dropdown box  2
    act =['sedentary','lightly_active','moderately_active','very_active'] # options  Activity level
    e5 = ttk.Combobox(main_win, values=act,width=17) # Combobox
    e5.grid(row=5,column=1,sticky=W,pady=4) # adding to grid
    e5.set('select anyone') # default selected option

    # dropdown box  3
    gender =['male', 'female'] # options  gender
    e4 = ttk.Combobox(main_win, values=gender,width=17) # Combobox
    e4.grid(row=4,column=1,sticky=W,pady=4) # adding to grid
    e4.set('select anyone') # default selected option

    
    


    R1 =  Radiobutton(main_win, text="Yes" , pady=4  , variable= var , value= 1).grid(row=7,sticky=W,column=1,pady=0) #
    R2 =  Radiobutton(main_win, text="No" ,pady=4  , variable= var , value= 0).grid(row=7,column=1,padx=40) #sticky=W,

    
    e0.grid(row=0, column=1)
    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)

    

    Button(main_win,fg="Black",background="green",text='ENTER',borderwidth=8,command=getvals).grid(row=8,column=0,sticky=W,pady=4)
    Button(main_win,fg="Black",background="red",text='EXIT',borderwidth=8,command=main_win.quit).grid(row=8,column=5,sticky=W,pady=4)

    main_win.geometry("600x300")
    main_win.minsize(600,300)
    main_win.maxsize(1000,350)

    main_win.wm_title("Health recommendation system by:- SCSS for PRMCEAM")

    

    main_win.mainloop()

   


