## Serialization tool in python
An exercise to serialize user-data from a csv file to multiple formats. Tested with *Python 2.7.15*

### Folder Structure

```text
.
├── config.py       # configurations for file location etc.
├── modules         # classes to handle exporters and serializers.
├── output          # generated output files.
├── serialize.py    # CLi Tool <------ run this. 
├── test_data.csv   # User input data in csv format.
└── unit_tests.py   # Basic unit tests
```

### Utilization

```bash
python serialize.py
```

#### Output generated formats
* html
* text

#### Serialized formats
* json
* pickle binary