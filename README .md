# FastAPI Product API

A simple FastAPI project that returns product data from an in-memory list.

## Project Files

- `main.py` - FastAPI app and API routes
- `model.py` - Product data model using Pydantic

## Setup

Create a virtual environment:

```powershell
python -m venv myenv
```

Activate the virtual environment:

```powershell
.\myenv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install fastapi uvicorn
```

## Run the App

Start the FastAPI development server:

```powershell
uvicorn main:app --reload
```

Open the app in your browser:

```text
http://127.0.0.1:8000
```

## API Endpoints

### Home

```http
GET /
```

Returns a greeting message.

### Get All Products

```http
GET /products
```

Returns the full product list.

### Get Product by ID

```http
GET /product/{id}
```

Example:

```text
http://127.0.0.1:8000/product/1
```

Returns one product by its ID.

## API Docs

FastAPI automatically creates interactive API documentation:

```text
http://127.0.0.1:8000/docs
```
