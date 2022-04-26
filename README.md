# Github for MDM2 Project: Analysing data from a team’ s season to inform strategies for playing them in the future; An example with Barcelona 20/21

This project analyses free available data from Statsbomb.com.
Its goal is to analyses a team's matches in order to inform strategies for playing against them.


### attackdirection.ipynb

This analyses the location of shot and the passes made leading up to each pass in order to determine the relative frequency of attacks from different parts of the pitch.

### pass_graph.ipynb

This considers all the passes made by Barcelona in the season. To turn this into a graph, it creates a list of nodes from all the different players who made passes. Each directed edge represents a each unique combination combination between players. The weight of the edge is calculated from the number of passes made along it. Centrality measures are applied to the graph to calculate which players are most important for passing. This also outputs the results to player_centralities.xlsx.

### player-xT.ipynb

This analyses all the events of Barcelona in the season and considers all passes and carries. For each event it calculates the change in expected threat from before and after the event. For each player, the total change in expected threat is calculated across all their events. This also outputs the results to player_xt.xlsx

### player_pass_graph.ipynb
This analyses all the events of Barcelona in the season and considers all passes. It creates a plot representing all the passes of a player using mplsoccer. This is done for Lionel Messi and Jordi Alba.

### player_pie_chart.ipynb
This analyses all the events of Barcelona in the season and considers passes, shots and carries. For each player it stores the number of each event. It then creates pie charts for the players, done for Lionel Messi and Jordi Alba.

### top_players.ipynb
This inputs the results from player_centralities.xlsx and player_xt.xlsx . A total score is calculated for each player and they are ranked by it. The results is outputted to player_ranking.xlsx
