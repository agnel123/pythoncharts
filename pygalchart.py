from flask import Flask,render_template
import time
import pygal
import json
import pygal.maps.world
from pygal.style import Style

app = Flask(__name__)
 
@app.route("/")
def home():
    return "Tutsplus : Welcome to PyGal Charting Library !! "

@app.route("/bar")
def bar():
    with open('pygaldatabar.json','r') as bar_file:
        data = json.load(bar_file)
    # custom_style = Style(
    #     label_font_size	= .75em ))    
    chart = pygal.Bar(style=pygal.style.styles['default'](label_font_size=20, ))
    mark_list = [x['mark'] for x in data]
    chart.add('Annual Mark List',mark_list)
    chart.x_labels = [x['year'] for x in data]    
    chart.render_to_file('static/images/bar_chart.svg')
    img_url = 'static/images/bar_chart.svg?cache=' + str(time.time())

    with open('pygaldatamultibar.json','r') as multibar_file:
        multi_data = json.load(multibar_file)
    chartmutli = pygal.Bar()
    multi_mark_list = [y['mark'] for y in multi_data]
    tourn_list = [y['tournament'] for y in multi_data]
    chartmutli.add('Annual Mark List',multi_mark_list)
    chartmutli.add('Tournament Score',tourn_list)
    chartmutli.render_to_file('static/images/multi_bar_chart.svg')
    multi_img_url = 'static/images/multi_bar_chart.svg?cache=' + str(time.time())

    with open('pygaldataline.json','r') as linechart_file:
        linechart_data = json.load(linechart_file)
    linechart = pygal.Line()
    linechart_list_names = [x['broswer'] for x in linechart_data]
    linechart_list = [y['values'] for y in linechart_data]    
    for i in range(0,len(linechart_list_names)):
        linechart.add(linechart_list_names[i],linechart_list[i])
    linechart.render_to_file('static/images/line_chart.svg')
    line_img_url = 'static/images/line_chart.svg?cache=' + str(time.time())
    

    supra = pygal.maps.world.SupranationalWorld()
    supra.add('Asia', [('asia', 1)])
    supra.add('Europe', [('europe', 1)])
    supra.add('North america', [('north_america', 1)])
    supra.add('South america', [('south_america', 1)])
    supra.render_to_file('static/images/world_map.svg')
    worldmap_img_url = 'static/images/world_map.svg?cache=' + str(time.time())

    with open('pygaldatapie.json','r') as piechart_file:
        piechart_data = json.load(piechart_file)
    pie_chart = pygal.Pie()
    piechart_list_names = [x['broswer'] for x in piechart_data]
    piechart_list_value = [y['value'] for y in piechart_data]    
    pie_chart.title = 'Browser usage in February 2012 (in %)'
    for i in range(0,len(piechart_list_names)):
        pie_chart.add(piechart_list_names[i],piechart_list_value[i])
    pie_chart.render_to_file('static/images/pie_chart.svg')
    piechart_img_url = 'static/images/pie_chart.svg?cache=' + str(time.time())


    gaugechart = pygal.SolidGauge(inner_radius=0.70)
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    dollar_formatter = lambda x: '{:.10g}$'.format(x)
    with open('pygaldatagauge.json','r') as gauagechart_file:
        gauagechart_data = json.load(gauagechart_file)

    gauagechart_series = [x['series'] for x in gauagechart_data]
    gauagechart_values = [y['value'] for y in gauagechart_data]
    gauagechart_max_values = [z['max_value'] for z in gauagechart_data]
    
    for i in range(0,len(gauagechart_series)):
            gaugechart.add(gauagechart_series[i], [{'value': gauagechart_values[i], 'max_value': gauagechart_max_values[i]}],
            formatter=dollar_formatter)
    gaugechart.render_to_file('static/images/gauge_chart.svg')
    gaugechart_img_url = 'static/images/gauge_chart.svg?cache=' + str(time.time())

    return render_template('app.html',**locals())
 
if __name__ == "__main__":
    app.run()
