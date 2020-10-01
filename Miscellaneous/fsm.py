class SM:
	def start(self):
		self.state = self.start_state # set state as start_state

	def step(self, input):
		(state, output) = self.get_next_values(self.state, input)
		self.state = state
		return output

	def transduce(self, inputs):
		self.start()
		outputs = []
		for input_value in inputs:
			output = self.step(input_value)
			if (self.done(self.state)):
				break
			else:
				outputs.append(output)

		return outputs

	def done(self, state):
		pass


class Cascade(SM):
	def __init__(self, sm1, sm2):
		self.start_state = (sm1.start_state, sm2.start_state) 
		self.sm1 = sm1
		self.sm2 = sm2

	def get_next_values(self, state, inp):
		(newstate1, output1) = self.sm1.get_next_values(state[0],inp) 
		(newstate2, output2) = self.sm2.get_next_values(state[1],output1) 
		return ((newstate1,newstate2), output2)




class Parallel(SM):
	def __init__(self, sm1, sm2):
		self.m1 = sm1
		self.m2 = sm2
		self.start_state = (sm1.start_state, sm2.start_state)

	# single input, many output
	def get_next_values(self, state, inp): 
		(s1, s2) = state
		(newS1, o1) = self.m1.get_next_values(s1, inp) 
		(newS2, o2) = self.m2.get_next_values(s2, inp) 
		return ((newS1, newS2), (o1, o2))


class Feedback (SM): 
	def __init__(self, sm):
		self.m = sm
		self.start_state = self.m.start_state

	def get_next_values(self, state, inp):
		#no input used
		(ignore, o) = self.m.get_next_values(state, 'undefined') 
		(newS, ignore) = self.m.get_next_values(state, o) 
		return (newS, o)

