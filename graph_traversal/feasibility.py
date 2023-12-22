import logging
from domain_models.decisions.feasibility import Feasibility
import networkx as nx

def get_feasibility(filtered_graph: nx.DiGraph, fully_connected_graph: nx.DiGraph, agent_name: str, target_node: str, lenses=[]):            
    is_feasible = filtered_graph.nodes[target_node].get('feasibility', Feasibility.INFEASIBLE) in [Feasibility.FEASIBLE, Feasibility.ATTAINED]
    if is_feasible:
        return Feasibility.FEASIBLE
    
    try:
        has_path = len(nx.shortest_path(fully_connected_graph, f"agent:{agent_name}", target_node)) > 0
        if has_path:
            return Feasibility.FEASIBLE_IF
    except Exception as e:
        logging.error("Error in get_feasibility", exc_info=e)
    
    return Feasibility.INFEASIBLE