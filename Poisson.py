import math
import matplotlib.pyplot as plt



class Poisson(Distribution):

	def calculate_mean(self):

			
		avg = 1.0 * sum(self.data) / len(self.data)

		self.mean = avg

		return self.mean

	def Poisson(self,act_success,alpha=0,z=0):

		alpha=2.71828**(-self.mean)*(self.mean**act_success)

		z=math.factorial(act_success)

		Poisson_probab=alpha/z

		return Poisson_probab
