from tkinter import*
import requests
import json

coin = Tk()
coin.overrideredirect(False)

coin.title("News Widget")
coin.geometry("500x500")
coin.configure(background="orange")

l1 = Label(coin,text="BBC News Update",font=("Helvetica",15,"bold"),bg="Orange")
l1.place(relx=0.5,rely=0.1,anchor=CENTER)


#Setting labels
city_name_label=Label(coin,text="Country Name",font=("Helvetica",18,'bold'),bg="orange")
city_name_label.place(relx=0.31,rely=15,anchor=NE)

label=Label(coin,text="Region",font=("Helvetica",18,'bold'),bg="orange")
label.place(relx=0.3,rely=16,anchor=NE)

label1=Label(coin,text="Language",font=("Helvetica",18,'bold'),bg="orange")
label1.place(relx=0.3,rely=16,anchor=NE)

label2=Label(coin,text="Population",font=("Helvetica",18,'bold'),bg="orange")
label2.place(relx=0.3,rely=16,anchor=NE)

label3=Label(coin,text="Area",font=("Helvetica",18,'bold'),bg="orange")
label3.place(relx=0.3,rely=16,anchor=NE)

#Finish
name_label = Label(coin,bg="white",font=("bold",10))
name_label.place(relx=0.31,rely=0.38,anchor=NE)
 
region1_label = Label(coin,bg="white",font=("bold",10))
region1_label.place(relx=0.31,rely=0.48,anchor=NE)

lan1_label = Label(coin,bg="white",font=("bold",10))
lan1_label.place(relx=0.31,rely=0.58,anchor=NE)

po1_label = Label(coin,bg="white",font=("bold",10))
po1_label.place(relx=0.31,rely=0.68,anchor=NE)

ar1_label = Label(coin,bg="white",font=("bold",10))
ar1_label.place(relx=0.31,rely=0.78,anchor=NE)
#humidity_info_label = Label(coin,bg="white",font=("bold",10))
#humidity_info_label.place(relx=0.5,rely=0.5,anchor=CENTER)

#main function
def city_d():
    api_request = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=037f11d959bf457db676af590fbb4ebe")
    
    api_output_json = json.loads(api_request.content)
    
    name_info=api_output_json["articles"][0]['title']
    print(name_info)
    
    region = api_output_json["articles"][1]['title']
    print(region)
    
    lang = api_output_json["articles"][2]['title']
    print(lang)
    
    popu = api_output_json["articles"][3]['title']
    print(popu)
    
    are = api_output_json["articles"][4]['title']
    print(are)
    
    name_label["text"]= "name:" + str(name_info)
    region1_label["text"]="Region:" + str(region)
    lan1_label["text"]="Language:" + str(lang)
    po1_label["text"]="Population:" + str(popu)
    ar1_label["text"]="Area:" + str(are)
    
    city_name_label["text"]
    label["text"] 
    label1["text"] 
    label2["text"] 
    label3["text"] 
    
search_btn = Button(coin,text="City Details",bg="yellow",command=city_d,relief=FLAT)
search_btn.place(relx=0.20,rely=0.9,anchor=NE)
coin.mainloop()