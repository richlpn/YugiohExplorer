# About

This project is a way to explore alternatives to Streamlit. 

This project was built using [NiceGUI](https://nicegui.io/), a Python library for creating web-based user interfaces with ease. Differently from Streamlit, NiceGUI focus on providing flexible and performant web apps (not only dashboards). The performance requirements comes from the necessity of being able to run on micro-controllers (where resources are scarcer then regular computers). In addition to the default components styles, NiceGUI also provide a interface with famous styling libraries such as TailwindCSS.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/richlpn/YugiOhExplorer.git
    cd YugiohExplorer
    ```

2. Start the containers:
    ```bash
    docker compose up -d
    ```

Access the application in your browser at `http://localhost:8080`.

## Project Structure

```
.
├── frontend/               # Main application code (NiceGUI pages, logic)
│   ├── src
│   |   ├── schema          # Entity data schemas. 
│   │   ├── state           # Function that controll (fetching, transforming, etc...) the data (schemas) states. 
│   │   ├── ui              # Interface complex components. 
│   │   └── __init__.py     
│   ├── main.py             # Entry point for NiceGUI app
│   └── requirements.txt    # Frontend Python dependencies.
├── backend/                # Search API
│   ├── src
│   |   ├── schema          # Entity data schemas. 
│   │   └── __init__.py     
│   ├── dockerfile          # Docker image definition.
│   ├── main.py             # Entry point for NiceGUI app
│   └── requirements.txt    # Frontend Python dependencies.
├── data/                   # Datasets and Faiss Index.    
├── docker-compose.yml      # Docker Compose configuration
├── requirements.txt        # Python dependencies
└──README.md                # Project documentation
```
## Contributing

Altough pull requests are welcomed, they aren't the priority. This is only a side project!

## Acknowledgments

- [NiceGUI Documentation](https://nicegui.io/documentation)
- Python Community
- Open-source contributors