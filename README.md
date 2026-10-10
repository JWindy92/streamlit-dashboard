# Data Dashboard

An independent Streamlit application for exploring personal data.

## Local development

Activate your existing Conda environment:

```bash
conda activate <your-environment>
pip install -r requirements.txt
pytest
streamlit run app.py
```

The application defaults to `sample_data/activity.json`.

To load real data, set `LETTERBOXD_DATA_PATH` to the JSON file path.

## Docker

```bash
docker compose up --build -d
```

Open http://localhost:8501.

The dashboard reads pipeline output through a read-only mount. It does not execute or import pipeline code.

## Tests

```bash
pytest
```