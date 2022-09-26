import re

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget


Window.size = (400, 600)


class MainWidget(Widget):
	def clear(self):
		self.ids.input_box.text = '0'

	def button_value(self, number):
		prev_num = self.ids.input_box.text

		if 'Math Error' in prev_num:
			prev_num = ''

		if prev_num == '0':
			self.ids.input_box.text = ''
			self.ids.input_box.text = f"{number}"
		else:
			self.ids.input_box.text = f"{prev_num}{number}"

	def signs(self, sign):
		prev_num = self.ids.input_box.text
		self.ids.input_box.text = f"{prev_num}{sign}"

	def remove_last_num(self):
		prev_num = self.ids.input_box.text
		prev_num = prev_num[:-1]

		self.ids.input_box.text = prev_num

	def dots(self, dot):
		prev_num = self.ids.input_box.text
		num_list = re.split("\+|\*|-|/|%", prev_num)

		if '.' not in num_list:
			self.ids.input_box.text = f"{prev_num}{dot}"

	def pos_neg(self):
		prev_num = self.ids.input_box.text

		if '-' in prev_num:
			self.ids.input_box.text = f"{prev_num.replace('-','')}"
		else:
			self.ids.input_box.text = f"-{prev_num}"

	def result(self):
		prev_num = self.ids.input_box.text
		try:
			result = eval(prev_num)
			self.ids.input_box.text = str(result)

		except:
			self.ids.input_box.text = 'Math Error'


class BasicCalApp(App):
	pass


BasicCalApp().run()
