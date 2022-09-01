import streamlit as st
import graphviz as graphviz

# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge('run', 'intr')
graph.edge('intr', 'runbl')
graph.edge('runbl', 'run')
graph.edge('run', 'kernel')
graph.edge('kernel', 'zombie')
graph.edge('kernel', 'sleep')
graph.edge('kernel', 'runmem')
graph.edge('sleep', 'swap')
graph.edge('swap', 'runswap')
graph.edge('runswap', 'new')
graph.edge('runswap', 'runmem')
graph.edge('new', 'runmem')
graph.edge('sleep', 'runmem')

st.graphviz_chart(graph)

st.sidebar.header('Resources')
st.sidebar.markdown('''
- [test1](https://afafore1-teststreamlitapp-streamlit-app-v046h1.head.streamlit.run/)
- [test2](https://afafore1-teststreamlitapp-streamlit-app-v046h1.head.streamlit.run/)
- [test3](https://afafore1-30days-streamlit-app-b0kqv2.head.streamlit.run/)
''')
