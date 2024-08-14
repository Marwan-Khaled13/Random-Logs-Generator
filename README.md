# Random Sentence Logger

## Overview

This script generates and logs random sentences at specified intervals. It reads configuration settings from a `.ini` file and data from a JSON file to create sentences composed of subjects, verbs, objects, and adverbs. The sentences are logged to both a file and the console at various log levels.

## Features

- **Configurable Logging**: Set up logging with custom folder, file, and log level.
- **Data-Driven Sentences**: Generate sentences from data loaded from a JSON file.
- **Random Logging**: Logs sentences at random log levels.
- **Continuous Operation**: Logs messages at a user-defined interval.

## Requirements
Use `pip install -r requirements.txt` to install any missing packages, if there exists.
- Python 3.x
- `configparser`
- `json` (standard library)
- `logging` (standard library)
- `os` (standard library)
- `random` (standard library)
- `time` (standard library)


## Configuration

The script uses a configuration file (`config.ini`) and a JSON data file (`words.json`).

### Configuration File (`config.ini`)

```ini
[logging]
log_folder = logs
log_file = generated_logs.log
log_level = NOTSET

[data]
data_folder = data
json_file = words.json

[settings]
interval = 1
```

- **[logging]**: Specifies the logging configuration.
  - `log_folder`: Directory where log files are saved.
  - `log_file`: Name of the log file.
  - `log_level`: Logging level (e.g., `NOTSET`, `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).

- **[data]**: Specifies the location of the data file.
  - `data_folder`: Directory where the JSON file is located.
  - `json_file`: Name of the JSON file.

- **[settings]**: Miscellaneous settings.
  - `interval`: Time interval (in seconds) between logging messages.

### Data File (`words.json`)

The JSON file should have the following structure:

```json
{
  "subjects": ["The cat", "A dog", "A bird"],
  "verbs": ["jumps", "runs", "flies"],
  "objects": ["over the fence", "through the park", "in the sky"],
  "adverbs": ["quickly", "silently", "loudly"]
}
```

## Usage

1. **Prepare Configuration and Data Files**:
   - Create a `config.ini` file with your desired logging and data settings.
   - Prepare a `words.json` file with lists of subjects, verbs, objects, and adverbs.

2. **Run the Script**:
   ```bash
   python logs_generator.py
   ```

3. **Observe the Output**:
   - Logs will be written to the specified log file and displayed in the console.
   - Messages will be logged at random intervals as defined in the configuration.

## Functions

- **load_config(config_file="config.ini")**: Loads configuration from the specified `.ini` file.
- **setup_logging(log_folder, log_file, log_level)**: Configures logging based on provided parameters.
- **load_data(data_folder, json_file)**: Loads data from the JSON file and returns lists of subjects, verbs, objects, and adverbs.
- **RandomSentenceLogger**: A class to generate and log random sentences.
  - **generate_random_sentence()**: Creates a random sentence with a random number.
  - **log_random_message()**: Logs a generated sentence at a random log level.
  - **start_logging(interval)**: Continuously logs messages at the specified interval.
- **main()**: The main entry point for the script.

## Troubleshooting

- **File Not Found**: Ensure that the paths in `config.ini` are correct and the files exist.
- **JSON Errors**: Verify that the JSON file is properly formatted and contains the required fields.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
