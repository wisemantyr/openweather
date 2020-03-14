from scipy.stats import linregress

temp = 90
wind = 10

def linear_regress(x_axis, y_axis):
    (slope, intercept, rvalue, pvalue, stderr) = linregress(x_axis, y_axis)
    regress_values = x_axis * slope + intercept
    line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
    return [line_eq, rvalue**2]

linear_regress(temp, wind)