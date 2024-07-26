"""
It's time to customize your own plot. This is the fun part, you will see your plot come to life!
You're going to work on the scatter plot with world development data: GDP per capita on the x-axis (logarithmic scale), life expectancy on the y-axis. The code for this plot is available in the script.
As a first step, let's add axis labels and a title to the plot. You can do this with the xlabel(), ylabel() and title() functions, available in matplotlib.pyplot. This sub-package is already imported as plt.
"""
gdp_cap = [974.5803384, 5937.029525999999, 6223.367465, 4797.231267, 12779.37964, 34435.367439999995, 36126.4927, 29796.04834, 1391.253792, 33692.60508, 1441.284873, 3822.137084, 7446.298803, 12569.85177, 9065.800825, 10680.79282, 1217.032994, 430.0706916, 1713.778686, 2042.09524, 36319.23501, 706.016537, 1704.063724, 13171.63885, 4959.114854, 7006.580419, 986.1478792, 277.5518587, 3632.557798, 9645.06142, 1544.750112, 14619.222719999998, 8948.102923, 22833.30851, 35278.41874, 2082.4815670000003, 6025.374752000001, 6873.262326000001, 5581.180998, 5728.353514, 12154.08975, 641.3695236000001, 690.8055759, 33207.0844, 30470.0167, 13206.48452, 752.7497265, 32170.37442, 1327.60891, 27538.41188, 5186.050003, 942.6542111, 579.2317429999999, 1201.637154, 3548.3308460000003, 39724.97867, 18008.94444, 36180.78919, 2452.210407, 3540.651564, 11605.71449, 4471.061906, 40675.99635, 25523.2771, 28569.7197, 7320.880262000001, 31656.06806, 4519.461171, 1463.249282, 1593.06548, 23348.139730000003, 47306.98978, 10461.05868, 1569.331442, 414.5073415, 12057.49928, 1044.770126, 759.3499101, 12451.6558, 1042.581557, 1803.151496, 10956.99112, 11977.57496, 3095.7722710000003, 9253.896111, 3820.17523, 823.6856205, 944.0, 4811.060429, 1091.359778, 36797.93332, 25185.00911, 2749.320965, 619.6768923999999, 2013.977305, 49357.19017, 22316.19287, 2605.94758, 9809.185636, 4172.838464, 7408.905561, 3190.481016, 15389.924680000002, 20509.64777, 19328.70901, 7670.122558, 10808.47561, 863.0884639000001, 1598.435089, 21654.83194, 1712.472136, 9786.534714, 862.5407561000001, 47143.17964, 18678.31435, 25768.25759, 926.1410683, 9269.657808, 28821.0637, 3970.095407, 2602.394995, 4513.480643, 33859.74835, 37506.41907, 4184.548089, 28718.27684, 1107.482182, 7458.396326999999, 882.9699437999999, 18008.50924, 7092.923025, 8458.276384, 1056.380121, 33203.26128, 42951.65309, 10611.46299, 11415.80569, 2441.576404, 3025.349798, 2280.769906, 1271.211593, 469.70929810000007]
life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829, 75.635, 64.062, 79.441, 56.728, 65.554, 74.852, 50.728, 72.39, 73.005, 52.295, 49.58, 59.723, 50.43, 80.653, 44.74100000000001, 50.651, 78.553, 72.961, 72.889, 65.152, 46.462, 55.322, 78.782, 48.328, 75.748, 78.273, 76.486, 78.332, 54.791, 72.235, 74.994, 71.33800000000001, 71.878, 51.57899999999999, 58.04, 52.947, 79.313, 80.657, 56.735, 59.448, 79.406, 60.022, 79.483, 70.259, 56.007, 46.388000000000005, 60.916, 70.19800000000001, 82.208, 73.33800000000001, 81.757, 64.69800000000001, 70.65, 70.964, 59.545, 78.885, 80.745, 80.546, 72.567, 82.603, 72.535, 54.11, 67.297, 78.623, 77.58800000000001, 71.993, 42.592, 45.678, 73.952, 59.443000000000005, 48.303, 74.241, 54.467, 64.164, 72.801, 76.195, 66.803, 74.543, 71.164, 42.082, 62.069, 52.906000000000006, 63.785, 79.762, 80.204, 72.899, 56.867, 46.859, 80.196, 75.64, 65.483, 75.53699999999999, 71.752, 71.421, 71.688, 75.563, 78.098, 78.74600000000001, 76.442, 72.476, 46.242, 65.528, 72.777, 63.062, 74.002, 42.568000000000005, 79.972, 74.663, 77.926, 48.159, 49.339, 80.941, 72.396, 58.556, 39.613, 80.884, 81.70100000000001, 74.143, 78.4, 52.517, 70.616, 58.42, 69.819, 73.923, 71.777, 51.542, 79.425, 78.242, 76.384, 73.747, 74.249, 73.422, 62.698, 42.38399999999999, 43.487]
import matplotlib.pyplot as plt
# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')
# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'
# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)
# Add title
plt.title(title)
# After customizing, display the plot
plt.show()

