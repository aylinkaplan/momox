# Requirements

* Python (3.7)
* Flask (2.2.2)


# Installation
```
> python3 -m venv vev
> source venv/bin/activate
> pip install -r requirements.txt 
```

Run Code

```
> python main.py 
```

Examples with curl:
```
> curl --request POST 'http://127.0.0.1:8000/orders' --header 'Content-Type: application/xml' --data-binary 'employee_orders.xml'
```

