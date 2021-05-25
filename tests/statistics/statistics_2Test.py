import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib

def before():
	try:
		import matplotlib
		matplotlib.use("Agg")
		import matplotlib.pyplot as plt
		plt.switch_backend("Agg")
		lib.neutralizeFunction(plt.pause)
	except ImportError:
		pass

	try:
		import numpy
		numpy.seterr('raise')
	except ImportError:
		pass


def after():
	try:
		import matplotlib.pyplot as plt
		plt.switch_backend("TkAgg")
		importlib.reload(plt)
	except ImportError:
		pass

  
@t.test(0)
def correctPercentageTwoSamples(test):
	def testMethod():
		output = lib.outputOf(
			test.fileName,
			overwriteAttributes = [("__name__", "__main__")]
		)
		line = lib.getLine(output, 0)
		correctPercentage = assertlib.numberOnLine(0.27, line, deviation = 0.01)
		return correctPercentage

	test.test = testMethod
	test.description = lambda : "prints the correct percentage of deviating samples for N = 2"

  # add tests for three, five, ten and hundred samples
