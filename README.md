# Housing Production Plan (HPP) Tool


### Starting the app
#### Using Python
```
pip3 install -e .
hpp
```
#### With Docker + docker-compose
```
docker-compose up
```


### Configuration and Environment

You must assign a PrQL token `PRQL_TOKEN` in the __.env__ file located in the project root.

All config options are listed in all-capped strings in _config/config.py_.

__Note:__ It is not recommended to change the default configurations in the default file when you 
are customizing the execution for you environment. That file is in there to ensure that
the app is usable with little configuration. If you want to override the default configuration,
you should override the environment variables with a __.env__ file.
