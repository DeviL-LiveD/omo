# Часть 5

# Строим график


import plotly.graph_objects as go

x=['AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ',
   'BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ',
   'CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG', 'CH', 'CI', 'CJ']
fig = go.Figure(go.Bar(x=x, y=[37.04, 37.8, 45.17, 58.62, 47.89, 49.4, 26.72, 53.81, 51.59, 39.43, 46.49, 51.22, 49.01, 49.83, 50.79, 50.94, 50.62, 53.73, 46.88, 51.76, 64.0, 50.51, 38.66, 46.46, 55.21, 52.0, 27.23, 59.0, 61.0, 50.96], name='одн'))
fig.add_trace(go.Bar(x=x, y=[14.37, 16.41, 6.16, 3.16, 1.61, 1.86, 1.18, 0.97, 0.99, 3.74, 0.22, 0.98, 0.33, 2.66, 0.95, 2.19, 0.83, 1.99, 0.89, 1.01, 1.5, 3.03, 7.56, 1.01, 1.04, 1.0, 55.8, 0.0, 0.0, 0.96], name='чр'))
fig.add_trace(go.Bar(x=x, y=[1.87, 2.6, 0.61, 2.77, 4.12, 2.0, 4.54, 6.97, 1.98, 1.76, 16.01, 3.17, 0.99, 0.0, 2.54, 2.81, 0.0, 1.0, 4.46, 1.01, 0.5, 2.02, 10.08, 1.01, 2.08, 1.0, 0.89, 2.0, 2.0, 0.96], name='нф'))
fig.add_trace(go.Bar(x=x, y=[20.69, 12.16, 3.27, 1.98, 6.94, 3.6, 43.78, 6.16, 4.56, 5.73, 1.1, 2.2, 4.3, 6.64, 4.76, 6.56, 3.32, 5.47, 14.29, 3.02, 1.0, 4.04, 5.88, 4.04, 2.08, 3.0, 0.45, 2.0, 5.0, 5.77], name='чр+нф'))
fig.add_trace(go.Bar(x=x, y=[26.03, 31.02, 44.78, 33.47, 39.44, 43.14, 23.78, 32.09, 40.87, 49.34, 36.18, 42.44, 45.36, 40.86, 40.95, 37.5, 45.23, 37.81, 33.48, 43.22, 33.0, 40.4, 37.82, 47.47, 39.58, 43.0, 15.62, 37.0, 32.0, 41.35], name='парам'))


fig.update_layout(barmode='stack', xaxis={'categoryorder':'category ascending'})
fig.show()