"""
Demonstrated how you could control the y-ticks by specifying two arguments:
plt.yticks([0,1,2], ["one","two","three"])
In this example, the ticks corresponding to the numbers 0, 1 and 2 will be replaced by one, two and three, respectively.
Let's do a similar thing for the x-axis of your world development chart, with the xticks() function. The tick values 1000, 10000 and 100000 should be replaced by 1k, 10k and 100k. To this end, two lists have already been created for you: tick_val and tick_lab.
"""
plt.clf()
# Scatter plot
plt.scatter(gdp_cap, life_exp)
# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']
# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)
# After customizing, display the plot
plt.show()

"""
Right now, the scatter plot is just a cloud of blue dots, indistinguishable from each other. Let's change this. Wouldn't it be nice if the size of the dots corresponds to the population?
To accomplish this, there is a list pop loaded in your workspace. It contains population numbers for each country expressed in millions. You can see that this list is added to the scatter method, as the argument s, for size.
"""
pop = [31.889923, 3.600523, 33.333216, 12.420476, 40.301927, 20.434176, 8.199783, 0.708573, 150.448339, 10.392226, 8.078314, 9.119152, 4.552198, 1.639131, 190.010647, 7.322858, 14.326203, 8.390505, 14.131858, 17.696293, 33.390141, 4.369038, 10.238807, 16.284741, 1318.683096, 44.22755, 0.71096, 64.606759, 3.80061, 4.133884, 18.013409, 4.493312, 11.416987, 10.228744, 5.46812, 0.496374, 9.319622, 13.75568, 80.264543, 6.939688, 0.551201, 4.906585, 76.511887, 5.23846, 61.083916, 1.454867, 1.688359, 82.400996, 22.873338, 10.70629, 12.572928, 9.947814, 1.472041, 8.502814, 7.483763, 6.980412, 9.956108, 0.301931, 1110.396331, 223.547, 69.45357, 27.499638, 4.109086, 6.426679, 58.147733, 2.780132, 127.467972, 6.053193, 35.610177, 23.301725, 49.04479, 2.505559, 3.921278, 2.012649, 3.193942, 6.036914, 19.167654, 13.327079, 24.821286, 12.031795, 3.270065, 1.250882, 108.700891, 2.874127, 0.684736, 33.757175, 19.951656, 47.76198, 2.05508, 28.90179, 16.570613, 4.115771, 5.675356, 12.894865, 135.031164, 4.627926, 3.204897, 169.270617, 3.242173, 6.667147, 28.674757, 91.077287, 38.518241, 10.642836, 3.942491, 0.798094, 22.276056, 8.860588, 0.199579, 27.601038, 12.267493, 10.150265, 6.144562, 4.553009, 5.447502, 2.009245, 9.118773, 43.997828, 40.448191, 20.378239, 42.292929, 1.133066, 9.031088, 7.554661, 19.314747, 23.174294, 38.13964, 65.068149, 5.701579, 1.056608, 10.276158, 71.158647, 29.170398, 60.776238, 301.139947, 3.447496, 26.084662, 85.262356, 4.018332, 22.211743, 11.746035, 12.311143]
# Import numpy as np
import numpy as np
# Store pop as a numpy array: np_pop
np_pop = np.array(pop)
# Double np_pop
np_pop = np_pop * 2
# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)
# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
# Display the plot
plt.show()

