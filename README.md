# Python
# Recipe application
 -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 17:49:17 2023

@author: Florent
"""

# import the library needed to add message box, picture and import file.
import tkinter as tk 
from tkinter import messagebox 
from tkinter import filedialog as fd
from tkinter import PhotoImage
# import pickle
# import os





class Recipe: 
    def __init__(self): 
        self.main_window = tk.Tk() 
        
        #  setting background color and app logo
        self.main_window.configure(background='#D2BF55')
        
        photo = "C:\\Users\Florent\.spyder-py3\mon_logo.png"
        image = PhotoImage(file=photo)
        logo_label = tk.Label(self.main_window, image=image, width=600,height=60)
        logo_label.pack(pady=5)
        
         # set app window title, create frames
        self.main_window.title('RecipeBox')
        self.search_frame = tk.Frame(self.main_window)
        self.register_frame = tk.Frame(self.main_window)
        self.listbox_frame = tk.Frame(self.main_window,background='#D2BF55')
        self.text_frame = tk.Frame(self.main_window)
        self.add_recipe_frame= tk.Frame(self.main_window, background= "#D2BF55")
        self.edit_frame = tk.Frame(self.main_window, background="#D2BF55")
        
        #Create labels, labels entries, textbox
        self.title = tk.Label(self.search_frame, text= 'International Recipe Tool', font="Times 20 italic bold")
        self.login = tk.Label(self.register_frame, text='Login')
        self.password = tk.Label(self.register_frame, text='Password')
        self.search = tk.Label(self.search_frame, text='Recipe Name')
        self.search_entry = tk.Entry(self.search_frame, borderwidth = 2)
        self.text = tk.Text(self.text_frame, width=65, height=12, font="Courier 12", wrap="word")
        
        self.v_scrollbar = tk.Scrollbar(self.text_frame, command=self.text.yview)
        self.v_scrollbar.pack(side='right', fill='y')
        self.text.config(yscrollcommand=self.v_scrollbar.set)
        
        self.enter = tk.Button(self.search_frame, text='Search', command=self.search_recipe)
        self.login_entry = tk.Entry(self.register_frame, borderwidth = 2)
        self.password_entry = tk.Entry(self.register_frame, borderwidth = 2)#command=self.password_encryption
        self.login_in = tk.Button(self.register_frame,text='sign in', borderwidth = 2, relief='raised', command=self.sign_in)

        # Setting listbox area with a scroll bar
        self.listbox = tk.Listbox(self.listbox_frame, width=65, height= 5)
        self.fav_listbox = tk.Listbox(self.listbox_frame, width=20, height= 5)
        self.v_scrollbar = tk.Scrollbar(self.listbox_frame, command=self.listbox.yview)
        self.v_scrollbar.pack(side='right', fill='y')
        self.listbox.config(yscrollcommand=self.v_scrollbar.set)
        
        
        # create buttons
        self.add_frecipe = tk.Button(self.add_recipe_frame, text = 'Add File Recipe',command=self.addRecipe)#command=self.addRecipe
        self.add_recipe = tk.Button(self.add_recipe_frame, text = 'Add Typed Recipe',command=self.addRecipe2)
        self.clear = tk.Button(self.add_recipe_frame, text = 'clear',command=self.clear)
        self.add_favorite = tk.Button(self.add_recipe_frame, text = 'Add to Favorite', command=self.addfavorite)
        self.quit = tk.Button(self.edit_frame, text = 'Quit', command=self.main_window.destroy, background="#ffeed6")
        # self.edit_entry= tk.Entry(self.edit_frame, borderwidth = 2 , width=30)
        # self.edit_label = tk.Label(self.edit_frame, text = 'Edit Recipe')
        # self.submit = tk.Button(self.edit_frame, text = 'Submit Change')
        
        
        # Pack the above frames and labales and entries  so they are visibleon the GUI
        self.search_frame.pack()
        self.title.pack(side='left',padx=20)
        self.search.pack(side='left',padx=10) 
        self.search_entry.pack(side ='left')
        self.enter.pack(side='left', padx=5)
        self.register_frame.pack(padx = 5, pady= 10)
        # self.login.pack(side = 'left')
        # self.login_entry.pack(side = 'left')
        # self.password.pack(side = 'left')
        # self.password_entry.pack(side = 'left')
        # self.login_in.pack(padx=5)
        self.listbox_frame.pack()
        self.listbox.pack(side='left', padx=10, pady= 10)
        self.fav_listbox.pack(side='right')
        self.text_frame.pack()
        self.text.pack(ipadx= 5, ipady=6, padx=5, pady=10)
        
        #self.favorite_listbox.pack()
        self.add_recipe_frame.pack()
        self.add_frecipe.pack(side='left',padx=5, pady= 5)
        self.add_recipe.pack(side='left',padx=5, pady= 5)
        self.clear.pack(side='left',padx=5, pady= 5)
        self.add_favorite.pack(padx=5,pady= 5)
        self.edit_frame.pack(padx=5, pady=5)
        # self.edit_label.pack()
        # self.edit_entry.pack()
        # self.submit.pack(pady=10)
        self.quit.pack(ipadx= 5)
        self.emptyset = []
        self.emptyset_recipe = set()
        tk.mainloop()
        
    #clear all entries     
    def clear(self):
        self.search_entry.delete(0, tk.END)
        self.listbox.delete(0,tk.END)
        self.text.delete(1.0,tk.END)
        self.fav_listbox.delete(0,tk.END)
        
   # Add recipe from local .txt file to the list    
    def addRecipe(self):
        filepath = fd.askopenfilename()
        try:
            file = open(filepath, 'r')
            file_content = file.read()
            
        except FileNotFoundError:
            print(f"The file '{filepath}' was not found.")
            for line in range(len(file_content)):
               
                file_content[line]=file_content[line].rstrip('\n')
        self.listbox.delete(0, tk.END)        
               
        self.text.insert(tk.END, f'{file_content}')
        file.close()
      # login in to an account 
    def sign_in(self):
       self.credentials = {'admin': 'mis310'}
       login = self.login_entry.get()
       password = self.password_entry.get()  
       if login in self.credentials and self.credentials[login] == password:
           messagebox.showinfo('Login', 'Login Sucessfully')
       else:
           messagebox.showerror('Login', 'Invalid login  or password')
       self.login_entry.delete(0, tk.END)
       self.password_entry.delete(0, tk.END)
    # Search a recipe in the recipe data base dictionary
    def search_recipe(self):
        
        food = {'lasagna':'1-Start by making the sauce with ground beef,bell peppers,' 
                 +'onions, and a combo of tomato sauce, tomato paste, and crushed tomatoes.'
                 +'The three kinds of tomatoes gives the sauce great depth of flavor.'
                 +'2-Let this simmer you boil the noodles and get the cheeses ready',
                 # +'We are using ricotta, shredded mozzarella, and parmesan like the mix of tomatoes,'
                 # +'this 3-cheese blend gives the lasagna great flavor'
                 # +'3-From there, its just an assembly job. A cup of meat sauce,'
                 # +'a layer of noodles, more sauce, followed by a layer of cheese.'
                 # +'Repeat until you have three layers and have used up all the ingredients.'
                 # +'4-Bake until bubbly and you are ready to eat!',
                     
                 'pizza':
 
                 '- Mix the bread flour and khorasan flour together in a bowl.'+ 
                 'Pour the water into a separate bowl and add the starter to the water.'+
                 'Mix with your hand to dissolve the starter before adding 10% of the flour mix.'+
                 'Mix with your hand till there are no dry bits. Cover, and rest for 10 minutes.'+
 
                 '- Add the salt to the mix and knead briefly to incorporate before adding the remaining'+
                 'flour and bringing together into a dough with your hands.'+
 
                 '- Tip the dough onto a clean work surface and knead for around 10 minutes.'+
                 ' Form into a tight ball, cover and leave for 2 hours.'+
 
                 '- When the time is up, divide the dough into 250g (8.8 oz) pieces and shape into dough balls.'
                 ' Place the dough balls into a container and cover.'+
 
                 '- Refrigerate for 24 hours. Allow the dough balls to sit at room temperature'+
                 'for at least 2 hours before opening into pizzas.',
                 
                 'spaghetti bolognese': 'Ingredients & Variation'+
                 'Vegetables: A mirepoix is a mixture of onions, carrots, and celery and is traditional in a bolognese.'+
                 ' If you’d like other veggies, chop them finely and add them in.'

                 'Meat: A combination of ground pork and beef adds great flavor,'+ 
                 'but this recipe works with just beef or the addition of ground veal.'

                 'Tomatoes: Canned whole tomatoes have a bit of a thicker consistency than diced tomatoes'+
                 'so I prefer them in this recipe. San Marzano tomatoes are the best choice for flavor.'+ 
                 'If you only have canned diced tomatoes, those will work too (as will crushed tomatoes) but they may change the consistency slightly.'+

                  'Wine: A dry red is great (but any red will do). I usually use a cabernet or merlot. Wine adds a lot of depth to this sauce (and the alcohol evaporates).'+
                  'If you cannot use wine, you can use a bit of beef broth but it will alter the flavor slightly.',    
                
                    'chicken alfredo':'    Boil the noodles: Cook the Fettuccine al dente, according to package instructions.'
                'Cook the chicken: Season the chicken, then pan-fry in oil and butter, for 6 minutes a side, or until an internal temperature reaches 165 degrees F. Transfer to a cutting board and let rest for a few minutes, then cut into 1/2-inch thick slices. Tent with foil, while you prepare the sauce.'+
                'Make the Alfredo sauce: Using the same pan you used to cook the chicken, the cream, butter, and seasonings are incorporated and simmered on medium-low heat until thickened, then the Parmesan is added in until melted and smooth.'+
                'Assemble: Drain the pasta, reserving some of the liquid to loosen the sauce (only if necessary.) Toss immediately with the Alfredo sauce. Divide the pasta among serving bowls and top with a few slices of cooked chicken. Garnish with parsley, more Parmesan, and black pepper if desired.',    
                 'vegetable curry': '2 tablespoons vegetable oil'+

                '1 pound beef sirloin, cut into 2-inch strips'+
                
                '1 ½ cups fresh broccoli florets'+
                
                '1 red bell pepper, cut into matchsticks'+
                
                '2 carrots, thinly sliced'+
                
                '1 green onion, chopped'+
                
                '1 teaspoon minced garlic'+
                
                '2 tablespoons soy sauce'+
                
                '2 tablespoons sesame seeds, toasted'
    
                        }
        if self.search_entry.get() == '':
             tk.messagebox.showinfo('Attention!','Field  need an Input')
        else:
            search_input = self.search_entry.get()
            search_inputs = search_input.lower()
           
          
            if search_inputs in food:  
                result = food.get(search_inputs,"Entry not found")
                self.text.delete(1.0, tk.END)
                search_inputs = search_input.capitalize()
                self.listbox.insert(tk.END,f" {search_inputs}") 
                self.text.insert(tk.END,f' {search_inputs} Recipe Description: \n ----------------------\n{result}')   
                
            else:
                
                tk.messagebox.showinfo('Response', f'Sorry {search_input} is not created yet, do you want to create it?')
                self.search_entry.delete(0, tk.END)
                self.text.delete(1.0, tk.END)


           # This function is adding the recipe name to our favorite list. 
    def addfavorite(self):
         search_input = self.search_entry.get()
         search_inputs = search_input.capitalize()
         selection = self.listbox.curselection()
         if selection:
             selected_value = self.listbox.get(selection[0])             
            #  self.fav_listbox.insert(tk.END, f"{selected_value}")
            #  tk.messagebox.showinfo ('Response',search_inputs +' is added to you favorite list')
         # for i in self.listbox.curselection():
         #     self.listbox.get(i)
             fav = open('fav_list.txt','a')
             fav.write(f'{selected_value}')
             fav = open('fav_list.txt','r')
             fav = fav.readlines()
             if selected_value in fav:
                 tk.messagebox.showwarning('Response',selected_value +' already on your favorite list')
             else:
                my_list = open('fav_list.txt','r')
                dish = my_list.readlines()
                for line in dish:
                    my_dish = f'{dish}\n'
                    # dish = f'{dish[line]}\n'
                    print(f"{my_dish}\n")
                self.fav_listbox.insert(tk.END, f"{my_dish}\n")
                
                tk.messagebox.showinfo('Response',selected_value +' is added to you favorite list')
             
                 
             # self.text.delete(1.0, tk.END)
             # self.text.insert(tk.END,f'{ myfile[line]}')
             
             
             
             #tk.messagebox.showinfo ('You Favorites',favlist)
         if search_input =='' :
             tk.messagebox.showwarning ('warning','Please Enter or search what to save')
         
         
      # Type a recipe and save it in a txt file 
    def addRecipe2(self):
        # filename = 'mesplat.pkl'

        # if os.path.exists(filename):
        #     with open(filename,'rb') as f:
        #         plat = pickle.load(f)
        # else:
        #     plat ={}
        # while True:
        #     addrecipe =input('add yes/no?\n')
        #     if addrecipe == 'yes':
        #         recipee_name = input('Recipe name')
        #         recipee_desc = input('Recipe description')
        #         plat[recipee_name]=recipee_desc
        #     else:
        #         break
        # with open(filename,'wb')as f:
        #     pickle.dump(plat,f)
            
        # print(plat)
        
        if self.text.get("1.0",'end-1c')== '':
            
            tk.messagebox.showwarning('Warning','Text box is empty, enter Recipe')
        else:
            text = self.text.get("1.0")
            print(text)
            saved_file = open('dish_list.txt','a')
            saved_file.write(text+'\n')
            read_file = open('dish_list.txt','r')
            print(read_file.readline()+ '\n') 
            saved_file.close()
    
      

if __name__=='__main__': 
    recipe = Recipe()
