"""
.py

Simple power system graph:
- Nodes: substations/switchyards
- Edges: lines/transformers
- Edge weights: distance (mi) and impedance (R, X) with derived |Z|
"""

from math import sqrt
import networkx as nx


def z_mag(r_ohm: float, x_ohm: float) -> float:
    return sqrt(r_ohm**2 + x_ohm**2)


def main() -> None:
    G = nx.Graph()

    # Nodes (substations / switchyards)
    G.add_nodes_from(["SS_A", "SS_B", "SS_C", "SS_D"])

    # Edges (lines/transformers) with distance + impedance
    G.add_edge("SS_A", "SS_B", element="line", miles=18.2, r=1.85, x=8.40)
    G.add_edge("SS_B", "SS_C", element="line", miles=26.5, r=3.20, x=12.10)
    G.add_edge("SS_C", "SS_D", element="line", miles=11.0, r=1.10, x=4.60)
    G.add_edge("SS_B", "SS_D", element="transformer", miles=0.0, r=0.25, x=2.10)

    # Add a derived weight |Z| to each edge (useful for "impedance-weighted" paths)
    for u, v, data in G.edges(data=True):
        data["z"] = z_mag(data["r"], data["x"])

    print("Nodes:", list(G.nodes()))

    print("\nEdges:")
    for u, v, data in G.edges(data=True):
        print(f"  {u} -- {v} | {data['element']} | miles={data['miles']}, R={data['r']}, X={data['x']}, |Z|={data['z']:.3f}")

    # Example: shortest path by distance (miles)
    path_mi = nx.shortest_path(G, "SS_A", "SS_D", weight="miles")
    dist_mi = nx.shortest_path_length(G, "SS_A", "SS_D", weight="miles")
    print(f"\nShortest path by distance SS_A -> SS_D: {path_mi}  (total miles={dist_mi:.2f})")

    # Example: shortest path by impedance magnitude |Z|
    path_z = nx.shortest_path(G, "SS_A", "SS_D", weight="z")
    dist_z = nx.shortest_path_length(G, "SS_A", "SS_D", weight="z")
    print(f"Shortest path by impedance SS_A -> SS_D: {path_z}  (total |Z|={dist_z:.3f})")


if __name__ == "__main__":
    main()