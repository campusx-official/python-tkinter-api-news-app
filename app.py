from tkinter import *
import requests
# pip install requests
from PIL import Image,ImageTk
from urllib.request import urlopen
import io

class News:

	def __init__(self):

		self.root=Tk()

		self.root.title("News Application")
		self.root.minsize(500,600)
		self.root.maxsize(500,600)

		self.root.configure(background="#fff")

		self.label=Label(self.root, text="Apnanewz 24*7",bg="#fff")
		self.label.configure(font=("Times",30,"bold"))
		self.label.pack(pady=(30,30))

		self.label1=Label(self.root,text="Enter the topic", bg="#fff")
		self.label1.configure(font=("Times",15,"italic"))
		self.label1.pack(pady=(10,20))

		self.topic=Entry(self.root)
		self.topic.pack(pady=(5,10),ipadx=30,ipady=3)

		self.click=Button(self.root, text="Search",bg="#000",fg="#fff", command=lambda: self.fetch())
		self.click.pack(pady=(5,10))

		self.root.mainloop()

	def fetch(self):
		# fetch the search term
		term=self.topic.get()

		url="https://newsapi.org/v2/everything?q={}&apiKey=15bcbe3f5e854f0ebf1058c526a52932".format(term)

		# hit the api
		response=requests.get(url)
		self.response=response.json()
		#print(self.response)
		self.data=self.response['articles']
		self.extract()


	def extract(self,index=0):

		news=[]

		news.append(self.data[index]['title'])
		news.append(self.data[index]['source']['name'])
		news.append(self.data[index]['description'])
		news.append(self.data[index]['urlToImage'])

		self.clear()
		self.display(news,index=index)


	def display(self, news, index):

		my_page = urlopen(news[3])

		my_picture = io.BytesIO(my_page.read())
		# use PIL to open image formats like .jpg  .png  .gif  etc.
		pil_img = Image.open(my_picture)
		# convert to an image Tkinter can use
		tk_img = ImageTk.PhotoImage(pil_img)
		# put the image on a typical widget
		label = Label(self.root, image=tk_img)
		label.pack(padx=5, pady=5)

		#imageUrl = "https://techcrunch.com/wp-content/uploads/2020/06/GettyImages-1193112376.jpg?w=600"

		#load = Image.open(imageUrl)
		#load = load.resize((200, 200), Image.ANTIALIAS)
		#render = ImageTk.PhotoImage(load)

		#img = Label(image=render)
		#img.image = render
		#img.pack()

		title=Label(self.root,text=news[0],fg="#000",bg="#fff")
		title.pack()

		source=Label(self.root,text=news[1],fg="#000",bg="#fff")
		source.pack()

		desc=Label(self.root,text=news[2],fg="#000",bg="#fff")
		desc.pack()

		frame=Frame(self.root)
		frame.pack()

		if index!=0:
			previous=Button(frame, text="Previous",command=lambda: self.extract(index=index-1))
			previous.pack(side="left")

		if index!=19:
			next=Button(frame, text="Next",command=lambda: self.extract(index=index+1))
			next.pack(side="right")



	def clear(self):

		for i in self.root.pack_slaves():
			i.destroy()




obj=News()

