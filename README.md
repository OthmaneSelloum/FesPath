# A* Graph Theory Project 🚀

Welcome to the **Mini Projet de théorie des graphes en utilisant A***! This project explores graph theory concepts and implements the A* algorithm to solve navigation problems in the beautiful city of Fès, Morocco.

## 🌟 Features

- **Graph Representation**: Extract and visualize city maps using OpenStreetMap data.
- **A* Algorithm**: Efficiently find the shortest path between two locations.
- **Coordinate Extraction**: Process location data to generate coordinates for specific points of interest.
- **Interactive Visualizations**: View the computed paths on dynamic maps.
- **Customizable Inputs**: Specify start and end locations easily.

## 📂 Project Structure

1. **Python Scripts**:
   - `LocationCordonnate.py`: Handles coordinate extraction.
   - `LocationExtraction.py`: Processes location data for graph representation.
   - `ShortPathFinder.py`: Implements the A* algorithm for shortest path computation.

2. **Documentation**:
   - This README file provides an overview of the project.

3. **Version Control**:
   - Managed using Git, with the `.git` directory included for tracking changes.

4. **IDE Configuration**:
   - `.idea` directory for PyCharm settings.

## 🔧 Setup Instructions

### Prerequisites
Make sure you have Python 3.8+ installed along with the following libraries:

```bash
pip install osmnx networkx geopy matplotlib folium
```

### How to Run

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Run the Python scripts individually or integrate them into a larger pipeline:
   - For coordinate extraction:
     ```bash
     python LocationCordonnate.py
     ```
   - For location data processing:
     ```bash
     python LocationExtraction.py
     ```
   - For shortest path calculation:
     ```bash
     python ShortPathFinder.py
     ```

## 🌍 Using the Project

1. **Graph Construction**:
   - The script fetches map data for Fès and builds a graph.

2. **Path Finding**:
   - Input start and end locations in the GUI or directly in the code.
   - The A* algorithm calculates the shortest path and displays it on a map.

3. **Visualization**:
   - Dynamic maps show the computed paths and important nodes.

## 📊 Example Output

- **Graph Visualization**: Nodes and edges representing Fès streets.
- **Shortest Path**: Highlighted route between two chosen locations.

## 🚀 Future Enhancements

- Support for additional cities.
- Integration with live traffic data.
- Enhanced user interface.



## 🙌 Acknowledgments

- **OpenStreetMap** for providing map data.
- **Python Libraries** for simplifying graph theory tasks.

Feel free to explore, contribute, or suggest improvements! 😄

