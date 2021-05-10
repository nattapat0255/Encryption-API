# Encryption-API

## Project setup
```
pip install -r requirements.txt
```

### Compiles
```
export FLASK_APP=api.py
```
```
flask run 
```

### Unittest
```
python test.py 
```

### API Documentation
1. POST Encrypt
```
POST http://localhost:5000/encrypt (with JSON Body)
{
  "data" : [
    {
        "text": "Message1"
    },
    {
        "text": "Message2"
    }
  ]
}
```
Response
```
{
  "data": [
      {
          "encrpyted": "5TkOr3EEVZJmfn4OtCePTsPBCLGrejdsMr3c2di1kC0="
      },
      {
          "encrpyted": "4E474hXY9smf7YDyf82FAW0SvLo00MGOCZLcn5rf1m4="
      }
  ]
}
```

2. POST Decrypt
```
POST http://localhost:5000/decrypt (with JSON Body)
{
  "data": [
      {
          "encrpyted": "5TkOr3EEVZJmfn4OtCePTsPBCLGrejdsMr3c2di1kC0="
      },
      {
          "encrpyted": "4E474hXY9smf7YDyf82FAW0SvLo00MGOCZLcn5rf1m4="
      }
  ]
}
```
Response
```
{
  "data" : [
    {
        "text": "Message1"
    },
    {
        "text": "Message2"
    }
  ]
}
```