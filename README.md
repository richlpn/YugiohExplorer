# NiceGUI Project

This project is built using [NiceGUI](https://nicegui.io/), a Python library for creating web-based user interfaces with ease.

## Requirements

- Python 3.13 or higher
- NiceGUI library

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

## Usage

Run the application:
```bash
python main.py
```

Access the application in your browser at `http://localhost:8080`.

## Project Structure

```
.
├── main.py          # Entry point of the application
├── src/      # Source Package
|    ├─ states/      # States handlers
|    ├─ models/      # Entity Models
|    ├─ service/      # Bussines Logic
|    └─ pages/      # Custom UI components
├── prisma/      # Source Package
|    └─ schema.prisma      # Data model
├── static/          # Static assets (CSS, JS, images)
└── README.md        # Project documentation
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [NiceGUI Documentation](https://nicegui.io/documentation)
- Python Community
- Open-source contributors