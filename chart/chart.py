import plotly.graph_objects as go

categories = ['Conectividad Wi-Fi',#  5 = si
              'RTOS',#                5 = si
              'Lenguaje C',#          5= si
              'Costo ($)',#           3 mayor de 10, 2 entre 5 y 10, 1 menor de 5  
              'Capacidad de Memoria (MB)',# 3 mayor a 1000MB, 2 entre 100MB y 1000MB, 1 menor a 100MB
              'UART',#                cantidad
              'GPIO']#                3 mayor de 25, 2 entre 10 y 25, 1 menor a 25

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=[1,0,1,3,3,3,3],
      theta=categories,
      fill='toself', 
      name='Cypress'          #cypress
))
fig.add_trace(go.Scatterpolar(
      r=[0,0,1, 3, 3, 2,3],
      theta=categories,
      fill='toself',
      name='Raspberry Pi 3'   #raspberry
))

fig.add_trace(go.Scatterpolar(
      r=[1, 1,1, 2, 1, 3,3],
      theta=categories,
      fill='toself',
      name='ESP32'              #esp32
))

fig.add_trace(go.Scatterpolar(
      r=[1, 1, 1,1, 1, 2,1],
      theta=categories,
      fill='toself',
      name='ESP8266'
))

fig.add_trace(go.Scatterpolar(
      r=[1, 1, 1, 1,1,1, 1],
      theta=categories,
      fill='toself',
      name='IDEAL'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 3]
    )),
  showlegend=True
)

fig.show()