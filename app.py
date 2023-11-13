from flask import Flask, render_template
from flask import request
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
 

app = Flask(__name__)

@app.route('/')
def index():
    # Data1
    data1 = {
        'Year': [2015, 2022] * 7,  # Example years
        'Country': ['Sub-Saharan', 'Central Asia', 'Eastern Asia', 'North Africa', 'Latin America', 'Europe and NA', 'Oceania'] * 2,
        'Percentage': [39, 88, 97, 93, 97, 100, 36, 50, 99, 98, 94, 98, 100, 38]  # Example percentages for two years
    }
    df1 = pd.DataFrame(data1)

    # Define colors for each year, you can customize this list as needed
    colors = {
    2015: '#FF1C53',  # Color for year 2015
    2022: '#A41034'  # Color for year 2022
    }


    # Create a figure with a slider
    fig1 = go.Figure()

    for year in df1['Year'].unique():
        filtered_df = df1[df1['Year'] == year]
        fig1.add_trace(
            go.Bar(
                x=filtered_df['Country'],
                y=filtered_df['Percentage'],
                name=str(year),
                marker_color=colors[year]  # Assign color to each bar trace
            )
        )

    # Create slider
    steps1 = []
    for i, year in enumerate(df1['Year'].unique()):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(df1['Year'].unique())}, {"title": f"Sample Bar Chart: {year}"}],
            label=str(year)
        )
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps1.append(step)

        sliders1 = [dict(
        active=10,
        currentvalue={"prefix": "Year: "},
        pad={"t": 50},
        steps=steps1
    )]

    fig1.update_layout(
        sliders=sliders1
    )


    # Data2
    data2 = {
        'Year': [2015, 2022] * 7,  # Example years
        'Country': ['Sub-Saharan', 'Central Asia', 'Eastern Asia', 'North Africa', 'Latin America', 'Europe and NA', 'Oceania'] * 2,
        'Percentage': [12.7, 2.5, 15.7, 11.7, 13.4, 47.5, 58.7, 12.8, 2.9, 19.9, 11.2, 11.8, 49.5, 76.8]  # Example percentages for two years
    }
    df2 = pd.DataFrame(data2)

    # Define colors for each year, you can customize this list as needed
    colors = {
    2015: '#FF903A',  # Color for year 2015
    2022: '#AE6329'  # Color for year 2022
    }


    # Create a figure with a slider
    fig2 = go.Figure()

    for year in df2['Year'].unique():
        filtered_df = df2[df2['Year'] == year]
        fig2.add_trace(
            go.Bar(
                x=filtered_df['Country'],
                y=filtered_df['Percentage'],
                name=str(year),
                marker_color=colors[year]  # Assign color to each bar trace
            )
        )

    # Create slider
    steps2 = []
    for i, year in enumerate(df2['Year'].unique()):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(df2['Year'].unique())}, {"title": f"Sample Bar Chart: {year}"}],
            label=str(year)
        )
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps2.append(step)

        sliders2 = [dict(
        active=10,
        currentvalue={"prefix": "Year: "},
        pad={"t": 50},
        steps=steps2
    )]

    fig2.update_layout(
        sliders=sliders2
    )

    # Data3
    data3 = {
        'Year': [2015, 2022] * 7,  # Example years
        'Country': ['Sub-Saharan', 'Central Asia', 'Eastern Asia', 'North Africa', 'Latin America', 'Europe and NA', 'Oceania'] * 2,
        'Percentage': [86.6, 84.6, 57.5, 53.0, 54.5, 13.9, 77.5, 87.2, 84.8, 53.8, 55.0, 53.8, 13.2, 76.4]  # Example percentages for two years
    }
    df3 = pd.DataFrame(data3)

    # Define colors for each year, you can customize this list as needed
    colors = {
    2015: '#FED72C',  # Color for year 2015
    2022: '#C19D00'  # Color for year 2022
    }


    # Create a figure with a slider
    fig3 = go.Figure()

    for year in df3['Year'].unique():
        filtered_df = df3[df3['Year'] == year]
        fig3.add_trace(
            go.Bar(
                x=filtered_df['Country'],
                y=filtered_df['Percentage'],
                name=str(year),
                marker_color=colors[year]  # Assign color to each bar trace
            )
        )

    # Create slider
    steps3 = []
    for i, year in enumerate(df3['Year'].unique()):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(df3['Year'].unique())}, {"title": f"Sample Bar Chart: {year}"}],
            label=str(year)
        )
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps3.append(step)

        sliders3 = [dict(
        active=10,
        currentvalue={"prefix": "Year: "},
        pad={"t": 50},
        steps=steps3
    )]

    fig3.update_layout(
        sliders=sliders3
    )

    # Data4
    data4 = {
        'Year': [2015, 2022] * 7,  # Example years
        'Country': ['Sub-Saharan', 'Central Asia', 'Eastern Asia', 'North Africa', 'Latin America', 'Europe and NA', 'Oceania'] * 2,
        'Percentage': [155.3, 97.4, 123.3, 137.0, 116.0, 113.1, 122.8, 115.3, 127, 123.3, 137.0, 116.0, 113.1, 122.8]  # Example percentages for two years
    }
    df4 = pd.DataFrame(data4)

    # Define colors for each year, you can customize this list as needed
    colors = {
    2015: '#1DC56E',  # Color for year 2015
    2022: '#016833'  # Color for year 2022
    }


    # Create a figure with a slider
    fig4 = go.Figure()

    for year in df4['Year'].unique():
        filtered_df = df4[df4['Year'] == year]
        fig4.add_trace(
            go.Bar(
                x=filtered_df['Country'],
                y=filtered_df['Percentage'],
                name=str(year),
                marker_color=colors[year]  # Assign color to each bar trace
            )
        )

    # Create slider
    steps4 = []
    for i, year in enumerate(df4['Year'].unique()):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(df4['Year'].unique())}, {"title": f"Sample Bar Chart: {year}"}],
            label=str(year)
        )
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps4.append(step)

        sliders4 = [dict(
        active=10,
        currentvalue={"prefix": "Year: "},
        pad={"t": 50},
        steps=steps4
    )]

    fig4.update_layout(
        sliders=sliders4
    )

    # Data5
    data5 = {
        'Year': [2015, 2022] * 7,  # Example years
        'Country': ['Sub-Saharan', 'Central Asia', 'Eastern Asia', 'North Africa', 'Latin America', 'Europe and NA', 'Oceania'] * 2,
        'Percentage': [59, 78, 95, 90, 95, 99, 85, 70, 89, 78, 94, 96, 99, 85]  # Example percentages for two years
    }
    df5 = pd.DataFrame(data5)

    # Define colors for each year, you can customize this list as needed
    colors = {
    2015: '#1CA2D7',  # Color for year 2015
    2022: '#006086'  # Color for year 2022
    }


    # Create a figure with a slider
    fig5 = go.Figure()

    for year in df5['Year'].unique():
        filtered_df = df5[df5['Year'] == year]
        fig5.add_trace(
            go.Bar(
                x=filtered_df['Country'],
                y=filtered_df['Percentage'],
                name=str(year),
                marker_color=colors[year]  # Assign color to each bar trace
            )
        )

    # Create slider
    steps5 = []
    for i, year in enumerate(df5['Year'].unique()):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(df5['Year'].unique())}, {"title": f"Sample Bar Chart: {year}"}],
            label=str(year)
        )
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps5.append(step)

        sliders5 = [dict(
        active=10,
        currentvalue={"prefix": "Year: "},
        pad={"t": 50},
        steps=steps5
    )]

    fig5.update_layout(
        sliders=sliders5
    )

    # Data6
    data6 = {
        'Year': [2015, 2022] * 7,  # Example years
        'Country': ['Sub-Saharan', 'Central Asia', 'Eastern Asia', 'North Africa', 'Latin America', 'Europe and NA', 'Oceania'] * 2,
        'Percentage': [3.17, 0.13, 0.14, 0.05, 0.35, 0.28, 0.50, 01.32, 0.09, 0.12, 0.07, 0.32, 0.35, 0.50]  # Example percentages for two years
    }
    df6 = pd.DataFrame(data6)

    # Define colors for each year, you can customize this list as needed
    colors = {
    2015: '#1CA2D7',  # Color for year 2015
    2022: '#006086'  # Color for year 2022
    }


    # Create a figure with a slider
    fig6 = go.Figure()

    for year in df6['Year'].unique():
        filtered_df = df6[df6['Year'] == year]
        fig6.add_trace(
            go.Bar(
                x=filtered_df['Country'],
                y=filtered_df['Percentage'],
                name=str(year),
                marker_color=colors[year]  # Assign color to each bar trace
            )
        )

    # Create slider
    steps6 = []
    for i, year in enumerate(df6['Year'].unique()):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(df6['Year'].unique())}, {"title": f"Sample Bar Chart: {year}"}],
            label=str(year)
        )
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps5.append(step)

        sliders6 = [dict(
        active=10,
        currentvalue={"prefix": "Year: "},
        pad={"t": 50},
        steps=steps6
    )]

    fig6.update_layout(
        sliders=sliders6
    )

    # Data7
    data7 = {
        'Year': [2015, 2022] * 7,  # Example years
        'Country': ['Sub-Saharan', 'Central Asia', 'Eastern Asia', 'North Africa', 'Latin America', 'Europe and NA', 'Oceania'] * 2,
        'Percentage': [2.3, 27.4, 22.8, 8.9, 23.7, 39.4, 29.4, 12.6, 83.6, 39.6, 18.0, 41.7, 152.2, 95.3]  # Example percentages for two years
    }
    df7 = pd.DataFrame(data7)

    # Define colors for each year, you can customize this list as needed
    colors = {
    2015: '#1CA2D7',  # Color for year 2015
    2022: '#006086'  # Color for year 2022
    }


    # Create a figure with a slider
    fig7 = go.Figure()

    for year in df7['Year'].unique():
        filtered_df = df7[df7['Year'] == year]
        fig7.add_trace(
            go.Bar(
                x=filtered_df['Country'],
                y=filtered_df['Percentage'],
                name=str(year),
                marker_color=colors[year]  # Assign color to each bar trace
            )
        )

    # Create slider
    steps7 = []
    for i, year in enumerate(df7['Year'].unique()):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(df7['Year'].unique())}, {"title": f"Sample Bar Chart: {year}"}],
            label=str(year)
        )
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps7.append(step)

        sliders7 = [dict(
        active=10,
        currentvalue={"prefix": "Year: "},
        pad={"t": 50},
        steps=steps6
    )]

    fig7.update_layout(
        sliders=sliders7
    )

    # Data8
    data8 = {
        'Year': [2015, 2022] * 7,  # Example years
        'Country': ['Sub-Saharan', 'Central Asia', 'Eastern Asia', 'North Africa', 'Latin America', 'Europe and NA', 'Oceania'] * 2,
        'Percentage': [0.35, 0.60, 2.05, 0.75, 0.72, 2.24, 1.83, 0.32, 0.58, 2.31, 0.90, 0.63, 2.62, 1.77]  # Example percentages for two years
    }
    df8 = pd.DataFrame(data8)

    # Define colors for each year, you can customize this list as needed
    colors = {
    2015: '#6947EB',  # Color for year 2015
    2022: '#3B2882'  # Color for year 2022
    }


    # Create a figure with a slider
    fig8 = go.Figure()

    for year in df7['Year'].unique():
        filtered_df = df8[df8['Year'] == year]
        fig8.add_trace(
            go.Bar(
                x=filtered_df['Country'],
                y=filtered_df['Percentage'],
                name=str(year),
                marker_color=colors[year]  # Assign color to each bar trace
            )
        )

    # Create slider
    steps8 = []
    for i, year in enumerate(df8['Year'].unique()):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(df8['Year'].unique())}, {"title": f"Sample Bar Chart: {year}"}],
            label=str(year)
        )
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps8.append(step)

        sliders8 = [dict(
        active=10,
        currentvalue={"prefix": "Year: "},
        pad={"t": 50},
        steps=steps8
    )]

    fig8.update_layout(
        sliders=sliders8
    )

    # Data9
    data9 = {
        'Year': [2015, 2022] * 7,  # Example years
        'Country': ['Sub-Saharan', 'Central Asia', 'Eastern Asia', 'North Africa', 'Latin America', 'Europe and NA', 'Oceania'] * 2,
        'Percentage': [23.3, 25.9, 24.8, 24.5, 33.0, 60.3, 67.4, 30.7, 33.7, 40.9, 36.1, 43.3, 90.6, 85.7]  # Example percentages for two years
    }
    df9 = pd.DataFrame(data9)

    # Define colors for each year, you can customize this list as needed
    colors = {
    2015: '#AA24CF',  # Color for year 2015
    2022: '#57116A'  # Color for year 2022
    }


    # Create a figure with a slider
    fig9 = go.Figure()

    for year in df7['Year'].unique():
        filtered_df = df9[df9['Year'] == year]
        fig9.add_trace(
            go.Bar(
                x=filtered_df['Country'],
                y=filtered_df['Percentage'],
                name=str(year),
                marker_color=colors[year]  # Assign color to each bar trace
            )
        )

    # Create slider
    steps9 = []
    for i, year in enumerate(df9['Year'].unique()):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(df9['Year'].unique())}, {"title": f"Sample Bar Chart: {year}"}],
            label=str(year)
        )
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps9.append(step)

        sliders9 = [dict(
        active=10,
        currentvalue={"prefix": "Year: "},
        pad={"t": 50},
        steps=steps9
    )]

    fig9.update_layout(
        sliders=sliders9
    )

    # Data10
    data10 = {
        'Year': [2015, 2022] * 7,  # Example years
        'Country': ['Sub-Saharan', 'Central Asia', 'Eastern Asia', 'North Africa', 'Latin America', 'Europe and NA', 'Oceania'] * 2,
        'Percentage': [40, 80, 76, 45, 86, 90, 75, 48.0, 85.4, 84.1, 51.6, 93.6, 94.2, 79.2]  # Example percentages for two years
    }
    df10 = pd.DataFrame(data10)

    # Define colors for each year, you can customize this list as needed
    colors = {
    2015: '#DF438E',  # Color for year 2015
    2022: '#79244D'  # Color for year 2022
    }


    # Create a figure with a slider
    fig10 = go.Figure()

    for year in df7['Year'].unique():
        filtered_df = df10[df10['Year'] == year]
        fig10.add_trace(
            go.Bar(
                x=filtered_df['Country'],
                y=filtered_df['Percentage'],
                name=str(year),
                marker_color=colors[year]  # Assign color to each bar trace
            )
        )

    # Create slider
    steps10 = []
    for i, year in enumerate(df10['Year'].unique()):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(df10['Year'].unique())}, {"title": f"Sample Bar Chart: {year}"}],
            label=str(year)
        )
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps10.append(step)

        sliders10 = [dict(
        active=10,
        currentvalue={"prefix": "Year: "},
        pad={"t": 50},
        steps=steps10
    )]

    fig10.update_layout(
        sliders=sliders10
    )

    # Data11
    data11 = {
        'Year': [2015, 2022] * 7,  # Example years
        'Country': ['Sub-Saharan', 'Central Asia', 'Eastern Asia', 'North Africa', 'Latin America', 'Europe and NA', 'Oceania'] * 2,
        'Percentage': [3.8, 2.9, 6.5, 10.4, 7.4, 9.0, 9.3, 3.7, 2.9, 8.0, 9.8, 8.6, 7.6, 13.9]  # Example percentages for two years
    }
    df11 = pd.DataFrame(data11)

    # Define colors for each year, you can customize this list as needed
    colors = {
    2015: '#989898',  # Color for year 2015
    2022: '#000000'  # Color for year 2022
    }


    # Create a figure with a slider
    fig11 = go.Figure()

    for year in df11['Year'].unique():
        filtered_df = df11[df11['Year'] == year]
        fig11.add_trace(
            go.Bar(
                x=filtered_df['Country'],
                y=filtered_df['Percentage'],
                name=str(year),
                marker_color=colors[year]  # Assign color to each bar trace
            )
        )

    # Create slider
    steps11 = []
    for i, year in enumerate(df11['Year'].unique()):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(df11['Year'].unique())}, {"title": f"Sample Bar Chart: {year}"}],
            label=str(year)
        )
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps11.append(step)

        sliders11 = [dict(
        active=10,
        currentvalue={"prefix": "Year: "},
        pad={"t": 50},
        steps=steps11
    )]

    fig11.update_layout(
        sliders=sliders11
    )

    # Data12
    data12 = {
        'Year': [2015, 2022] * 7,  # Example years
        'Country': ['Sub-Saharan', 'Central Asia', 'Eastern Asia', 'North Africa', 'Latin America', 'Europe and NA', 'Oceania'] * 2,
        'Percentage': [55.1, 76.4, 25.0, 11.5, 6.8, 2.6, 0.6, 56.8, 76.4, 18.3, 10.2, 5.7, 2.1, 0.7]  # Example percentages for two years
    }
    df12 = pd.DataFrame(data12)

    # Define colors for each year, you can customize this list as needed
    colors = {
    2015: '#989898',  # Color for year 2015
    2022: '#000000'  # Color for year 2022
    }


    # Create a figure with a slider
    fig12 = go.Figure()

    for year in df12['Year'].unique():
        filtered_df = df12[df12['Year'] == year]
        fig12.add_trace(
            go.Bar(
                x=filtered_df['Country'],
                y=filtered_df['Percentage'],
                name=str(year),
                marker_color=colors[year]  # Assign color to each bar trace
            )
        )

    # Create slider
    steps12 = []
    for i, year in enumerate(df12['Year'].unique()):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(df12['Year'].unique())}, {"title": f"Sample Bar Chart: {year}"}],
            label=str(year)
        )
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps12.append(step)

        sliders12 = [dict(
        active=10,
        currentvalue={"prefix": "Year: "},
        pad={"t": 50},
        steps=steps12
    )]

    fig12.update_layout(
        sliders=sliders12
    )


    # Convert the charts to HTML
    chart1_html = fig1.to_html()
    chart2_html = fig2.to_html()
    chart3_html = fig3.to_html()
    chart4_html = fig4.to_html()
    chart5_html = fig5.to_html()
    chart6_html = fig6.to_html()
    chart7_html = fig7.to_html()
    chart8_html = fig8.to_html()
    chart9_html = fig9.to_html()
    chart10_html = fig10.to_html()
    chart11_html = fig11.to_html()
    chart12_html = fig12.to_html()

    # Pass both charts to the template
    return render_template('chart_template.html', chart1_html=chart1_html, chart2_html=chart2_html, chart3_html=chart3_html, chart4_html=chart4_html, chart5_html=chart5_html, chart6_html=chart6_html, chart7_html=chart7_html, chart8_html=chart8_html, chart9_html=chart9_html, chart10_html=chart10_html, chart11_html=chart11_html, chart12_html=chart12_html)

if __name__ == '__main__':
    app.run(debug=True)
