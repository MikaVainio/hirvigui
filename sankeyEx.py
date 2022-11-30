import plotly.graph_objects as charts

# Labels for the sankey chart (from a view)
sourceLabels = ['Hirvi', 'Peura']
targetLabels = ['Ryhmä 1', 'Ryhmä 2', 'Ryhmä 3']
labels = sourceLabels + targetLabels
print(labels)

# Data from the database view
dBdata = [('Hirvi', 'Ryhmä 1', 100),
    ('Hirvi', 'Ryhmä 2', 200),
    ('Hirvi', 'Ryhmä 3', 100),
    ('Peura', 'Ryhmä 2', 50)
    ]

rows = len(dBdata)
print(rows)
# Empty lists for label indexses and values
sankeySources = []
sankeyTargets = []
sankeyValues = []

# Create Indexes for sankey chart
for row in dBdata:
    tupleSource = row[0]
    tupleTarget = row[1]
    tupleValue = row[2]
    sourceIx = labels.index(tupleSource)
    targetIx = labels.index(tupleTarget)
    sankeySources.append(sourceIx)
    sankeyTargets.append(targetIx)
    sankeyValues.append(tupleValue)

print(sankeySources)

figure = charts.Figure(data=[charts.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = labels,
      color = ["orange", "teal"]
    ),
    link = dict(
      source = sankeySources, # indices correspond to labels, eg A1, A2, A1, B1, ...
      target = sankeyTargets,
      value = sankeyValues,
      color = ['rgba(255,255,0,100)', "burlywood", "teal"]
  ))])

figure.update_layout(title_text="Basic Sankey Diagram", font_size=10)
figure.show()
