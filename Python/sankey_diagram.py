import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ["DAUq", 
               "Users w Wallet", "Users w/o Wallet",
               "Pushcard Exposed", "None Exposure", 
               "Clickers", "None Clickers", "Dismissers",
               "Claimers", "Not Claimers",
               "30d Retention", "Not 30d Retention",
               "180d Retention", "Not 180d Retention" , "None of above" 
               ], #   
      # color = "blue"
    ),
    link = dict(
        source = [0,0,1,1,2,2,3,3,3,4, 5,5,6, 7, 8, 8, 9, 10,10,11,11], 
        target = [1,2,3,4,3,4,5,6,7,14,8,9,14,14,10,11,14,12,13,12,13],
        value  = [300,700, # 0
                  150,150,
                  400,300,
                  400,100,50,
                  450,
                  400, 50, # 5
                  100,
                  50,
                  300,50,
                  50,
                  250,50,
                  25, 25]
      )
    )
]
)

fig.update_layout(title_text="Basic Sankey Diagram", font_size=15)

fig.update_layout(
    hovermode = 'x', #   ['x', 'y', 'closest', False, 'x unified', 'y unified']
    title="NFL CA Claimers",
    font=dict(size = 10, color = 'white'),
    plot_bgcolor='black',
    paper_bgcolor='black'
)

fig.show()
