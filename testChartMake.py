import ChartMake
chart = ChartMake.new_chart()
ChartMake.set_title(chart, "Wild Parrot Deaths per Year")
ChartMake.set_x_axis(chart,
                   ["2009", "2010", "2011", "2012", "2013",
                    "2014", "2015"])
ChartMake.set_y_axis(chart, minimum=0, maximum=700,
                   labels=[0, 100, 200, 300, 400, 500, 600, 700])
ChartMake.set_series(chart, [250, 270, 510, 420, 680, 580, 450])
ChartMake.set_series_type(chart, "bar")
ChartMake.generate_chart(chart, "chart.png")
