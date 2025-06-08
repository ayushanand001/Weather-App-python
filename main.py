import tkinter as tk
import requests

def weather(cityname):
    response=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid=YOUR_API_KEY')
    w=response.json()['main']
    y=response.json()['coord']
    str=f"Latitude: {y['lat']}\nLongitute: {y['lon']}\nTemperature: {w['temp']}\nFeels like: {w['feels_like']}\nMaximum temperature: {w['temp_max']}\nMinimum temperature: {w['temp_min']}\nHumidity: {w['humidity']}\nPressure: {w['pressure']}\nWind Speed: {response.json()['wind']['speed']}"
    return str

#main window
window=tk.Tk()
window.geometry('350x750')
window.config(bg='#83a2e1')

#frame 1 heading
frame1=tk.Frame(window, bg='white', height='50', width='200')
frame1.pack_propagate(False) 
heading=tk.Label(frame1,text='Weather forcast', width=150, height=40, bg="white", fg="blue", font=("Arial",14))
heading.pack()
frame1.pack(pady=10)

#working area
frame2=tk.Frame(window, bg='white', height='600', width='800')
frame2.pack_propagate(False) 
frame2.pack(pady=(50,0))

#input
frame3=tk.Frame(frame2, bg='gray95', height='40', width='750')
frame3.pack_propagate(False) 
frame3.pack(pady=10)

city=tk.Label(frame3, text='Enter city: ', bg="gray90", fg="black", font=("Arial",10))
city.pack(side='left',padx=10)

var=tk.StringVar()
var.set(value=' ')
def entry_city_():
    a=city_entry.get()
    out=weather(a)
    var.set(out)

city_entry=tk.Entry(frame3, bg="gray80", fg="black", font=("Arial",10))
city_entry.pack(side='left',padx=10)
but1=tk.Button(frame2, text="show", height=2, width=6, bg="#304d87", fg="white", activebackground="gray5", activeforeground="white", command=entry_city_)
but1.pack()

#output
frame4=tk.Frame(frame2, bg='gray95', height='400', width='750')
frame4.pack_propagate(False) 
frame4.pack(pady=40)
output=tk.Label(frame4, textvariable=var, bg="gray90", fg="black", font=("papyrus",18), justify='left')
output.pack(side='left',padx=10)

window.mainloop()