"""
The next step is making the plot more colorful! To do this, a list col has been created for you. It's a list with a color for each corresponding country, depending on the continent the country is part of.
How did we make the list col you ask? The Gapminder data contains a list continent with the continent each country belongs to. A dictionary is constructed that maps continents onto colors:
dict = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}
"""

"""
# cont = ['Asia', 'Europe', 'Africa', 'Africa', 'Americas', 'Oceania', 'Europe', 'Asia', 'Asia', 'Europe', 'Africa', 'Americas', 'Europe', 'Africa', 'Americas', 'Europe', 'Africa', 'Africa', 'Asia', 'Africa', 'Americas', 'Africa', 'Africa', 'Americas', 'Asia', 'Americas', 'Africa', 'Africa', 'Africa', 'Americas', 'Africa', 'Europe', 'Americas', 'Europe', 'Europe', 'Africa', 'Americas', 'Americas', 'Africa', 'Americas', 'Africa', 'Africa', 'Africa', 'Europe', 'Europe', 'Africa', 'Africa', 'Europe', 'Africa', 'Europe', 'Americas', 'Africa', 'Africa', 'Americas', 'Americas', 'Asia', 'Europe', 'Europe', 'Asia', 'Asia', 'Asia', 'Asia', 'Europe', 'Asia', 'Europe', 'Americas', 'Asia', 'Asia', 'Africa', 'Asia', 'Asia', 'Asia', 'Asia', 'Africa', 'Africa', 'Africa', 'Africa', 'Africa', 'Asia', 'Africa', 'Africa', 'Africa', 'Americas', 'Asia', 'Europe', 'Africa', 'Africa', 'Asia', 'Africa', 'Asia', 'Europe', 'Oceania', 'Americas', 'Africa', 'Africa', 'Europe', 'Asia', 'Asia', 'Americas', 'Americas', 'Americas', 'Asia', 'Europe', 'Europe', 'Americas', 'Africa', 'Europe', 'Africa', 'Africa', 'Asia', 'Africa', 'Europe', 'Africa', 'Asia', 'Europe', 'Europe', 'Africa', 'Africa', 'Europe', 'Asia', 'Africa', 'Africa', 'Europe', 'Europe', 'Asia', 'Asia', 'Africa', 'Asia', 'Africa', 'Americas', 'Africa', 'Europe', 'Africa', 'Europe', 'Americas', 'Americas', 'Americas', 'Asia', 'Asia', 'Asia', 'Africa', 'Africa']
# dict = {
#     'Asia':'red',
#     'Europe':'green',
#     'Africa':'blue',
#     'Americas':'yellow',
#     'Oceania':'black'
# }
"""


# # Specify c and alpha inside plt.scatter()
# plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)
# # Previous customizations
# plt.xscale('log')
# plt.xlabel('GDP per Capita [in USD]')
# plt.ylabel('Life Expectancy [in years]')
# plt.title('World Development in 2007')
# plt.xticks([1000,10000,100000], ['1k','10k','100k'])
#
# # Show the plot
# plt.show()

"""
In above program the color is  not wroking. as we domnt know how to color countries as per continent and update it to list. we will learn this later.
"""

"""
ADDITIONAL CUSTOMIZATIONS:
If you have another look at the script, under # Additional Customizations, you'll see that there are two plt.text() functions now. They add the words "India" and "China" in the plot.
# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)
"""
# PREVIOUS CUSTOMIZATIONS <<<------------
#plt.xscale('log')
#plt.xlabel('GDP per Capita [in USD]')
#plt.ylabel('Life Expectancy [in years]')
#plt.title('World Development in 2007')
#plt.xticks([1000,10000,100000], ['1k','10k','100k'])
## Additional customizations
#plt.text(1550, 71, 'India')
#plt.text(5700, 80, 'China')
## Add grid() call
#plt.grid(True)
## Show the plot
#plt.show()